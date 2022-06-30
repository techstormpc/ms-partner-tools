import requests

from partner_tools.auth.auth_info import AuthInfo

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


class ApiClient:
    """
    Provides helper methods to call the partner center REST API
    """

    def __init__(self, auth_info: AuthInfo):
        self.auth_info = auth_info
        self._version = 1
        self._base = 'https://api.partnercenter.microsoft.com'

    @property
    def base_url(self):
        return f'{self._base}/v{self._version}'

    def post(self, path, data=None):
        url = f'{self.base_url}/{path}'
        return requests.post(url,
                             json=data,
                             headers=HEADERS,
                             auth=self.auth_info.get_request_auth())

    def get(self, path, query_params=None):
        url = f'{self.base_url}/{path}'
        return requests.get(url,
                            params=query_params,
                            headers=HEADERS,
                            auth=self.auth_info.get_request_auth())
