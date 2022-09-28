# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.


import csv
from collections import defaultdict

# open the vendorlist file
infile = open("VendorList.csv","r")

# create a csv object from the file object
csvfile = csv.reader(infile,delimiter=",")
next(csvfile) # skips header

# create an output file
outfile = open("marketinglistFINAL.csv","w")

dictionary = {}
key = []
values = []

for line in csvfile:
    name = (line[1] + " " + line[2])
    key.append(name)
    info = ("email: " + line[4] + "," + " phone: " + line[5])
    values.append(info)

res = defaultdict(list)
for i, j in zip(key, values):
    res[i].append(j)

print(str(dict(res)))

outfile.write("Name, Email, Phone")
outfile.write("\n")
outfile.write(str(dict(res)))

infile.close()
outfile.close()
