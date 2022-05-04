#Python 
#Author:  Wayne Michael AC9HP 
import socket
import sys
import requests
import pytz
import time

from datetime import datetime


if len(sys.argv)<3:
	print("Arguments request are APIKEY CALLSIGN PATH_TO_ALL.TXT") # give information about required parameters
	sys.exit(0)  #End gracefully

# Parameters APIKEY CALLSIGN  PATH {wsjtx all.txt}
while True:
	with open(sys.argv[3],"r") as f: 
		last_line = f.readlines()[-1]

	if last_line.__contains__(sys.argv[2]): #Does the last line contain the call sign?

		line = last_line.split()
		if line[8] == sys.argv[2]: #Make sure the call sign is in the right place 
			if line[7] == "CQ": #Make sure the line is a call for CQ
				freq = line[1].replace('.','') #remove the period for proper frequency
				freq = freq + "000" # Add three zeros to send frequency in hertz 
				print( sys.argv[2] + " is on " + freq + " at " + line[0])
				dt = datetime.strptime(line[0],'%y%m%d_%H%M%S'); #Convert the time into a date variable
				a = datetime.now(pytz.utc) #Get the current time in UTC
				c = a-dt.replace(tzinfo=pytz.utc) # Calculate the differece in time
				m = c.seconds / 60  #Convert the seconds to minutes
				if (m<2): #Only update the frequency if the date/time is newer than 2 minutes
                    #Send the request to QRZCQ website
					r = requests.post('https://ssl.qrzcq.com/api/rig/put',json={"auth":{"call":sys.argv[2],"key":sys.argv[1]},"request":{"freq":freq,"mode":line[3],"smeter":"48"}})
					print("update complete: " + str(r.status_code)) #Show the status code
	time.sleep(240) #Sleep for 4 minutes before looping back to the WHILE
