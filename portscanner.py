import argparse
import socket
import concurrent.futures

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                return port
    except Exception:
        pass
    return None

def scan_ports(target, start_port, end_port, num_threads=10):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_port = {executor.submit(scan_port, target, port): port for port in range(start_port, end_port + 1)}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Basic Port Scanner Tool")
    parser.add_argument("target", help="Target IP address to scan")
    parser.add_argument("-r", "--range", metavar=("START", "END"), type=int, nargs=2, required=True, help="Port range to scan (start and end)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads for parallel scanning")
    args = parser.parse_args()

    start_port, end_port = args.range
    open_ports = scan_ports(args.target, start_port, end_port, args.threads)

    print("\nOpen ports:")
    for port in open_ports:
        print(port)

if __name__ == "__main__":
    main()
