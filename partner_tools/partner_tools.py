from partner_tools.auth.auth_info import AuthInfo
from partner_tools.clients.api import ApiClient
from partner_tools.services.customer import CustomerService


class PartnerTools:
    """
    Client for the Microsoft Partner Center REST API.
    """
    def __init__(self, auth_info: AuthInfo):
        self._api_client = ApiClient(auth_info)
        self._customer_service = CustomerService(self._api_client)

    @property
    def customer(self):
        return self._customer_service
