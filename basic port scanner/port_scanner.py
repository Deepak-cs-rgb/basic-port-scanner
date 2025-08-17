import socket
from utils.services import common_ports

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            output = f"[+] Port {port} ({service}) is OPEN"
            print(output)
            save_result(output)
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def save_result(data):
    with open("results/scan_results.txt", "a") as file:
        file.write(data + "\n")

def main():
    print("=== Basic Port Scanner ===")
    target = input("Enter target IP/hostname: ")
    print(f"\nScanning target: {target}\n")
    for port in range(1, 1025):  # ports 1–1024
        scan_port(target, port)

if __name__ == "__main__":
    main()
