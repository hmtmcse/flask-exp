import re

input_string = "('10.0.12.1', 34994): firewall,info forward: in:Rapid Net out:SRV_OFS_Bridge, proto TCP (SYN), 45.58.159.222:37340->10.0.12.22:443, NAT 45.58.159.222:37340->(103.145.208.134:443->10.0.12.22:443), len 44"

# Regular expression to match the IP and port
pattern = r"\('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', (\d+)\)"

# Perform regex search
match = re.search(pattern, input_string)

# Extract IP address and port if match found
if match:
    ip_address = match.group(1)
    port = match.group(2)
    print("IP Address:", ip_address)
    print("Port:", port)
else:
    print("No match found")
