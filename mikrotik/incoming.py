import re

log_entry = """firewall,info forward: in:Rapid Net out:SRV_OFS_Bridge, proto TCP (SYN), 45.58.159.222:37340->10.0.12.22:443, NAT 45.58.159.222:37340->(103.145.208.134:443->10.0.12.22:443), len 44"""

# Regular expression to extract values
pattern = re.compile(
    r"in:(?P<in>[\w\s]+) out:(?P<out>[\w\s]+), proto (?P<proto>\w+) "
    r".* (?P<src_ip>[\d\.]+):(?P<src_port>\d+)->(?P<dst_ip>[\d\.]+):(?P<dst_port>\d+), "
    r"NAT (?P<nat_src_ip>[\d\.]+):(?P<nat_src_port>\d+)->"
    r"\((?P<nat_dst_ip>[\d\.]+):(?P<nat_dst_port>\d+)->(?P<nat_final_ip>[\d\.]+):(?P<nat_final_port>\d+)\)"
)

match = pattern.search(log_entry)

if match:
    parsed_data = match.groupdict()
    print(parsed_data)
else:
    print("No match found")
