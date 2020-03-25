from jinja2 import Environment, FileSystemLoader
import yaml
from flask import current_app
from kubernetes.client.rest import ApiException
from core.utils import slug
import kubernetes


def deploy_challenge_instance(
    challenge_id: str, challenge_title: str, participation_id: str, containers: dict
):
    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)
    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_network_v1 = kubernetes.client.NetworkingV1Api(current_app.k8s)

    jinja = Environment(
        loader=FileSystemLoader(searchpath="./kubernetes_controller"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template_context = {
        "challenge_name_slug": slug(challenge_title),
        "participation_id": participation_id,
        "challenge_id": challenge_id,
        "secret": participation_id,
        "containers": containers["containers"],
        "exposed": containers["exposed"],
    }
    rendered_templates = "\n".join(
        [
            jinja.get_template(f"templates/{k}.yaml.j2").render(template_context)
            for k in ("deployment", "service", "configmap", "network_policy",)
        ]
    )
    manifests = yaml.load_all(rendered_templates)

    # Create all Kubernetes resources
    try:
        for manifest in manifests:
            if manifest["kind"] == "Deployment":
                k8s_apps_v1.create_namespaced_deployment(
                    body=manifest, namespace="emmental-challenges"
                )
            elif manifest["kind"] == "Service":
                service_resp = k8s_core_v1.create_namespaced_service(
                    body=manifest, namespace="emmental-challenges"
                )
            elif manifest["kind"] == "ConfigMap":
                k8s_core_v1.create_namespaced_config_map(
                    body=manifest, namespace="emmental-challenges"
                )
            elif manifest["kind"] == "NetworkPolicy":
                k8s_network_v1.create_namespaced_network_policy(
                    body=manifest, namespace="emmental-challenges"
                )
    except ApiException as err:
        # Clean any resource which may have been created
        stop_challenge_instance(challenge_title, participation_id)
        raise err

    # WIP to get a local DNS
    # Each container would have had all of the others IP addresses in /etc/hosts.
    # But patching a deployment recreates the pods
    # thus changing the IPs, so we can't do it that way.
    # We should have an external DNS server and use its API tu dynamically add or remove entries.
    # But responses to requests should depend on the pod who initiated the request
    # because each instance of a challenge will use different IP addresses for the same DNS name

    # Most of this code is necessary to get the pod's addresses
    # and will be useful when another solution is implemented

    # # Get the Pods IPs
    # label_selector = (f"tier=challenge-instances,challenge_id={challenge_id},"
    #     f"participation_id={participation_id}")
    # res = k8s_core_v1.list_namespaced_pod(
    #     label_selector=label_selector,
    #     namespace="emmental-challenges"
    #     )
    # pods = res.items

    # pods_without_ip = [p.metadata.name for p in pods if not p.status.pod_ip]
    # pods_ips = {
    #     p.metadata.labels["container"]: p.status.pod_ip
    #     for p in pods if p.status.pod_ip
    # }
    # tries = 0
    # while (len(pods_without_ip) > 0 and tries < 10):
    #     sleep(0.5)
    #     tries += 1
    #     pods_without_ip_iter = pods_without_ip[:]
    #     for pod in pods_without_ip_iter:
    #         pod_state = k8s_core_v1.read_namespaced_pod(pod, namespace="emmental-challenges")
    #         if pod_state.status.pod_ip:  # IP allocated
    #             pods_ips[pod_state.metadata.labels["container"]] = pod_state.status.pod_ip
    #             pods_without_ip.remove(pod)

    # if len(pods_without_ip) != 0:
    #     raise Exception

    # # Add these IPs with a hostAliases entry in the Deployments
    # patch_template = jinja.get_template(f"templates/deployment_patch.yaml.j2")
    # patch_manifest = patch_template.render({"pods_ips": pods_ips})
    # print(patch_manifest)
    # deployment_name_prefix = f"{slug(challenge_title)}-{participation_id}-"
    # for cname in containers["containers"]:
    #     k8s_apps_v1.patch_namespaced_deployment(
    #         name=deployment_name_prefix + cname,
    #         namespace="emmental-challenges",
    #         body=patch_manifest)

    return service_resp.spec.ports[0].node_port


def stop_challenge_instance(challenge_title: str, participation_id: str):
    """
    Send a request to k8s that stop the challenge instance linked to this ChallengeParticipation
    """
    name = f"{slug(challenge_title)}-{participation_id}"
    label_selector = f"tier=challenge-instances,participation_id={participation_id}"

    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)
    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_network_v1 = kubernetes.client.NetworkingV1Api(current_app.k8s)

    try:
        k8s_apps_v1.delete_collection_namespaced_deployment(
            label_selector=label_selector, namespace="emmental-challenges"
        )
    except ApiException as err:
        if err.status != 404:
            # Else the object we want to delete does not exist, which is okay
            raise err
        else:
            print(
                f"Warning: Deployments matching labelSelector='{label_selector}' not found."
            )
    try:
        k8s_core_v1.delete_namespaced_service(
            name=name, namespace="emmental-challenges"
        )
    except ApiException as err:
        if err.status != 404:
            # Else the object we want to delete does not exist, which is okay
            raise err
        else:
            print(f"Warning: Service '{name}' not found.")
    try:
        k8s_core_v1.delete_collection_namespaced_config_map(
            label_selector=label_selector, namespace="emmental-challenges"
        )
    except ApiException as err:
        if err.status != 404:
            # Else the object we want to delete does not exist, which is okay
            raise err
        else:
            print(
                f"Warning: Configmaps matching labelSelector='{label_selector}' not found."
            )
    try:
        k8s_network_v1.delete_collection_namespaced_network_policy(
            label_selector=label_selector, namespace="emmental-challenges"
        )
    except ApiException as err:
        if err.status != 404:
            # Else the object we want to delete does not exist, which is okay
            raise err
        else:
            print(
                f"Warning: NetworkPolicies matching labelSelector='{label_selector}' not found."
            )
