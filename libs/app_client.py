import logging
import sys

import requests


class AppClient:

    logging.getLogger('appclient')
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    @property
    def url(self) -> str:
        return 'http://localhost/tutorial'

    def healthcheck(self) -> None:
        logging.info('Performing app\'s healthcheck')
        resp = requests.get(self.url)
        resp.raise_for_status()
