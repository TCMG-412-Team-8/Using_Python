import requests
import re 
from collections import Counter 
# print('Downloading file request')

# url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# r = requests.get(url,allow_redirects=True)

# open('logfile.log','wb').write(r.content)

# print(r.status_code)
# print(r.encoding)




log = 'logfile.log' 
def reader(log):
    with open('logfile.log') as f:
        log = f.read()
        match= re.search(r'^GET',log)
        request_count = Counter(match)
        for k, v in request_count.items():
            print("Number of requests" + "=> " + str(k) + " " + "Count "  + "=> " + str(v))


if __name__ == '__main__':
    print("The output is", reader("access_log"))