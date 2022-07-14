import pyfiglet
import socket

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

for port in range(1, 9000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("192.168.0.250", port))
    if result == 0:
        print("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")
    sock.close()