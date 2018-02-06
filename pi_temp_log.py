#!/usr/bin/env python3

"""
Measures linux system cpu temp and logs in csv every 60 secs
"""

import os
import sys
import time

__author__ = "Nick Everett"
__version__ = "0.5.0"
__license__ = "GNU GPLv3"


def check_os():
    platform_dict = {'darwin': 'MacOS',
                     'freebsd': 'FreeBSD',
                     'linux': 'Linux',
                     'win32': 'Windows',
                     'win64': 'Windows',}
    platform = sys.platform
    if platform.startswith('linux'):
        return True
    else:
        if platform in platform_dict:
            print('detected: {} - unsupported platform'.format(platform_dict[platform]))
        else:
            print('unknown platform detected: {}'.format(platform))
        sys.exit('exiting...')


def measure_temp():  # Returns temp reading from pi terminal / bash
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp[5:9]  # returns only temp characters TODO find more efficient process


def update_temp_log(value):  # appends log file with time and temp value
    log = open("~/temp_log.csv", "a+")
    log_date = time.strftime("%Y-%m-%d", time.gmtime())
    log_time = time.strftime("%H:%M:%S", time.gmtime())
    log.write("{},{},{}\n".format(log_date, log_time, value))
    log.close()


while True:  # Measures temp every 60secs
    linux_platform = check_os()
    temp = measure_temp()
    update_temp_log(temp)
    time.sleep(60)

