import ipaddress


def filter_ipv4(ip):
    """Validate IP address from YAML variables."""
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        return "!!! Not valid ip address !!!"
