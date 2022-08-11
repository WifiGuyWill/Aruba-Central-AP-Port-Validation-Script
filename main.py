#!/usr/bin/python3
#(c) 2022 Will Smith

#First populate creds.py with Central info + API keys
#Uncomment ap_details_eth0_only if you want stats only on Eth0
#Otherwise run this script to generate a list of all active APs and the port speed/duplex for each active port
#Output will be shown on the screen and a file called ap_data.txt is also generated

from pycentral.base import ArubaCentralBase
import creds as creds
#import os

central_info = creds.central_info
central_info = central_info = creds.central_info
central = ArubaCentralBase(central_info=central_info, ssl_verify=True)

#This function will generate a list of the serial numbers for all active APs
def inventory():
    offset = 0
    f = open("temp/serial.txt", "w")
    while True:
        inventory_response = central.command(apiMethod="GET", apiPath="/monitoring/v2/aps", apiParams={"limit": 1000, "offset": offset})
        for aps in inventory_response["aps"]:
            f.write(aps["serial"] + "\n")
        offset = offset + 1000
        if int(inventory_response['count']) == 0:
            break

#Use this function if you want stats on only Eth0
def ap_details_eth0_only():
    ap_data = open("ap_data.txt", "w")
    with open('temp/serial.txt') as f:
        for line in f:
            serial = line.strip()
            ap_details_response = central.command(apiMethod="GET", apiPath="/monitoring/v1/aps/" + serial)
            ap_name = ap_details_response["name"]
            ap_model = ap_details_response["model"]
            eth_speed = ap_details_response["ethernets"]
            for eth in eth_speed:
                if eth["index"] == "0":
                    print(ap_name + " " + ap_model + " " + serial + " " + "Eth" + (eth["index"]) + " " + (eth["link_speed"]) + " " + (eth["duplex_mode"]))                    
                    ap_data.write(ap_name + " " + ap_model + " " + serial + " " + "Eth" + (eth["index"]) + " " + (eth["link_speed"]) + " " + (eth["duplex_mode"]) + "\n")
#    os.remove("/temp/serial.txt")

#Use this function for stats on all AP ports
def ap_details_all():
    ap_data = open("ap_data.txt", "w")
    with open('temp/serial.txt') as f:
        for line in f:
            serial = line.strip()
            ap_details_response = central.command(apiMethod="GET", apiPath="/monitoring/v1/aps/" + serial)
            ap_name = ap_details_response["name"]
            ap_model = ap_details_response["model"]
            eth_speed = ap_details_response["ethernets"]
            for eth in eth_speed:
                if eth["status"] == "Up":
                    print(ap_name + " " + serial + " " + ap_model + " " + "Eth" + (eth["index"]) + " " + (eth["link_speed"]) + " " + (eth["duplex_mode"]))                    
                    ap_data.write(ap_name + " " + serial + " " + ap_model + " " + "Eth" + (eth["index"]) + " " + (eth["link_speed"]) + " " + (eth["duplex_mode"]) + "\n")
#    os.remove("temp/serial.txt")

if __name__ == "__main__":
    print("--- Starting ---")
    inventory()
#    ap_details_eth0_only()
    ap_details_all()
    print("--- Finished ---")
    print("NOTE: Output saved to ap_data.txt")
