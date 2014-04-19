from functools import wraps
import requests
import json

from django.conf import settings


class ApiWorker(object):
    def __init__(self, function, endpoint):
        self.func = function
        self.endpoint = endpoint

    def __call__(self, *args, **kwargs):
        g = self.func.func_globals
        params = args[1:]
        endpoint = self.endpoint.format(*params)
        url = 'http://{0}/{1}'.format(
            settings.JTF_WORKER_API_HOST, endpoint
        )
        g['api_result'] = json.loads(requests.get(url).text)
        return self.func(*args, **kwargs)


def fetch_from_api_worker(endpoint):
    def fetch(function):
        return ApiWorker(function, endpoint)
    return fetch
