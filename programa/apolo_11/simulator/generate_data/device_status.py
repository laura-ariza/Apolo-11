import random


def generate_device_status() -> str:

    # list of device status
    opcion_status: list[str] = ["excellent", "good", "warning", "faulty", "killed", "unknown"]

    # device status randomization
    device_status: str = random.choice(opcion_status)
    return device_status
