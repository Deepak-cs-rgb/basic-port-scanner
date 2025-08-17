import socket
from concurrent.futures import ThreadPoolExecutor
from utils.services import common_ports   # <-- reuse your services.py mapping

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # shorter timeout for speed
        result = sock.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            print(f"[+] Port {port} ({service}) is OPEN")
        sock.close()
    except Exception:
        pass

def main():
    print("=== Threaded Port Scanner ===")
    target = input("Enter target IP/hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    # Run up to 100 threads at once
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: scan_port(target, port), range(start_port, end_port + 1))

    print("\nScan complete.")

if __name__ == "__main__":
    main()
