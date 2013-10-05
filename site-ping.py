#!/usr/bin/python3
"""
Ping a Stack Exchange page using Firefox's cookies and see if we're logged in.
By: Brad Conte
"""

import urllib.request
import re
import logging
import os
import subprocess
from http.cookiejar import MozillaCookieJar


urls = [
    "http://crypto.stackexchange.com/users/593/b-con",
    "http://security.stackexchange.com/users/8857/b-con",
    "http://stackoverflow.com/users/1361836/b-con"
]

logging.basicConfig(filename="/tmp/site-ping.log", 
                   datefmt="%m-%d %H:%M",
                   level=logging.DEBUG)

# Extract the cookies from Firefox. The script to do so is co-located.
path = os.path.dirname(os.path.realpath(__file__))
p = subprocess.call(path + "/extract-cookies.sh")

# Load the cookies.
cj = MozillaCookieJar("/tmp/firefox-cookies.txt")
try:
    cj.load()
except FileNotFoundErr as ex:
    logging.error(ex)
    quit(1)

# Use the cookies to visit each of the URLs.
for url in urls:
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(url)
    
    html = response.read().decode("utf-8")
    response.close()
    
    # The "votes" tab only appears on the user profile when you're logged in.
    match = re.search("tab=votes", html)
    if match:
        log_line = "{} -> Succeeded".format(url)
        logging.info(log_line)
        print(log_line)
    else:
        log_line = "{} -> Failed".format(url)
        logging.error(log_line)
        print(log_line)

    
