import socket
import sys

def scan_port(target, port):
    """Checks if a port is open on the target."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

def main():
    """Gets user input and scans the specified ports."""
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target> <start_port> <end_port>")
        sys.exit(1)
    
    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print(f"Scanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("\nScan complete!")

if __name__ == "__main__":
    main()
