import socket

def port_scan(target):
    common_ports = [21, 22, 25, 53, 80, 443, 8080]
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports
