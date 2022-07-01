from typing import Callable

import questionary
from questionary import Question


class QuestionType:
    text = questionary.text
    select = questionary.select


def ask(question_type: Callable[..., Question],
        message: str,
        **kwargs) -> str:
    """
    Wrapper for the questionary ask method
    Mainly to catch the keyboard interrupt case
    """
    if kwargs.get("default") is not None:
        kwargs["default"] = str(kwargs["default"])

    if kwargs.get("required"):
        del kwargs["required"]
        kwargs["validate"] = lambda val: len(val.strip()) > 0 or "This field is required"

    resp = question_type(message=message, **kwargs).ask()
    if resp is None:
        raise KeyboardInterrupt()

    return resp
