import configparser
import os
from pathlib import Path
from typing import NamedTuple

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
