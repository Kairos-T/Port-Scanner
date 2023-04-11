import pyfiglet
import socket

def port_scanner(ip, start_port, end_port):
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

    for port in range(start_port, end_port+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")

if __name__ == "__main__":
    ip = "192.168.0.250"
    start_port = 1
    end_port = 9000
    port_scanner(ip, start_port, end_port)