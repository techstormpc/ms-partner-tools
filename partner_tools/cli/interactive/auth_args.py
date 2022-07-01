from partner_tools.auth import DeviceCode
from partner_tools.auth.interactive import Interactive
from partner_tools.cli.interactive.question_wrapper import ask, QuestionType
from partner_tools.config import AuthConfig


def gather_login():
    method = ask(QuestionType.select, "Please select the authentication method:",
                 choices=[DeviceCode.__name__,
                          Interactive.__name__])
    client_id = ask(QuestionType.text, "Please enter the client ID:")
    client_secret = ''
    if method is not Interactive.__name__:
        client_secret = ask(QuestionType.text, "Please enter the client secret:")
    tenant_id = ask(QuestionType.text, "Please enter the tenant ID (CSP):")

    return AuthConfig(
        method=method,
        client_id=client_id,
        client_secret=client_secret,
        tenant_id=tenant_id)
