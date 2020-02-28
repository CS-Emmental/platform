import kubernetes
import yaml
from flask import current_app

from challenges.model import Challenge
from challenge_participations.model import ChallengeParticipation
from challenges.manager import ChallengesManager


def deploy_challenge_instance(challenge: Challenge, participation: ChallengeParticipation):
    challenge_id = challenge.challenge_id
    challenge_name_slug = challenge.title.replace(" ", "-").lower()
    participation_id = participation.participation_id
    port = int(challenge.ports[0]["port"])
    port_name = challenge.ports[0]["name"]
    image = challenge.image
    identifier = challenge_name_slug + "-" + participation_id

    with open("./kubernetes_controller/manifest.yaml") as f:
        deployment, service, config_map = yaml.load_all(f, Loader=yaml.FullLoader)

    deployment["metadata"]["name"] = identifier
    deployment["metadata"]["labels"]["challenge_id"] = challenge_id
    deployment["metadata"]["labels"]["participation_id"] = participation_id
    deployment["spec"]["selector"]["matchLabels"]["challenge_id"] = challenge_id
    deployment["spec"]["selector"]["matchLabels"]["participation_id"] = participation_id
    deployment["spec"]["template"]["metadata"]["labels"]["challenge_id"] = challenge_id
    deployment["spec"]["template"]["metadata"]["labels"]["participation_id"] = participation_id
    deployment["spec"]["template"]["spec"]["containers"][0]["name"] = challenge_name_slug
    deployment["spec"]["template"]["spec"]["containers"][0]["image"] = image
    deployment["spec"]["template"]["spec"]["containers"][0]["ports"][0]["containerPort"] = port
    deployment["spec"]["template"]["spec"]["volumes"][0]["configMap"]["name"] = "configmap-" + participation_id

    service["metadata"]["name"] = identifier
    service["metadata"]["labels"]["challenge_id"] = challenge_id
    service["metadata"]["labels"]["participation_id"] = participation_id
    service["spec"]["selector"]["challenge_id"] = challenge_id
    service["spec"]["selector"]["participation_id"] = participation_id
    service["spec"]["ports"][0]["name"] = port_name
    service["spec"]["ports"][0]["port"] = port

    config_map["metadata"]["name"] = "configmap-" + participation_id
    config_map["metadata"]["labels"]["challenge_id"] = challenge_id
    config_map["metadata"]["labels"]["participation_id"] = participation_id
    config_map["data"]["secret"] = "root:" + participation_id

    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="emmental-challenges")

    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)
    k8s_core_v1.create_namespaced_config_map(body=config_map, namespace="emmental-challenges")
    resp = k8s_core_v1.create_namespaced_service(
        body=service, namespace="emmental-challenges", pretty="true"
    )
    participation.port = resp.spec.ports[0].node_port

    return participation


def stop_challenge_instance(challenge: Challenge, participation: ChallengeParticipation):
    """
    Send a request to k8s for stopping the challenge instance linked to this ChallengeParticipation
    """
    challenge_name_slug = challenge.title.replace(" ", "-").lower()
    participation_id = participation.participation_id
    name = challenge_name_slug + "-" + participation_id

    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)

    k8s_apps_v1.delete_namespaced_deployment(name=name, namespace="emmental-challenges")
    k8s_core_v1.delete_namespaced_service(name=name, namespace="emmental-challenges")

    return "deleted"
