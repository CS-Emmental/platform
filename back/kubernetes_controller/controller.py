import kubernetes
import yaml

from challenges.models import Challenge, ChallengeParticipation
from challenges.manager import ChallengesManager

def deploy_challenge_instance(challenge: Challenge, participation: ChallengeParticipation):
    challenge_id = challenge.challenge_id
    challenge_name_slug = challenge.title.replace(' ', '-').lower()
    participation_id = participation.participation_id
    port = int(challenge.ports[0]['port'])
    port_name = challenge.ports[0]['name']
    image = challenge.image
    identifier = challenge_name_slug + '-' + participation_id

    with open('./kubernetes_controller/manifest.yaml') as f:
        deployment, service = yaml.load_all(f, Loader=yaml.FullLoader)

    deployment['metadata']['name'] = identifier
    deployment['metadata']['labels']['challenge_id'] = challenge_id
    deployment['metadata']['labels']['participation_id'] = participation_id
    deployment['spec']['selector']['matchLabels']['challenge_id'] = challenge_id
    deployment['spec']['selector']['matchLabels']['participation_id'] = participation_id
    deployment['spec']['template']['metadata']['labels']['challenge_id'] = challenge_id
    deployment['spec']['template']['metadata']['labels']['participation_id'] = participation_id
    deployment['spec']['template']['spec']['containers'][0]['name'] = challenge_name_slug
    deployment['spec']['template']['spec']['containers'][0]['image'] = image
    deployment['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort'] = port

    service['metadata']['name'] = identifier
    service['metadata']['labels']['challenge_id'] = challenge_id
    service['metadata']['labels']['participation_id'] = participation_id
    service['spec']['selector']['challenge_id'] = challenge_id
    service['spec']['selector']['participation_id'] = participation_id
    service['spec']['ports'][0]['name'] = port_name
    service['spec']['ports'][0]['port'] = port


    kubernetes.config.load_incluster_config()
    
    k8s_apps_v1 = kubernetes.client.AppsV1Api()
    k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")

    k8s_core_v1 = kubernetes.client.CoreV1Api()
    resp = k8s_core_v1.create_namespaced_service(body=service, namespace="default", pretty='true')
    participation.port = resp.spec.ports[0].node_port

    return participation
