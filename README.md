# Port-Scanner (Updated Version)

Updates:
1. Use of function 'port_scanner' for organisation
2. Formatting with f-strings for conciseness
3. 'With' used to ensure that socket is properly closed (even if exceptions occur)
4. Timeout of 0.5s - preventing program from hanging on unresponsive ports
5. __name__ to ensure port_scanner function is only executed when the code is run as a script, not when it is imported as a module


IP address 192.168.0.250 is a private IP address used for local networks
- (192.168.0) represents the network
- (250) represents the specific device on the network

- Used to specify IP address of targetted device to be scanned for open ports
