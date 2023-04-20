# Name: Michael Mei
# Date: 03/27/2022

from MergeSort import MergeSort
from Client import Client
from datetime import date
import time    # use this library to time the code executions

# display name and date in output
print("Name:", "Michael Mei")
print("Date:", date.today())
print()

#input_file_name = 'ClientData100.csv'
#input_file_name = 'ClientData1000.csv'
#input_file_name = 'ClientData10000.csv'
input_file_name = 'ClientData100000.csv'

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

# Scenario 1: Sorting records from a data file
section_title = "Scenario: Sorting " + str(num_records) + " Records"
print(section_title)
print("-" * len(section_title))

# how long does it take to sort the records?
start_time = time.time()
       
# call the static sort method in the class
MergeSort.sort(clients)

end_time = time.time()
total_time = end_time - start_time
print("Seconds to sort {0} records: {1:.6f}".format(num_records, total_time))

# display the sorted list
#for clt in clients:
#    print(clt)
    









