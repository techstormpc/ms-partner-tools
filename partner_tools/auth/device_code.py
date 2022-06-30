from azure.identity import DeviceCodeCredential
from requests.auth import AuthBase

from partner_tools.auth.auth_info import AuthInfo, SCOPES


class DeviceCode(AuthInfo):
    """
    Implements the Device code flow for the Microsoft login endpoint
    https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code
    """
    def __init__(self, client_id: str, client_secret: str, tenant_id: str):
        self.credential = DeviceCodeCredential(
            client_id=client_id,
            client_secret=client_secret,
            disable_automatic_authentication=True,
            tenant_id=tenant_id
        )
        self.credential.authenticate(scopes=SCOPES)

    def get_request_auth(self) -> AuthBase:
        return self.RequestAuth(self._get_token())

    def _get_token(self):
        return self.credential.get_token(SCOPES[0]).token

    class RequestAuth(AuthBase):
        def __init__(self, token):
            self.token = token

        def __call__(self, request):
            request.headers['Authorization'] = f'Bearer {self.token}'
            return request
