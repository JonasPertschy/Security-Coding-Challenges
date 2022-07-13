# Solution based on socket
# Read target and port from command line paramter

import socket
import sys

def port_scanner(ip, tcp_ports):
	
    for tcp_port in tcp_ports:
        print ("Connect to ",ip,tcp_port)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            s.connect((ip,int(tcp_port)))
            print (tcp_port, " is open")
        except:
	        s.close()

def main():
    if not len(sys.argv)>2:
        print("Usage: python3 "+sys.argv[0]+' ip port-range')
    else:
        ip = sys.argv[1]
        port = sys.argv[2]
        if '-' in port:
            port_scanner(ip,range(int(port.split('-')[0]),int(port.split('-')[1])+1))
        elif ',' in port:
            port_scanner(ip,port.split(','))
        else:
            port_scanner(ip,[port])
main()