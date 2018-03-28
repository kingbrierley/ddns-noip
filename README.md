# ddns-noip
A script that will update your no-ip hostname.
I did this because I could run it on my Pi behind my firewall, there are a few others out there that will allow you to do this but most lack functionality for no-ip (WHich is what I always use).
Quick script that will update it using the no-ip API and use crontab to just keep running it, added a couple of other bits to it, args and some logging functionality.

## No-IP DDNS Script
Simple script to update your DDNS host based on either your current WAN IP or an IP you provide
Login details required for your no-ip account and host etc.

Logging enabled, syslog and also written to text file if need be [See bellow]

## Usage
Pass the arguments in a single command or edit script variables, essentially IP is optional as current ip will be used if none is provided.
All arguments passed are prefered over the ones in the script.
Use cron tab to schedule this if required:

## Crontab schedule
corntab -e
use nano (option 2)
Add a line to set your schedule
Heres a few examples:

yearly        0 0 1 1 * 
monthly       0 0 1 * *
weekly        0 0 * * 0
daily         0 0 * * *
hourly        0 * * * *

e.g.
corntab -e
0 * * * * python /path/to/script.py

# Based on current IP
python ddns.py -host [ddns host] -u [Username] -p [Password]
e.g.
python ddns.py -host myname.ddns.net -u myname@someprovider.com -p superstrongpass

# Pass an IP to update
python ddns.py -host [ddns host] -u [Username] -p [Password] -i [Ip address]
python ddns.py -host myname.ddns.net -u myname@someprovider.com -p superstrongpass -i 8.8.8.8

Or edit the script and edit the values in the script save and run:

nano ddns.py
_USERNAME_ = args.username or "Someone@gmail.com"
_PASSWORD_ = args.password or "Somepassword"
_HOST_ = args.hostname or "somethingcool.ddns.net"

## Arguments
The following can be passed as arguments, without these edit the script.
e.g. python ddns.py -i 8.8.8.8 -host some.ddns.net

usage: ddns.py [-h] [-i IPADDRESS] [-host HOSTNAME] [-u USERNAME]
               [-p PASSWORD]

Script to update No-IP account with WAN IP automatically or pass a manual IP

optional arguments:
  -h, --help            show this help message and exit
  -i IPADDRESS, --ipaddress IPADDRESS
                        Manual IP to provide
  -host HOSTNAME, --hostname HOSTNAME
                        Hostname to Parse
  -u USERNAME, --username USERNAME
                        Username to parse
  -p PASSWORD, --password PASSWORD
                        Password to parse



## Setting up log file | IF NEEDED / WANTED | DEFAULT: DISABLED
The script will write to a file to show when this has been updated etc.
It also writes to syslog e.g. /var/log/log
It probably already doesn't exist so make the folders

## Make folders & change owner to use who is running the script
mkdir /var/log/ddnslogs
chown user:user /var/log/ddnslogs/

## Enable logging
Open the script and find the following lines, uncomment these by removing the hash / Pund sign
Feel free to change the log location, file will be created so just needs a valid folder, /var/log should do
Just wanted a seperate ddns log folder as I am fussy.

#logfile = open('/var/log/ddnslogs/log','a')
#logfile.write(datetime.datetime.now().ctime() + ' | ' + success)
#logfile.close

