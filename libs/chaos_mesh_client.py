import logging
import sys

from chaosmesh.client import Client, Experiment
from chaosmesh.k8s.selector import Selector


class ChaosMeshClient:

    logging.getLogger('chaosmesh')
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    def __init__(self):
        self.client = Client('v1alpha1')

    def start_pod_failure(self, labels: dict, ns: list, expr_name: str) -> None:
        self.client.start_experiment(Experiment.POD_FAILURE,
                                     namespace='chaos-mesh',
                                     name=expr_name,
                                     selector=Selector(labelSelectors=labels, namespaces=ns))

    def delete_pod_failure(self, expr_name: str) -> None:
        self.client.delete_experiment(Experiment.POD_FAILURE,
                                      namespace='chaos-mesh',
                                      name=expr_name)
