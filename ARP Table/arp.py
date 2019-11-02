import csv

def get_arp_table():
    """
    Returns: ARP Table
    """
    with open("/proc/net/arp") as arpt:
        names = [
            'IP address', 'HW type', 'Flags', 'HW address', 'Mask', 'Device'
        ]

        reader = csv.DictReader(
            arpt, fieldnames=names, skipinitialspace=True, delimiter=' '
        )
        next(reader)
        
        return [block for block in reader]

print(get_arp_table())