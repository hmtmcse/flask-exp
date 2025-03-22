import re
variable = "firewall,info forward: in:ether5_EXT out:Rapid Net, src-mac 2c:c8:1b:f4:85:e4, proto TCP (ACK,FIN), 10.0.15.100:57916->142.250.194.234:443, NAT (10.0.15.100:57916->103.145.208.134:57916)->142.250.194.234:443, len 52"

def data_parse_1(syslog_message):
    pattern = re.compile(
        r"in:(?P<in>\S+) out:(?P<out>[^,]+), src-mac (?P<src_mac>[0-9a-f:]+), .* (?P<src_ip>\d+\.\d+\.\d+\.\d+):(?P<src_port>\d+)->(?P<dst_ip>\d+\.\d+\.\d+\.\d+):(?P<dst_port>\d+)"
    )

    match = pattern.search(syslog_message)

    if match:
        parsed_data = match.groupdict()
        print(parsed_data)
    else:
        print("No match found")


def parse_nat_data(log):
    pattern = re.compile(
        r"in:(?P<in>\S+) out:(?P<out>[^,]+), src-mac (?P<src_mac>[0-9a-f:]+), "
        r"proto (?P<proto>\S+(?: \([^)]+\))?), (?P<src_ip>\d+\.\d+\.\d+\.\d+):(?P<src_port>\d+)->"
        r"(?P<dst_ip>\d+\.\d+\.\d+\.\d+):(?P<dst_port>\d+), "
        r"NAT \((?P<nat_src_ip>\d+\.\d+\.\d+\.\d+):(?P<nat_src_port>\d+)->"
        r"(?P<nat_dst_ip>\d+\.\d+\.\d+\.\d+):(?P<nat_dst_port>\d+)\)->"
        r"(?P<final_dst_ip>\d+\.\d+\.\d+\.\d+):(?P<final_dst_port>\d+)"
    )

    match = pattern.search(log)

    if match:
        parsed_data = match.groupdict()
        print(parsed_data)
    else:
        print("No match found")


def incoming_log():
    log = "firewall,info forward: in:Rapid Net out:SRV_OFS_Bridge, proto TCP (SYN), 45.58.159.222:37340->10.0.12.22:443, NAT 45.58.159.222:37340->(103.145.208.134:443->10.0.12.22:443), len 44"

    pattern = re.compile(
        r"in:(?P<in>\S+) out:(?P<out>[^,]+), "
        r"proto (?P<proto>\S+(?: \([^)]+\))?), "
        r"(?P<src_ip>\d+\.\d+\.\d+\.\d+):(?P<src_port>\d+)->"
        r"(?P<dst_ip>\d+\.\d+\.\d+\.\d+):(?P<dst_port>\d+), "
        r"NAT (?P<nat_src_ip>\d+\.\d+\.\d+\.\d+):(?P<nat_src_port>\d+)->"
        r"\((?P<nat_dst_ip>\d+\.\d+\.\d+\.\d+):(?P<nat_dst_port>\d+)->"
        r"(?P<final_dst_ip>\d+\.\d+\.\d+\.\d+):(?P<final_dst_port>\d+)\)"
    )

    match = pattern.search(log)

    if match:
        parsed_data = match.groupdict()
        print(parsed_data)
    else:
        print("No match found")

# data_parse_1(variable)

log = "firewall,info forward: in:ether5_EXT out:Rapid Net, src-mac 2c:c8:1b:f4:85:e4, proto TCP (ACK,FIN), 10.0.15.100:57916->142.250.194.234:443, NAT (10.0.15.100:57916->103.145.208.134:57916)->142.250.194.234:443, len 52"
# parse_nat_data(log)

log2 = "firewall,info forward: in:Rapid Net out:SRV_OFS_Bridge, proto TCP (SYN), 45.58.159.222:37340->10.0.12.22:443, NAT 45.58.159.222:37340->(103.145.208.134:443->10.0.12.22:443), len 44"
incoming_log()
