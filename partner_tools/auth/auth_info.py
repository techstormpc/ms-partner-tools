from abc import abstractmethod, ABC

from requests.auth import AuthBase


SCOPES = ['https://api.partnercenter.microsoft.com/user_impersonation']


class AuthInfo(ABC):
    """
    Represents an abstract class to provide a way to authorize requests
    """
    @abstractmethod
    def get_request_auth(self) -> AuthBase:
        """
        Auth for the requests library
        """
        raise NotImplementedError()
