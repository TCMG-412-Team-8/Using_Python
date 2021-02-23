import requests

print('Downloading file request')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url)

with open('/Users/nrcar/Desktop/tcmgfile.txt')
    f.write(r.content)

print(r.status_code)
print(r.headers.['content-type'])
print(r.encoding)
