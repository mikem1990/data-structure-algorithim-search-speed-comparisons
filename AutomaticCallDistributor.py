# Name: Michael Mei
# Date: 3/20/2022

from Queue import Queue
from Call import Call
from datetime import date
import time          # use to pause the application
import random        # use to generate random numbers

# display author's name and date in the output
print("Name:", "Michael Mei")
print("Date:", date.today())
print()

# create a list
calls = []

# read call records into the list
input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int( s[0] )
        client_name = s[1]
        client_phone = s[2]
        # create a Call object based on the data from the line
        a_call = Call(client_id, client_name, client_phone)
        # add the Call object to the list
        calls.append(a_call)

# Queue object for our calls
calls_waiting = Queue()
call_number = 0

# how long is the simulation?
seconds = int( input("How many seconds do you want to simulate? "))

# run the simulation for the given number of seconds
for i in range(seconds):
    print("-" * 40)
    time.sleep(2)    # pause the application for given number of seconds
    random_event = random.randint(1, 3)
    # do the event based on the random number generated
    if random_event == 1:
        print("Call received. Caller added to queue.")
        calls_waiting.enqueue( calls[call_number] )
        call_number += 1     # set upo the next call
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
    elif random_event == 2:
        print("Call sent to representative for service.")
        if calls_waiting.get_length() > 0:
            print("Caller information:")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
    else:
        print("Nothing happened during this second in time.")
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
        
print("\nThe 'Automatic Call Distributor' simulation has completed.")
            
            
            
            
            
            
            
            
            
            
            
            
            
            