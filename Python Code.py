import requests

print('Downloading file request')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
r = requests.get(url,allow_redirects=True)

open('logfile.txt','wb').write(r.content)
reader = open("logfile.txt","r")
print(r.status_code)
print(r.encoding)

reader.seek(0)

line_number = reader.tell()
total = 0
current = 0
while(reader.readline()!=""):
    reader.seek(line_number)
    line = reader.readline()
    line_number = reader.tell()
    date = ""
    counter = 0

    if line[0] == "l":
        for i in line:
            if counter >= 18 and counter <= 21:
                date += i
            counter += 1
    elif line[0] == "r":
        for i in line:
            if counter >= 19 and counter <= 22:
                date += i
            counter += 1
    #print(date)
    total += 1
    if float(date) == 1995:
        current += 1

print(total)
print(current)



