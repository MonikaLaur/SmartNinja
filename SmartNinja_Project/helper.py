import json
import urllib

def get_address_from_ip(ip_address):
    base_uri = "http://freegeoip.net/json/"
    result = urllib.urlopen(base_uri+ip_address)
    data = json.loads(result)
    return data

if __name__ == '__main__':
    ip_address = "80.110.114.199"
    address_info = get_address_from_ip(ip_address)
    print address_info