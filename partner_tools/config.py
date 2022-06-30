import configparser
import os
from pathlib import Path
from typing import NamedTuple

CONFIG_LOCATION = "~/.ms-partner-tools/config"


class AuthConfig(NamedTuple):
    client_id: str
    client_secret: str
    tenant_id: str


def get_config_path() -> Path:
    config_location = os.environ.get('PARTNER_TOOLS_CONFIG', CONFIG_LOCATION)
    return Path(config_location).expanduser()


def save_config(auth_config: AuthConfig):
    ini_config = configparser.SafeConfigParser()
    ini_config['DEFAULT'] = auth_config._asdict()
    config_path = get_config_path()
    config_path.parent.mkdir(exist_ok=True)
    with config_path.open('w') as configfile:
        ini_config.write(configfile)


def load_config() -> AuthConfig:
    config_path = get_config_path()
    if not config_path.exists():
        raise RuntimeError('Please configure authentication by running partnertools-cli configure')
    ini_config = configparser.ConfigParser()
    ini_config.read(str(config_path.absolute()))
    auth_config = ini_config['DEFAULT']
    return AuthConfig(auth_config['client_id'],
                      auth_config['client_secret'],
                      auth_config['tenant_id'])
