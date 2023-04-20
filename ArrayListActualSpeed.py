# Name: Michael Mei
# Date: 03/06/2022

from ArrayList import ArrayList
from Client import Client
from Quicksort import Quicksort
from datetime import date
import time    # use this library to time the code executions
import random  # use to generate random numbers
import sys     # use to terminate the application early

# display name and date in output
print("Name:", "Michael Mei")
print("Date:", date.today())
print()

# create a list
clients = []

# read the records from the ClientData.csv file
# into Client objects and place the Client objects into the list
input_file_name = 'ClientData.csv'
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

# soirt the clients list
Quicksort.sort(clients)
       
# how many client objects do we have?
num_records = len(clients)

# create an ArrayList object
my_array_list = ArrayList()

# Scenario 1: Printer Queue or Call Queue
section_title = "Scenario: Printer Queue or Call Queue"
print(section_title)
print("-" * len(section_title))

# how long does it take to add the client records to the ArrayList?
start_time = time.time()

for i in range(num_records):
    my_array_list.append(clients[i])

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records: {:.6f}".format(total_time))

# how long does it take to remove records from the front of the ArrayList?
start_time = time.time()

for i in range(num_records):
    my_array_list.remove_at(0)

end_time = time.time()
total_time = end_time - start_time
print("Seconds to remove records from front: {:.6f}".format(total_time))

# Scenario 2: Customer Service Center
answer = input("Continue (y/n)?")
if answer.lower() != "y":
    sys.exit() # end the application
    
section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

# add clients to the ArrayList
for i in range(num_records):
    my_array_list.append(clients[i])
    
# how long does it take to randomly display 1000 records?
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    # print(my_array_list.search(Client(random_num)))
    print(my_array_list.search_sorted(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to display random records: {:.6f}".format(total_time))

# Scenario 3: Call Center
answer = input("Continue (y/n)?")
if answer.lower() != "y":
    sys.exit() # end the application
    
section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))
    
# how long does it take to add records, randomly display 1000 records
# and randomly remove 1000 records?

start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_array_list.append(Client(current_id))
    current_id += 1

# display random records    
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    # print(my_array_list.search(Client(random_num)))
    print(my_array_list.search_sorted(Client(random_num)))
    
# remove random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_array_list.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add, display, and remove records: {:.6f}".format(total_time))












