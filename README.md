# Network Subnet Scanner Tool

This tool scans a network subnet for active devices and services such as open ports commonly used by web servers, IP cameras, and IoT devices.

## Features

* Auto-detects your local network interface and IP address
* Scans the entire subnet for active hosts
* Identifies open ports such as 80, 554, 8000, 8080
* Detects potential RTSP streams and camera dashboards
* Fast or stealth scanning modes
* Optionally uses proxychains for anonymous scanning
* Verbose output and optional filtering

## Usage

```bash
sudo python3 scanner.py
```

Follow the on-screen prompts to:

* Detect your subnet
* Choose scanning mode
* Enable optional verbose output
* View device types and ports

## Requirements

* Python 3
* Modules:

  * `nmap`
  * `netifaces`
  * `mac_vendor_lookup`
* Nmap installed and accessible via command line

Install Python modules:

```bash
pip install python-nmap netifaces mac-vendor-lookup
```

Make sure you also have Nmap installed:

```bash
sudo dnf install nmap    # Fedora
sudo apt install nmap    # Debian/Ubuntu
```

## Disclaimer

This tool is intended **only for educational purposes and ethical testing** on networks you own or have explicit permission to analyze.

> **Unauthorized scanning or spoofing on networks you don't control is illegal.**

Use responsibly.

## License

MIT License
