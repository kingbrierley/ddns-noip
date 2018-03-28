# Imports | ensure you have these libraries | tested on Vanilla Ubuntu all good
import urllib2
import requests
import sys
import syslog
import os
import datetime
import argparse

# Parser | Non required | Use ARGS or further down edit the script Vars
parser = argparse.ArgumentParser(description='Script to update No-IP account with  WAN IP automatically or pass a manual IP')
parser.add_argument('-i','--ipaddress', help='Manual IP to provide',required=False)
parser.add_argument('-host','--hostname',help='Hostname to Parse', required=False)
parser.add_argument('-u','--username',help='Username to parse',required=False)
parser.add_argument('-p','--password',help='Password to parse', required=False)
args = parser.parse_args()

# Login | Used for Auth | Required or parsed
_USERNAME_ = args.username or "YOUREMAIL@YOURDOMAIN.com"
_PASSWORD_ = args.password or "YOURPASSWORD"
_HOST_ = args.hostname or "YOURHOSTNAME.ddns.net"

# Get current WAN IP | At Some point provider may be down | look for alternative if that happens
wanip = args.ipaddress or urllib2.urlopen("http://api.enlightns.com/tools/whatismyip/?format=text").read().strip()

# Update No-IP Hostname | Print status codes | Remove if need be
updateddns = requests.get("http://dynupdate.no-ip.com/nic/update?hostname=" + str(_HOST_), auth=(_USERNAME_, _PASSWORD_))
# Testing | Used for showing response codes | leave commented for now
#print updateddns.status_code
#print updateddns.content

# Not HTTP 200 | Something gone wrong | Write a log entry
if updateddns.status_code != 200:
        success = 'Incomplete - The DDNS entry: ' + str(_HOST_) + ' | has NOT been updated successfully | WAN IP: ' + str(wanip) +  ' | HTTP Response: ' +  str(updateddns.status_code)
# is HTTP 200 | All working | Write a log entry
else:
        success = 'Complete | The DDNS host: ' + str(_HOST_) + ' | has been updated successfully | WAN IP: ' + str(wanip) + ' | HTTP Response: ' +  str(updateddns.status_code)

# Finish off | Write status | Log to file | write to Syslog
print(success)
log=syslog.syslog
log('... Succeed: {success}'.format(success=success))

# Log To file | Uncomment bellow | Change paths to suit
#logfile = open('/var/log/ddnslogs/log','a')
#logfile.write(datetime.datetime.now().ctime() + ' | ' + success)
#logfile.close
