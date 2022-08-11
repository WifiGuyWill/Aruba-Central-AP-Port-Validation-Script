# Aruba-Central-AP-Port-Validation-Script
Script to automate the validation of AP speed/duplex on all AP ports including uplink

Download the repo, make sure Python is installed.
Edit creds.py and enter the credentials for Aruba Central
Then execute the script 'python3 main.py'

The script will first generate a valid API key. It will then create a list of every active AP in Central. Lastly it will query the details of each AP and output the AP Name, Serail, Model, Port#, Speed and Duplex. This will be shown on the screen as the script executes, but will also be written to a file called 'ap_data.txt'.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com
