from pytest import fixture

from libs.app_client import AppClient
from libs.chaos_mesh_client import ChaosMeshClient
from libs.k8s_client import K8sClient


@fixture(scope='session')
def app():
    return AppClient()

@fixture(scope='session')
def ch_mesh_cl():
    return ChaosMeshClient()


@fixture(scope='session')
def k8s_cl():
    return K8sClient()
