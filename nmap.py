#! y=usr/bin/python3

import nmap

scanner = nmap.portScanner()

print('Welcome, to this a nmap automation tool')
print('<------------------------------------------------>')

ip_addr = input('Please enter the ip address you want to scan:')
print('the IP you entered is: ', ip_addr)

resp = input("""\n please enter the type of scan you want to run 
                           1) SYN ACK Scan 
                           2) UDP Scan 
                           3) Comprehensive Scan """)
print('you have selected option:', resp)

if resp == '1':
    print('Nmap Version:', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', 'v- sS')
    print(scanner.scaninfo())
    print('Ip Status:', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocolo())
    print('open Portis:', scanner[ip_addr]['tcp'].key())