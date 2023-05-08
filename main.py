import logging
from retry import retry

from libs.exceptions import PodNotRunningError, ContainersNotReadyError


def containers_ready():
    return all([None])

@retry(exceptions=(ContainersNotReadyError, ), delay=5, tries=10)
def wait_containers_ready() -> None:
    logging.info(f'Waiting till containers are ready')
    if not containers_ready():
        raise ContainersNotReadyError

wait_containers_ready()