from typing import TypedDict


class AutopilotDevice(TypedDict):
    """
    Represents a Device to be registered into Autopilot

    The following combinations of properties are required at a minimum for each device:
        hardwareHash + productKey.
        hardwareHash + SerialNumber.
        hardwareHash + productKey + serialNumber.
        hardwareHash only.
        productKey only.
        serialNumber + oemManufacturerName + modelName.
    """
    hardwareHash: str
    productKey: str
    serialNumber: str
    modelName: str
    oemManufacturerName: str
