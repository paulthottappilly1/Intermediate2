# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
# https://docs.python.org/3/library/time.html

import time
# starts the timer
start = time.time()

# defines the function for the fibonacci sequence
def fibonacci(x):
    if x <= 1:
        return x
    else:
        return(fibonacci(x-1) + fibonacci(x-2))
        
number = 35

print("fib(" + str(number) + ") = " + str(fibonacci(number)))

# ends the timer and stores it in the variable "end"
end = time.time()

print("fib(" + str(number) + ") took " + str(end-start) + " seconds")