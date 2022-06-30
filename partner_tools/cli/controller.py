from partner_tools import PartnerTools
from partner_tools.auth import DeviceCode
from partner_tools.cli.interactive.auth_args import gather_login
from partner_tools.cli.interactive.autopilot_args import get_serial_number, get_device
from partner_tools.cli.interactive.common_args import get_customer
from partner_tools.config import save_config, load_config
from partner_tools.models import AutopilotDevice


def get_credentials():
    config = load_config()
    return config.client_id, config.client_secret, config.tenant_id


def run_register_device():
    client = PartnerTools(auth_info=DeviceCode(*get_credentials()))

    customers = client.customer.get_customers()

    customer = get_customer(customers)
    device_type = get_device()
    serial = get_serial_number()

    device: AutopilotDevice = {
        'serialNumber': serial,
        'modelName': device_type.model,
        'oemManufacturerName': device_type.manufacturer,
        'hardwareHash': '',
        'productKey': ''
    }
    client.customer.enroll_devices([device], customer['id'], 'cli-upload')

    print()
    print('Device was added')


def run_configure():
    auth_config = gather_login()
    save_config(auth_config)
