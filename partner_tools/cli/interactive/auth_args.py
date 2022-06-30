import questionary

from partner_tools.config import AuthConfig


def gather_login():
    client_id = questionary.text("Please enter the client ID").ask()
    client_secret = questionary.text("Please enter the client secret").ask()
    tenant_id = questionary.text("Please enter the tenant ID").ask()

    return AuthConfig(client_id=client_id,
                      client_secret=client_secret,
                      tenant_id=tenant_id)
