# Aruba Central AP Port Validation Script
Script to automate the validation of AP speed/duplex on all AP ports including uplink

```
% python3 main.py
2022-08-10 23:02:52 - ARUBA_BASE - INFO - Loaded token from storage from file:
Office-AP 505H CNKBKSN0RQ Eth0 1000Mbps (Full Duplex)
Bedroom-AP 505H CNKBKSN0SC Eth0 1000Mbps (Full Duplex)
Bedroom-AP 505H CNKBKSN0SC Eth1 1000Mbps (Full Duplex)
Bedroom-AP 505H CNKBKSN0SC Eth2 1000Mbps (Full Duplex)
Bedroom-AP 505H CNKBKSN0SC Eth3 100Mbps (Full Duplex)
```

Download the repo, make sure Python is installed.
Edit creds.py and enter the credentials for Aruba Central.
Then execute the script 'python3 main.py'

The script will first generate a valid API key, then create a list of every active AP in Central. It will then query the details of each AP and output the AP Name, Serail, Model, Port#, Speed and Duplex. This will be shown on the screen as the script executes and written to a file called 'ap_data.txt'.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com