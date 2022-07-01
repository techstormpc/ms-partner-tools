from azure.identity import DeviceCodeCredential

from partner_tools.auth.auth_info import AuthInfo, SCOPES


class DeviceCode(AuthInfo):
    """
    Implements the Device code flow for the Microsoft login endpoint
    https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code
    """
    def __init__(self, client_id: str, client_secret: str, tenant_id: str):
        super().__init__()
        self.credential = DeviceCodeCredential(
            client_id=client_id,
            client_secret=client_secret,
            disable_automatic_authentication=True,
            tenant_id=tenant_id,
            **self._get_cache_args()
        )
        record = self.credential.authenticate(scopes=SCOPES)
        self._cache_auth_record(record)

    def _get_token(self):
        return self.credential.get_token(SCOPES[0]).token
