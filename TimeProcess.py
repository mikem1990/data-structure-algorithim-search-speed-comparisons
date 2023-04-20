#Name: Michael Mei
#Date:  03/06/2022
import time    # use time library to time the code executions

# get current time before the process
start_time = time.time()

# run the process
for i in range(1000):
    print( "Hello Everyone!" )

# get current time after the process
end_time = time.time()

# subtract start time from end time to get time used by process
total_time = end_time - start_time

# Show the result.  Note: .6f means “show six decimal places”
print("\nSeconds run 1000 times: {:.6f}".format(total_time))  
