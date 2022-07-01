from azure.identity import InteractiveBrowserCredential

from partner_tools.auth import AuthInfo
from partner_tools.auth.auth_info import SCOPES


class Interactive(AuthInfo):
    """
    Implements the authorization code flow (PKCE) for the Microsoft login endpoint
    https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
    """
    def __init__(self, client_id: str, tenant_id: str):
        super().__init__()
        self.credential = InteractiveBrowserCredential(
            client_id=client_id,
            disable_automatic_authentication=True,
            tenant_id=tenant_id,
            **self._get_cache_args()
        )
        record = self.credential.authenticate(scopes=SCOPES)
        self._cache_auth_record(record)

    def _get_token(self):
        return self.credential.get_token(SCOPES[0]).token
