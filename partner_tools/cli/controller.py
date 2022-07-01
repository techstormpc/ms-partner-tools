from partner_tools import PartnerTools
from partner_tools.auth import DeviceCode
from partner_tools.auth.interactive import Interactive
from partner_tools.cli.interactive.auth_args import gather_login
from partner_tools.cli.interactive.autopilot_args import get_serial_number, get_device
from partner_tools.cli.interactive.common_args import get_customer
from partner_tools.config import save_config, load_config
from partner_tools.models import AutopilotDevice


DEVICE_BATCH_NAME = 'cli-upload'


def get_auth():
    config = load_config()
    if config.method == DeviceCode.__name__:
        return DeviceCode(client_id=config.client_id,
                          client_secret=config.client_secret,
                          tenant_id=config.tenant_id)
    if config.method == Interactive.__name__:
        return Interactive(client_id=config.client_id,
                           tenant_id=config.tenant_id)

    raise RuntimeError(f'Unknown auth method {config.method}')


def run_register_device():
    client = PartnerTools(auth_info=get_auth())

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
