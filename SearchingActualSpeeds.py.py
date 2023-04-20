# Name: Michael Mei
# Date: 04/03/2022

from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from Quicksort import Quicksort
from Client import Client
from datetime import date
import random  # use to generate random numbers
import time    # use this library to time the code executions
import sys     # use to exit the application early 

# display name and date in output
print("Name:", "Michael Mei")
print("Date:", date.today())
print()

input_file_name = 'ClientData100.csv'
#input_file_name = 'ClientData1000.csv'
#input_file_name = 'ClientData10000.csv'
#input_file_name = 'ClientData100000.csv'

# create a list
clients = []

# read the records from the ClientData.csv file
# into Client objects and place the Client objects into the list
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int(s[0]) # convert the default string to an int
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # create a client objects using the data from the file
        clt = Client(client_id, f_name, l_name, phone, email)
        #add the client object to the list
        clients.append(clt)

# how many client objects do we have?
num_records = len(clients)

# Scenario 1: Search for 1000 records from a datafile
section_title = "Scenario: Searching Through " + str(num_records) + " Records"
print(section_title)
print("-" * len(section_title))

# MUST SORT THE DATA TO DO A BINARY SEARCH
Quicksort.sort(clients)

# start and end record numbers
start_record = 100001
end_record = start_record + num_records

# how long does it take to sort the records?
start_time = time.time()
       
# how long does it take to do a random linear search through the records?
for i in range(1000):
    client_id = random.randint(start_record, end_record)
    clt = Client(client_id)
    result = BinarySearch.search(clients, clt)
    if result is None:
        print(clt, "was not found.")
    else:
        print(result)

end_time = time.time()
total_time = end_time - start_time
print("Seconds to linear search for 1000 random records: {:.6f}".format(total_time))

# display name and date in output
print("\nName:", "Michael Mei")
print("Date:", date.today())
print()

# display the sorted list
#for clt in clients:
#    print(clt)
    









