# Kent Pan
# PUI HW2 Part 1

# import packages
from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# check for number of arguments
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_kwp225.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# assigns arguments to variables
key = sys.argv[1]
line = sys.argv[2]

# pulls bus data from MTA API
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# navigates through JSON to specific bus activity
buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# loop through each each active bus and prints active bus locations
print('Bus Line:', line)
print('Number of Active Buses:', len(buses))
for i in range(len(buses)):
    print("Bus", buses[i]['MonitoredVehicleJourney']['VehicleRef'].lstrip('MTABC_'), "is at latitude", 
          buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], "and longitude", 
          buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
