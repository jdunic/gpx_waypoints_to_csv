#!/usr/bin/python

"""GPX_to_csv_waypoints.py: Exporting waypoints in GPX file to a csv file"""

# Author: Jillian Dunic
# Date created: 2014-08-13

###########
## Data Loading and Cleaning
###########
#Load the data from Google Docs

#Extract GPX file data into csv

# Load libraries
import gpxpy

import csv
import time
from datetime import date

def gpx_to_csv(output_name, gpx_filenames = None):
    if isinstance(gpx_filenames, list) is False:
        gpx_filenames = [gpx_filenames] 
    wp_list = []
    for filename in gpx_filenames:
        print(filename)
        gpx_file = open(filename, 'r')
        gpx = gpxpy.parse(gpx_file)
        for w in gpx.waypoints:
            wp_dict = {
                'waypoint': w.name, 
                'lat': w.latitude,
                'long': w.longitude,
                'date': w.time.strftime("%Y-%m-%d"),
                'time': w.time.strftime("%H:%M:%S")
            }
            wp_list.append(wp_dict)
    return(wp_list)

    keys = wp_list[0].keys()
    with open(output_name, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(wp_list)

