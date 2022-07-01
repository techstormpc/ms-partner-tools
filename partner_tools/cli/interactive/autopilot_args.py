from partner_tools.cli.helpers.devices import CommonDevice, COMMON_DEVICES
from partner_tools.cli.interactive.question_wrapper import ask, QuestionType


def get_serial_number() -> str:
    return ask(QuestionType.text,
               "Please enter the serial number:",
               required=True)


def get_device() -> CommonDevice:
    options = [f'{device.model} - {device.manufacturer}' for device in COMMON_DEVICES]

    resp = ask(QuestionType.select,
               "Please select a device type:",
               choices=options)

    device = [x for x in COMMON_DEVICES if f'{x.model} - {x.manufacturer}' == resp][0]
    return device
