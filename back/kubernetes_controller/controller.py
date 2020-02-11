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
    image = "sqli1" # TODO lol on peut lancer que ça
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
    configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFwaS1kZXBsb3ktc2VydmljZS10b2tlbi05ejVubiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhcGktZGVwbG95LXNlcnZpY2UiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI1ZjBmMTEzZC00ZDE3LTExZWEtYTkxZi0wODAwMjcxYWVlZTMiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDphcGktZGVwbG95LXNlcnZpY2UifQ.k9_gwEKMYDjLv9RXgUUemRTVu9X0WHyZ05rz8mi--_WvebSl1LVaCqWLKeHOqpM_tLWli-H7nlKcLthkfwJMpWnJrplBOeKqxrWEGGVFvcx3-DvcAALakb3v6_a6-zjXeLvBu-MPcrisFs5aUKh-5g0Y4tgpzmtfeJkawtDGrn8xvbPHycQhLzuLJHhiEjm_Z_P-lDuLo4UkNxXRuaLuW3xCICA8ALzxwcRA93OP2MrSQmWAauMmClAfKSwVSbK8S6fsVTvXvNGUfixV5e1hcMK1akcLowc0rdHVOS8q7I4eHJRzwRVem7WuI5yZ6vDB6CV-7dNDlJlf8kh6fVsW3w'
    configuration.api_key_prefix['authorization'] = 'Bearer'
    apiClient = kubernetes.client.ApiClient(configuration)

    k8s_apps_v1 = kubernetes.client.AppsV1Api(apiClient)
    resp = k8s_apps_v1.create_namespaced_deployment(body=deployment, namespace="default")

    k8s_v1 = kubernetes.client.CoreV1Api(apiClient)
    resp2 = k8s_v1.create_namespaced_service(body=service, namespace="default", pretty='true')
    participation.port = resp2.spec.ports[0].node_port

    return participation