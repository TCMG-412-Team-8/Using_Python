
# This tells us how many total requests were made 
total = 0
for line in open("/home/skip/Downloads/http.log"):
    total = total +1 

print("The total amount of requests are:",total)


# This calculates how many requests were done in the last year 

TOTAL = 0
YEAR = 0 

for line in open("/home/skip/Downloads/http.log"):
    items = line.split()
    if len(items) < 9:
        continue 
    year = items[3].split(':')[0][-4:]
    if year == '1995':
        YEAR += 1
        TOTAL += 1

print ('This is the total amount of requests in the last year (1995):',YEAR)
        