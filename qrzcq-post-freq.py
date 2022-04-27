# Written by Wayne Michael 
# AC9HP 

import requests
import sys

#command line parameters need to be call key mode freq smeter 

if len(sys.argv)<=1:
	print("command line parameters: call key mode freq smeter")
	sys.exit()

response = requests.post('https://ssl.qrzcq.com/api/rig/put', json={"auth":{"call":sys.argv[1],"key":sys.argv[2]},"request":{"mode":sys.argv[3],"freq":sys.argv[4],"smeter":sys.argv[5]}})

if response.status == 0:
	print(response.json())
	quit()
print("command line parameters: call key mode freq smeter")