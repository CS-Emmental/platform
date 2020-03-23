import kubernetes
import yaml
from flask import current_app
from jinja2 import Environment, FileSystemLoader

from challenge_participations.model import ChallengeParticipation
from challenges.manager import ChallengeManager
from challenges.model import Challenge
from core.utils import slug


def deploy_challenge_instance(
    challenge_id: str,
    challenge_title: str,
    participation_id: str,
    containers: dict
): # TODO : Change calls to that function
    challenge_name_slug = slug(challenge_title)

    jinja = Environment(
        loader=FileSystemLoader(searchpath="./kubernetes_controller"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = jinja.get_template("manifest.yaml.j2")
    templated_manifest = template.render(
            {
                "CHALLENGE_NAME_SLUG": challenge_name_slug,
                "PARTICIPATION_ID": participation_id,
                "CHALLENGE_ID": challenge_id,
                "SECRET": participation_id,
            }
        )
    kubernetes_objects = yaml.load_all(templated_manifest)

    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)
    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_network_v1 = kubernetes.client.NetworkingV1Api(current_app.k8s)

    for k8s_object in kubernetes_objects:
        if k8s_object["kind"] == "Deployment":
            k8s_apps_v1.create_namespaced_deployment(
                body=k8s_object, namespace="emmental-challenges"
            )
        elif k8s_object["kind"] == "Service":
            resp = k8s_core_v1.create_namespaced_service(
                body=k8s_object, namespace="emmental-challenges", pretty="true"
            )
        elif k8s_object["kind"] == "ConfigMap":
            k8s_core_v1.create_namespaced_config_map(
                body=k8s_object, namespace="emmental-challenges"
            )
        elif k8s_object["kind"] == "NetworkPolicy":
            k8s_network_v1.create_namespaced_network_policy(
                body=k8s_object, namespace="emmental-challenges"
            )


    return_port = resp.spec.ports[0].node_port

    return return_port


def stop_challenge_instance(participation_id: str):
    """
    Send a request to k8s that stop the challenge instance linked to this ChallengeParticipation
    """
    label_selector = f"tier%3Dchallenge-instances,participation_id%3D{participation_id}"

    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)
    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_network_v1 = kubernetes.client.ExtensionsV1beta1Api(current_app.k8s)

    k8s_apps_v1.delete_collection_namespaced_deployment(labelSelector=label_selector, namespace="emmental-challenges")
    k8s_core_v1.delete_collection_namespaced_service(labelSelector=label_selector, namespace="emmental-challenges")
    k8s_core_v1.delete_collection_namespaced_config_map(labelSelector=label_selector, namespace="emmental-challenges")
    k8s_network_v1.delete_collection_namespaced_network_policy(labelSelector=label_selector, namespace="emmental-challenges")
