# https://docs.python.org/es/3/library/hashlib.html
# Hashlib:this module implements a common interface to many different secure hash and message digest algorithms.
import hashlib


def generate_hash(now_date, value_mission, device, device_status):
    # concatenate relevant data to generate the hash
    hash_data = f"{now_date}{value_mission}{device}{device_status}"
    # apply hash SHA-256 to concatenated data
    hash = hashlib.sha256(hash_data.encode()).hexdigest()
    return hash
