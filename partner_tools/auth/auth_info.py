from abc import abstractmethod, ABC
from pathlib import Path
from typing import Optional

from azure.identity import AuthenticationRecord, TokenCachePersistenceOptions
from requests.auth import AuthBase

from partner_tools.config import get_config_directory

SCOPES = ['https://api.partnercenter.microsoft.com/user_impersonation']
TOKEN_FILE_NAME = '.token'


def _save_token(token: str):
    config_dir = get_config_directory()
    token_path = Path(config_dir, TOKEN_FILE_NAME)
    with token_path.open('w') as token_file:
        token_file.write(token)


def _load_token() -> Optional[str]:
    config_dir = get_config_directory()
    token_path = Path(config_dir, TOKEN_FILE_NAME)
    if not token_path.exists():
        return None
    with token_path.open() as token_file:
        return token_file.read()


class AuthInfo(ABC):
    """
    Represents an abstract class to provide a way to authorize requests
    """
    def __init__(self, enable_cache=True) -> None:
        self.enable_cache = enable_cache

    @abstractmethod
    def _get_token(self):
        raise NotImplementedError()

    def get_request_auth(self) -> AuthBase:
        return self.RequestAuth(self._get_token())

    def _get_cache_args(self):
        if not self.enable_cache:
            return {}

        cache_args = {
            'cache_persistence_options': TokenCachePersistenceOptions(name='partner-tools')
        }
        auth_record = _load_token()
        if auth_record:
            cache_args['authentication_record'] = AuthenticationRecord.deserialize(auth_record)
        return cache_args

    def _cache_auth_record(self, auth_record: AuthenticationRecord):
        if not self.enable_cache:
            return

        _save_token(auth_record.serialize())

    class RequestAuth(AuthBase):
        def __init__(self, token):
            self.token = token

        def __call__(self, request):
            request.headers['Authorization'] = f'Bearer {self.token}'
            return request
