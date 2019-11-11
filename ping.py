"""
Created on Tuesday, October 29, 2019 18:38:47 IST

@author: Saurabh Ghanekar
"""

import os
import platform


def ping(hostname, iterations):

    if platform.system() == "Windows":
        response = os.system("ping "+hostname+" -n " + iterations)
    else:
        response = os.system("ping -c " + iterations + " " + hostname)

    return response

iterations = "10"
ping("google.com", iterations)

