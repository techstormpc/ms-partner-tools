import logging
from typing import List

from partner_tools.services.base import BaseService
from partner_tools.models.autopilot_device import AutopilotDevice
from partner_tools.models.customer import Customer


logger = logging.getLogger()


class CustomerService(BaseService):
    """
    Tools for interacting with the customers endpoint
    """
    base_url = 'customers'

    def enroll_devices(self, devices: List[AutopilotDevice],
                       customer_id: str, batch_name: str) -> None:
        """
        Enrolls devices into the customers Autopilot system
        :param devices: A list of devices using the
        :param customer_id: The customers tenant ID
        :param batch_name: can be anything to group the devices
        """
        batches = self._get_device_batches(customer_id)
        matching_batch = next((batch for batch in batches if batch['id'] == batch_name), None)
        if matching_batch is None:
            self._create_device_batch(devices, customer_id, batch_name)
        else:
            self._add_device_to_batch(devices, customer_id, batch_name)

    def get_devices(self, customer_id: str, batch_name: str) -> List[AutopilotDevice]:
        """
        Gets a list of devices in the given batch name from the customer
        """
        url = f'{self.base_url}/{customer_id}/deviceBatches/{batch_name}/devices'
        resp = self._api_client.get(url)
        return resp['items']

    def get_customers(self) -> List[Customer]:
        """
        :return a list of customers you have relationships with
        """
        resp = self._api_client.get(self.base_url)
        return [Customer(**item) for item in resp['items']]

    def get_relationship_request_url(self) -> str:
        """
        :return: the relationship request URL
        """
        resp = self._api_client.get(f'{self.base_url}/relationshiprequests')
        return resp['url']

    # Lower level device methods
    def _add_device_to_batch(self, devices: List[AutopilotDevice],
                             customer_id: str, batch_name: str):
        url = f'{self.base_url}/{customer_id}/deviceBatches/{batch_name}/devices'
        self._api_client.post(url, data=devices)

    def _create_device_batch(self, devices: List[AutopilotDevice],
                             customer_id: str, batch_name: str):
        logging.info(f'Creating new device batch {batch_name}')
        url = f'{self.base_url}/{customer_id}/deviceBatches'
        self._api_client.post(url, data={
            'batchId': batch_name,
            'devices': devices
        })

    def _get_device_batches(self, customer_id):
        url = f'{self.base_url}/{customer_id}/deviceBatches'
        resp = self._api_client.get(url)
        return resp['items']
