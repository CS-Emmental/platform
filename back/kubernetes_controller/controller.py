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
    ports: list,
    image: str,
):
    challenge_name_slug = slug(challenge_title)

    jinja = Environment(
        loader=FileSystemLoader(searchpath="./kubernetes_controller"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = jinja.get_template("manifest.yaml.j2")
    deployment, service, config_map = yaml.load_all(
        template.render(
            {
                "CHALLENGE_NAME_SLUG": challenge_name_slug,
                "PARTICIPATION_ID": participation_id,
                "CHALLENGE_ID": challenge_id,
                "IMAGE": image,
                "PORT": ports,
                "SECRET": participation_id,
            }
        )
    )

    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)

    k8s_core_v1.create_namespaced_config_map(
        body=config_map, namespace="emmental-challenges"
    )
    k8s_apps_v1.create_namespaced_deployment(
        body=deployment, namespace="emmental-challenges"
    )
    resp = k8s_core_v1.create_namespaced_service(
        body=service, namespace="emmental-challenges", pretty="true"
    )

    return_port = resp.spec.ports[0].node_port

    return return_port


def stop_challenge_instance(challenge_title: str, participation_id: str):
    """
    Send a request to k8s that stop the challenge instance linked to this ChallengeParticipation
    """
    challenge_name_slug = slug(challenge_title)
    name = challenge_name_slug + "-" + participation_id

    k8s_apps_v1 = kubernetes.client.AppsV1Api(current_app.k8s)
    k8s_core_v1 = kubernetes.client.CoreV1Api(current_app.k8s)

    k8s_apps_v1.delete_namespaced_deployment(name=name, namespace="emmental-challenges")
    k8s_core_v1.delete_namespaced_service(name=name, namespace="emmental-challenges")
    k8s_core_v1.delete_namespaced_config_map(name=name, namespace="emmental-challenges")
