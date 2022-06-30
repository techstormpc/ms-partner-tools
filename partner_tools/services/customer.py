from typing import List

from partner_tools.services.base import BaseService
from partner_tools.models.autopilot_device import AutopilotDevice
from partner_tools.models.customer import Customer


class CustomerService(BaseService):
    """
    Tools for interacting with the customers endpoint
    """
    base_url = 'customers'

    def enroll_devices(self, devices: List[AutopilotDevice], customer_id: str, batch_name: str):
        """
        Enrolls devices into the customers Autopilot system
        :param devices: A list of devices using the
        :param customer_id: The customers tenant ID
        :param batch_name: can be anything to group the devices
        :return:
        """
        url = f'{self.base_url}/{customer_id}/deviceBatches/{batch_name}/devices'
        return self._api_client.post(url, devices)

    def get_customers(self) -> List[Customer]:
        """
        :return a list of customers you have relationships with
        """
        resp = self._api_client.get(self.base_url)
        return resp.json()['items']
