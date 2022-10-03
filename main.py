import re
import sites
#Data
check = int
link = input("Enter link : ")
webs = ["twitter.com","instagram.com","youtube.com"]
#Checking the Service
for i in webs:
    if i in link:
        check = i
        break
#To run respective function
output = getattr(sites, check[:-4])
output(link)