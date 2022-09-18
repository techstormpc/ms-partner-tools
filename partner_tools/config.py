import configparser
import csv
import os
import shutil
from functools import lru_cache
from pathlib import Path
from typing import NamedTuple, List

from partner_tools.models.autopilot_device import CommonDevice


CONFIG_LOCATION = "~/.ms-partner-tools"


class AuthConfig(NamedTuple):
    method: str
    client_id: str
    client_secret: str
    tenant_id: str


def get_config_directory() -> Path:
    config_location = os.environ.get('PARTNER_TOOLS_CONFIG', CONFIG_LOCATION)
    config_dir = Path(config_location).expanduser()
    config_dir.mkdir(exist_ok=True)
    return config_dir


@lru_cache(maxsize=None)
def load_device_options() -> List[CommonDevice]:
    config_dir = get_config_directory()
    devices_path = Path(config_dir, 'devices.csv')

    # Initialize devices file based on template
    if not devices_path.exists():
        repo_dir = Path(__file__).resolve().parent.parent
        template_file = Path(repo_dir, 'common_devices.csv')
        shutil.copy(template_file, devices_path)

    with devices_path.open() as devices_file:
        reader = csv.DictReader(devices_file)
        return [
            CommonDevice(
                manufacturer=row['manufacturer'],
                model=row['model']
            )
            for row in reader
        ]


def save_config(auth_config: AuthConfig):
    ini_config = configparser.SafeConfigParser()
    ini_config['DEFAULT'] = auth_config._asdict()
    config_dir = get_config_directory()
    config_path = Path(config_dir, 'config.ini')
    with config_path.open('w') as configfile:
        ini_config.write(configfile)


def load_config() -> AuthConfig:
    config_dir = get_config_directory()
    config_path = Path(config_dir, 'config.ini')
    if not config_path.exists():
        raise RuntimeError('Please configure authentication by running partnertools-cli configure')
    ini_config = configparser.ConfigParser()
    ini_config.read(str(config_path.absolute()))
    auth_config_section = ini_config['DEFAULT']
    return AuthConfig(
        auth_config_section.get('method'),
        auth_config_section.get('client_id'),
        auth_config_section.get('client_secret'),
        auth_config_section.get('tenant_id'))
