import nmap
import netifaces
import time

def get_local_subnet():
    try:
        # Get the default network interface
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
        ip = ip_info['addr']
        netmask = ip_info['netmask']

        # Convert netmask to CIDR format
        mask_parts = netmask.split('.')
        cidr = sum([bin(int(part)).count('1') for part in mask_parts])
        subnet = f"{ip}/{cidr}"
        return subnet
    except Exception as e:
        print(f"[-] Failed to get subnet: {e}")
        return None

def scan_for_cameras(subnet):
    print(f"[+] Scanning subnet: {subnet}")
    time.sleep(2)
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments='-p 80,554,8000,8080 --open')

    for host in scanner.all_hosts():
        print(f"\n[+] Host found: {host}")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"    [!] Open port: {port}")
                if port == 554:
                    print(f"    🔍 Might be RTSP stream: rtsp://{host}:554")
                if port in [80, 8000, 8080]:
                    print(f"    🌐 Try in browser: http://{host}:{port}")

if __name__ == "__main__":
    try:
        subnet = get_local_subnet()
        if subnet:
            scan_for_cameras(subnet)
        else:
            print("[-] Could not detect local subnet.")
    except Exception as e:
        print(f"[-] Error: {e}")

