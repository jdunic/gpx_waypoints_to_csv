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
import distutils.core
import os

import gpxpy

import csv
import time
from datetime import date

# Get input and output file names and locations
def get_input_data():
    # User prompts and confirmation that information entered is correct. In case of an error, type 'exit' to escape.
    print('Type "exit" to escape')
    username = raw_input("Enter your name: ")
    username = username.rstrip()
#
    if username == 'exit':
        return None
    gpx_filename = raw_input("Enter the gpx file path: ")
    gpx_filename = gpx_filename.replace('\\', '')
    gpx_filename = gpx_filename.strip()
#    
    assert os.path.exists(gpx_filename), "I did not find the file at, " + str(gpx_filename)
#
    if gpx_filename == 'exit':
        return None
#
    output_filename = raw_input("Enter the output file path; e.g., PATH/filename1.csv: ")
    output_filename = output_filename.replace('\\', '')
    output_filename = output_filename.replace('\'', '')
    gpx_filename = gpx_filename.strip()
#
    if output_filename == 'exit':
        return None
#   
    # Print confirmation message
    print("Your name is:", username, "Your input file path is:", gpx_filename, "and your output file path", output_filename)
    confirmation = raw_input("Is this information correct? If no, you will be able to re-enter this information. (y/n) ")
    go_ahead = distutils.util.strtobool(confirmation)
#
    names = ('username', 'gpx_filename', 'output_filename', 'confirmation')
    inputs = (username, gpx_filename, output_filename, confirmation)
    info_dict = dict(zip(names, inputs))
#
    return(info_dict)

def gpx_to_csv(output_name, gpx_filenames):
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
    #return(wp_list)

    keys = wp_list[0].keys()
    with open(output_name, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(wp_list)


# For a single file
input_data = get_input_data()

gpx_to_csv(output_name = input_data['output_filename'], 
           gpx_filenames = input_data['gpx_filename'])