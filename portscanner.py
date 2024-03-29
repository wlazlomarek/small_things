#!/usr/bin/python3
import socket
import sys
import os

port_list = []

def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on a given IP address """

    print('[*] Starting TCP port scan on host %s\n' % ip)

    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)

    print('\n[+] TCP scan on host %s complete' % ip)
    print(f'[+] Open ports: {port_list}')


def scanRange(network, startPort, endPort):
    """ Starts a TCP scan on a given IP address range """

    print('[*] Starting TCP port scan on network %s.0\n' % network)

    # Iterate over a range of host IP addresses and scan each target
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(network, startPort, endPort)

    print('\n[+] TCP scan on network %s.0 complete' % network)
    print(f'[+] Open ports: {port_list}')


def banner(tcp,ip, port):
    try:
        return tcp.recv(1024).decode("UTF-8")
    except Exception:
        pass


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """
    
    for port in range(startPort, endPort + 1):
        sys.stdout.write('\r[*] Current port number: ' + str(port))

        try:
            # Create a new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Print if the port is open
            if not tcp.connect_ex((ip, port)):
                print(f' -> {ip}:{port}/TCP Open | Service name:', banner(tcp, ip, port))
                port_list.append(port)
                tcp.close()
                
        except Exception:
            pass
            

if __name__ == '__main__':
    # Timeout in seconds
    socket.setdefaulttimeout(0.05)

    if len(sys.argv) < 4:
        print('Usage: ./portscanner.py <IP address> <start port> <end port>')
        print('Example: ./portscanner.py 192.168.1.10 1 65535\n')
        print('Usage: ./portscanner.py <network> <start port> <end port> -n')
        print('Example: ./portscanner.py 192.168.1 1 65535 -n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:
        scanRange(network, startPort, endPort)
