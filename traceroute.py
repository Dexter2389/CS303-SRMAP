"""
Created on Monday, November 04, 2019 12:00:46 IST

@author: Saurabh Ghanekar
"""

import sys
import socket

def traceroute(dest_addr, max_hops=30, timeout=0.2):
    proto_icmp = socket.getprotobyname('icmp')
    proto_udp = socket.getprotobyname('udp')
    port = 33434

    for ttl in range(1, max_hops+1):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        rx.bind(('', port))
        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto(''.encode(), (dest_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = None
        finally:
            rx.close()
            tx.close()

        yield curr_addr

        if curr_addr == dest_addr:
            break

if __name__ == "__main__":
    dest_name = "www.google.com"
    dest_addr = socket.gethostbyname(dest_name)
    print(type(dest_addr))
    print("traceroute to %s (%s)" % (dest_name, dest_addr))
    for i, v in enumerate(traceroute(dest_addr)):
        print("%d\t%s" % (i+1, v))
