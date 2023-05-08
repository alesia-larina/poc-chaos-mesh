import logging
import sys

from kubernetes import client, config
from kubernetes.client.models import V1Pod
from retry import retry

from libs.exceptions import PodNotRunningError, ContainersNotReadyError


class K8sClient:

    logging.getLogger('k8sclient')
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    def __init__(self):
        config.load_kube_config()
        self.client = client.CoreV1Api()

    def get_pod(self, name: str, ns: str) -> V1Pod:
        pod = self.client.read_namespaced_pod(name=name, namespace=ns)
        return pod

    def pod_running(self, name: str, ns: str) -> bool:
        status = self.get_pod(name, ns).status.phase == 'Running'
        logging.info(f'Checking if pod {name} is up >>> {status}')
        return status

    def containers_running(self, name: str, ns: str) -> bool:
        statuses = all([i.state.running for i in self.get_pod(name, ns).status.container_statuses])
        logging.info(f'Checking if pod {name} containers are ready >>> {statuses}')
        return statuses

    @retry(exceptions=(PodNotRunningError, ), delay=10, tries=30)
    def wait_pods_up(self, name: str, ns: str) -> None:
        logging.info(f'Waiting till pod is up')
        if not self.pod_running(name, ns):
            raise PodNotRunningError

    @retry(exceptions=(ContainersNotReadyError, ), delay=10, tries=60)
    def wait_containers_ready(self, name: str, ns: str) -> None:
        logging.info(f'Waiting till containers are ready')
        if not self.containers_running(name, ns):
            raise ContainersNotReadyError
