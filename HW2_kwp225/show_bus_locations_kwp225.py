# Author: Kent Pan
##############################
# Code written to fill in later
##############################
# describe how code functions
# fill in later

from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_kwp225.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

key = sys.argv[1]
line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print('Bus Line:', line)
print('Number of Active Buses:', len(buses))
for i in range(len(buses)):
    print("Bus", buses[i]['MonitoredVehicleJourney']['VehicleRef'].lstrip('MTABC_'), "is at latitude", 
          buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], "and longitude", 
          buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
