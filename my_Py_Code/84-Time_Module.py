#Time Module in python

import time

print(time.time())  # Current time in seconds since the epoch

def usingForLoop():
    for i in range(500):
        print(i)
        # time.sleep(1)

def usingWhileLoop():
    i = 0
    while i < 500:
        print(i)
        # time.sleep(1)
        i += 1

# Measure usingForLoop
start1 = time.time()
usingForLoop()
end1 = time.time()
print(f"usingForLoop took {end1 - start1:.2f} seconds")

# Measure usingWhileLoop
start2 = time.time()
usingWhileLoop()
end2 = time.time()
print(f"usingWhileLoop took {end2 - start2:.2f} seconds")



print(9)
time.sleep(5)  # Sleep for 5 seconds
print("This is printer after 5 seconds")


t=time.localtime()  # Get the current local time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)  # Format the time
print("Current Time:", formatted_time)  # Print the formatted time