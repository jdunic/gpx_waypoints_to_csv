#!/usr/bin/python

"""GPX_to_csv_waypoints.py: Exporting waypoints in GPX file to a csv file"""

# Author: Jillian Dunic
# Date created: 2014-08-13

# Change log #

# Date modified:




###########
## Data Loading and Cleaning
###########
#Load the data from Google Docs

#Extract GPX file data into csv

# Load libraries
import os

import gpxpy
import gpxpy.gpx

import csv
import time
from datetime import date

files = os.listdir

for f in os.listdir('/Users/jillian/Desktop/gps_conversion_py_work/GPS2_downloads/2015_JULY_16'):
    gpx_to_csv(output_name = f + '.csv')

os.chdir('/Users/jillian/Desktop/gps_conversion_py_work/GPS2_downloads/2015_JULY_16')

for f in os.listdir(os.getcwd()):
    gpx_to_csv(output_name = f + '.csv', gpx_filename = f)


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






'GPS2_downloads/2015_JULY_16/Waypoints_06-AUG-14.gpx'


#6.28.8.1 Basic example - log to a file

# Here's a simple logging example that just logs to a file. In order, it creates a Logger instance, then a FileHandler and a Formatter. It attaches the Formatter to the FileHandler, then the FileHandler to the Logger. Finally, it sets a debug level for the logger.

"""
import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/tmp/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
We can use this logger object now to write entries to the log file:

logger.error('We have a problem')
logger.info('While this is just chatty')
If we look in the file that was created, we'll see something like this:

2003-07-08 16:49:45,896 ERROR We have a problem
The info message was not written to the file - we called the setLevel method to say we only wanted WARNING or worse, so the info message is discarded.

The timestamp is of the form ``year-month-day hour:minutes:seconds,milliseconds.'' Note that despite the three digits of precision in the milliseconds field, not all systems provide time with this much precision.
"""