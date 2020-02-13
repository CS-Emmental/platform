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

    configuration = kubernetes.client.Configuration()
    configuration.verify_ssl = False # TODO pour théo le plus beau
    configuration.debug = False
    configuration.host = "https://192.168.99.100:8443"
    configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFwaS1kZXBsb3ktc2VydmljZS10b2tlbi03Y2xxZyIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhcGktZGVwbG95LXNlcnZpY2UiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI1YzEyMmZiOC00ZGYwLTExZWEtYjQ3MC0wODAwMjc5OWJlZjUiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDphcGktZGVwbG95LXNlcnZpY2UifQ.SIRWWXmD8K6pbF8jCXIh4UtpZrOg_aZUNbuslYILrWBRNkvkNK8E-DoW9jaV_cn7u1cKl6__qjr4DWAh2gZbvS4PT4YuXaBgxzVnbBUd30-9bRfDR_AemwsUEq9wC5nGDz7g_JVrW5ADoxY2Tyk3UpfxKMi2QL3Zzpcaxo5PeDXR6X01Jty5j2IpUuN2XpGWt3ovA3iEY-hUeAgaOXKURQQnimiTr9djJlI8vVb1Ew0Jvf6pUpTd5K6Vahde9HBMxpKhTxSOnjJAh1ryUVEWhj373BM4AJln4dWZZmEVCbtK2kvwxK4k7de0l5Wn-keM7sn-O9oDHmDSl3sYiES1QA'
    configuration.api_key_prefix['authorization'] = 'Bearer'
    apiClient = kubernetes.client.ApiClient(configuration)

    k8s_apps_v1 = kubernetes.client.AppsV1Api(apiClient)
    resp = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")

    k8s_v1 = kubernetes.client.CoreV1Api(apiClient)
    resp2 = k8s_v1.create_namespaced_service(body=service, namespace="default", pretty='true')
    participation.port = resp2.spec.ports[0].node_port

    return participation