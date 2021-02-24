#This is the code I'm currently working on, that may or may not work for our situation
import re
import apache_log_parser
import pprint
import sys
import datetime

pp = pprint.PrettyPrinter(indent=4)
now = date.timee.date.time.now()
oneweek = 604800

logfile = "logfile.log"


line_parser = apache_log_parser.make_parser("%h %l %u %t \ "%r\" %>s %b \"%{Referneri\"}i\" \%{User-Agent}i\"")

lines = {}
hits = {}

re.search(" 404 ", line)
#Here's the new section of the code, I'm not sure what this part actually does or if we need it
def handle_line_data(line_data)
    global hits
    global lines
    dateobj = line_data["time_received_datetimeobj"]
    datediff = now - dateobj
    diffsec = dateddiff.total_seconds()

    url = line_data["request_url"]
    header = line_data["request_header_user_agent"]
    ind = url+" - "+header
    
    if diffsec < oneweek:
        return
    lines[ind] = ind
count = 0
nomatch = 0





#This is the while loop I was looking at to modify for our needs
with open(logfile, "r") as f:
    line = f.readline()
    
while line:
    if (re.search(" 404 ", line) and not(re.search("/admin.min.css", line)) ):
        try:
         log_line_data = line_parser(line)
         if count % 1000 == 0:
          print count, nomatch
         count += 1
         handle_line_data(log_line_data)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    else:
        nomatch += 1
    line = f.readline()
f.close()