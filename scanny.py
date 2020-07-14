#!/usr/bin/python

import argparse
import ipaddress
import scapy.all as scapy


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                      help="specify target IP address and CIDR block, e.g. 192.168.0.1/24")
    options = parser.parse_args()

    # exit early if target not specified
    if not options.target:
        parser.error(
            "Please specify a target IP. Use --help for more information.")

    # check if target is a valid IP with CIDR block
    try:
        if ipaddress.ip_network(options.target, False):
            return options
    except ValueError:
        parser.error(
            "Please specify a valid IP. Use --help for more information.")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(
        arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []

    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC_address": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

    print(clients_list)


def print_result(results_list):
    if not results_list:
        print("No results found.")
    else:
        print("IP\t\t\tMAC Address\n-----------------------------------------")
        for client in results_list:
            print(client["IP"] + "\t\t" + client["MAC_address"])


options = get_arguments()

scan_result = scan(options.target)
print_result(scan_result)
