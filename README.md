# Using_Python
This project involves parsing a log file and using the data to give information. We used if and for loops to find the answers needed for marketing. 

In the code we use to retrieve the log from the server we use the requests module. 
If the machine you are using does not have this module already, it can easily be downloaded by using the following command in any terminal(cmd,bash,etc):
python -m pip install requests

If any error occurs it is most likely in syntax, check the syntax and try again if you recieve an error. 

All our main code is in the Python Code.py file. The downloadcheck.py file is used to check and see if the log file is already downloaded, and if not will download the file. 

Executing the Python Code.py file will give marketing the answers of how many total requests have been made in the last year of the log (which happens to be the year 1995), and how many total requests were made in the time period of the log. 
