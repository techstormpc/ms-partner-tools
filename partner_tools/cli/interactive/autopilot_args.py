from partner_tools.cli.interactive.question_wrapper import ask, QuestionType
from partner_tools.config import load_device_options
from partner_tools.models.autopilot_device import CommonDevice


def get_serial_number() -> str:
    return ask(QuestionType.text,
               "Please enter the serial number:",
               required=True)


def get_device() -> CommonDevice:
    common_devices = load_device_options()
    options = [f'{device.model} - {device.manufacturer}' for device in common_devices]

    resp = ask(QuestionType.select,
               "Please select a device type:",
               choices=options)

    device = [x for x in common_devices if f'{x.model} - {x.manufacturer}' == resp][0]
    return device
