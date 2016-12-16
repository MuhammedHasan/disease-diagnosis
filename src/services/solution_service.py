from typing import List
import json
import time
import logging

import requests


class SolutionService(object):

    def __init__(self):
        self.url = 'http://metabolitics.biodb.sehir.edu.tr/api3/'
        self.logger = logging.getLogger('solution-services')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('../logs/solution-services.log')
        handler.setFormatter(
            logging.Formatter("%(asctime)s;%(levelname)s;%(message)s"))
        self.logger.addHandler(handler)

    def _get_key(self, concentration_changes: dict):
        data = self._key_request_body(concentration_changes)
        req = requests.post('%ssubsystems-analyze-start-async' % self.url,
                            data=json.dumps(data),
                            headers={'content-type': 'application/json'})
        key = req.json()
        self.logger.info(key)
        return key

    def _key_request_body(self, concentration_changes: dict):
        return {
            'name': 'my anaylsis',
            'concentrationChanges': [
                {'name': k, 'change': v}
                for k, v in concentration_changes.items()
            ]
        }

    def _get_solution(self, key: str):
        req = requests.get('%ssubsystems-analyze/%s' % (self.url, key))
        while req.text == 'null':
            time.sleep(10)
            req = requests.get('%ssubsystems-analyze/%s' % (self.url, key))
            self.logger.info('data is not ready')
        output_data = req.json()
        self.logger.info('len(solution): %d' % len(output_data))
        return output_data

    def get_solution(self, concentration_changes: dict):
        key = self._get_key(concentration_changes)
        solution = self._get_solution(key)
        return solution

    def get_solutions(self, X: List[dict]):
        return [self.get_solution(x) for x in X]
