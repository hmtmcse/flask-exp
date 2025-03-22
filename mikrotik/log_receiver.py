import socket
import re


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


def start_syslog_listener():
    # Create a socket to listen for syslog messages
    syslog_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    syslog_socket.bind(('0.0.0.0', 514))  # Bind to all interfaces on port 514

    print("Listening for syslog messages on port 514...")

    try:
        while True:
            message, address = syslog_socket.recvfrom(1024)  # Buffer size
            syslog_message = message.decode()
            print(f"{address}: {syslog_message}")

    except KeyboardInterrupt:
        print("\nListener stopped.")
    finally:
        syslog_socket.close()


if __name__ == "__main__":
    start_syslog_listener()
