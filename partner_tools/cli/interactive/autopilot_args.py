import questionary

from partner_tools.cli.helpers.devices import CommonDevice, COMMON_DEVICES


def get_serial_number() -> str:
    return questionary.text(
        "Please enter the serial number"
    ).ask()


def get_device() -> CommonDevice:
    options = [f'{device.model} - {device.manufacturer}' for device in COMMON_DEVICES]
    resp = questionary.select(
        "Please select a device type",
        choices=options
    ).ask()

    device = [x for x in COMMON_DEVICES if f'{x.model} - {x.manufacturer}' == resp][0]
    return device
