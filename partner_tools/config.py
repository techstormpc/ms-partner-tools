import configparser
import csv
import os
import shutil
from functools import cache
from importlib.resources import files
from pathlib import Path
from typing import NamedTuple

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


@cache
def load_device_options() -> list[CommonDevice]:
    config_dir = get_config_directory()
    devices_path = Path(config_dir, 'devices.csv')

    # Initialize devices file based on template
    if not devices_path.exists():
        template = files('partner_tools.data').joinpath('common_devices.csv')
        with template.open('rb') as src, devices_path.open('wb') as dst:
            shutil.copyfileobj(src, dst)

    with devices_path.open(newline='', encoding='utf-8') as devices_file:
        reader = csv.DictReader(devices_file)
        return [
            CommonDevice(
                manufacturer=row['manufacturer'],
                model=row['model']
            )
            for row in reader
        ]


def save_config(auth_config: AuthConfig):
    ini_config = configparser.ConfigParser()
    ini_config['DEFAULT'] = auth_config._asdict()
    config_dir = get_config_directory()
    config_path = Path(config_dir, 'config.ini')
    with config_path.open('w', encoding='utf-8') as configfile:
        ini_config.write(configfile)


def load_config() -> AuthConfig:
    config_dir = get_config_directory()
    config_path = Path(config_dir, 'config.ini')
    if not config_path.exists():
        raise RuntimeError('Please configure authentication by running partnertools-cli configure')
    ini_config = configparser.ConfigParser()
    ini_config.read(config_path, encoding='utf-8')
    auth_config_section = ini_config['DEFAULT']
    return AuthConfig(
        auth_config_section.get('method'),
        auth_config_section.get('client_id'),
        auth_config_section.get('client_secret'),
        auth_config_section.get('tenant_id'))
