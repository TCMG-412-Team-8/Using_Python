import os.path

if os.path.isfile('logfile.log'):
    print ("Opening File")
else:
    print('Downloading file request')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    r = requests.get(url,allow_redirects=True)

    open('logfile.log','wb').write(r.content)

    print(r.status_code)
    print(r.encoding)
