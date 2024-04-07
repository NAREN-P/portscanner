# PortScanner

PortScanner is a Python tool designed for scanning ports to identify which ones are open on a target system. It includes two Python scripts:

- `portscanner.py`: This script displays the available ports on a target system.
- `portsanadv.py`: This script provides more detailed information, including the protocol, service, and open status of the ports.

## Usage

To use the PortScanner tool, follow the format below:

```bash
python portscanner.py <target_address> -r <start_port> <end_port> -t <num_threads>
```

&nbsp;

Replace `<target_address>` with the IP address or hostname of the target system, `<start_port>` and `<end_port>` with the range of ports to scan, and `<num_threads>` with the desired number of threads for parallel scanning.

## Notes

- Threading consumes more CPU usage, so ensure your system can handle it.
- The accuracy of port scanning results may vary depending on network conditions and target configurations.

## File Descriptions

- `portscanner.py`: Displays the available ports on a target system.
- `portsanadv.py`: Provides more detailed information, including the protocol, service, and open status of the ports.

## Example Usage

Here are examples of how to use both scripts:

python portscanner.py 192.168.1.100 -r 1 100 -t 10  
python portsanadv.py 192.168.1.100 -r 1 100 -t 10
