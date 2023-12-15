# Network Scanning Tool

This Network Scanning Tool is a Python-based utility for network analysis and port scanning. It leverages the Scapy library and standard socket programming to provide various network scanning features.

## Features

- **Set Default Interface:** Automatically selects a common network interface (Ethernet, Wi-Fi, etc.) for network operations.
- **TCP Port Scan:** Allows scanning of TCP ports on a target host to determine their status (Open, Closed, Filtered).
- **UDP Port Scan:** Facilitates scanning of UDP ports on a target host, identifying if ports are Open, Closed, or Filtered.
- **Banner Grabbing:** Retrieves banners from open ports to identify service information, supporting both TCP and UDP protocols.

## Usage

The tool provides the following functions:

- `set_default_interface()`: Sets the default network interface for scanning.
- `single_tcp_scan(target, port)`: Performs a TCP scan on a single port of the target host.
- `single_udp_scan(target, port)`: Conducts a UDP scan on a specified port of the target host.
- `grab_banner(target, port, protocol)`: Grabs the banner from the specified port (TCP/UDP) of the target host.

## Dependencies

- Python 3.7+
- Scapy
- Socket

To install Scapy, run:


## Example

```python
# Set the default network interface
set_default_interface()

# Perform a TCP scan on port 80 of example.com
tcp_result = single_tcp_scan("example.com", 80)
print("TCP Port 80:", tcp_result)

# Perform a UDP scan on port 53 of example.com
udp_result = single_udp_scan("example.com", 53)
print("UDP Port 53:", udp_result)

# Grab a banner from port 22 (SSH) of example.com
banner = grab_banner("example.com", 22)
print("Banner from Port 22:", banner)



Disclaimer

This tool is for educational and ethical testing purposes only. Unauthorized scanning and banner grabbing on networks or servers without explicit permission is illegal and unethical.