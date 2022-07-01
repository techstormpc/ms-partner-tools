from typing import NamedTuple


class CommonDevice(NamedTuple):
    manufacturer: str
    model: str


# TODO: These settings should be loaded from a config file
COMMON_DEVICES = [
    CommonDevice("Microsoft Corporation", "Surface Laptop 4"),
    CommonDevice("Dell Inc.", "Latitude 3420"),
    CommonDevice("Dell Inc.", "Latitude 3520")
]
