from abc import ABC

from partner_tools.clients.api import ApiClient


class BaseService(ABC):
    def __init__(self, api_client: ApiClient):
        self._api_client = api_client
