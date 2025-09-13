# Another name for CPU is core, and computers with more cores can handle multiple tasks simultaneously
# Threads are lightweight proccesses, and cores can handle many threads
# To check the cores and threads, you can go to the Task Manager and go to the Performance section
# OS is the operating system, which handles both the cores and threads

# Mainthread and Childthreads
# Mainthread is the default thread in Python, and will be created by the OS
# Childthreads are allowed to be created in Python, and help to do tasks simultaneously
# To create threading, we need a module named threading which needs to be inherited, and the methods in our class should be named "run"
# to overwrite the run method which is already defined in the class Thread from the threading module
# A thread that is created by Python as a default is the mainthread, but the threads which are created by the user explicitly are called
# childthreads.
# Mainthread's name can't be changed, while childthread names can be changed.


# def Func1():
#     for i in range(10):
#         print("Raj")

# if __name__ == "__main__":
#     Func1()

from threading import Thread
from time import sleep

# class creatingThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Raj")
#             sleep(2)

# class creatingThread2(Thread):
#     def run(self):
#         for i in range(10):
#             print("Shubhangi")
#             sleep(2)

# obj1 = creatingThread()
# obj2 = creatingThread2()
# obj1.start()
# obj2.start()
# print("string")


# TASK 1
# Come up with a different example of multithreading, and show how multithreading is done/achieved
# import threading
# import time

# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#         time.sleep(1)

# if __name__ == "__main__":
#     t1 = threading.Thread(target=countdown, args=(10,))
#     t1.start()

# TASK 2
# Write a python program to accept 'n' number of parameters and perform the product of all those numbers and print the result
# EX (input): 2, 4, 8           -> 2*4*8
# EX (output): 64
def multiply_numbers(numbers):
  product = 1
  for num in numbers:
    product *= num
  return product

# numbers_list = input("Enter numbers separated by commas: ")
# numbers = [float(num) for num in numbers_list.split(",")]
# result = multiply_numbers(numbers)
# print("Product:", result)
# result = multiply_numbers(2, 3, 4, 5)

# TASK 3
# Brush up on numpy, pandas, and series (meaning everything)

# TASK 4
# Make an example on abstraction, or fix the old one
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Vehicle started.")
    @abstractmethod
    def stop(self):
        print("Vehicle stopped.")

class car(vehicle):
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.model} ({self.year}) started.")
    def stop(self):
        print(f"{self.model} ({self.year}) stopped.")

# car1 = car("Honda Civic", 2023)
# car1.start()
# car1.stop()
# car2 = vehicle()
# car2.start()
# car2.stop()

import threading
import time

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    print(threading.current_thread().name)

def func1():
    for i in range(5):
        print("String")
        time.sleep(1)
    print(threading.current_thread().name)

if __name__ == "__main__":
    t1 = threading.Thread(target=countdown, args=(5,), name="CountdownThread")
    t2 = threading.Thread(target=func1, name="func1Thread")
    t1.start()
    t2.start()
    # .join() can be used to prioritize certain threads over other things, however, it can only be used by threads, nothing else
    t1.join()
    t2.join()
    print("end")
    # print(threading.current_thread().name)
    # TASK ONE
    # Uncomment the following line and look at all of the built-in methods (using a .) in purple and come up with what they do, with an example.
    # print(threading.current_thread().)
    
    # getName - Gets the thread's name
    print(t1.getName())
    # is_alive - Checks if the thread is currently executing
    if t1.is_alive():
        print("Thread is still running")
    # join - Used to prioritize certain threads
    # *On lines 129 and 130*
    # run - It is the method that you overwrite when you use a class to create a thread
    class thread1(Thread):
        def run(self):
            for i in range(10):
                print("Str")
                sleep(1)

    obj1 = thread1()
    # setDaemon - Sets the daemon flag, and a daemon thread exits when the main program exits
    obj1.setDaemon(True)
    # setName - Sets the name of the thread
    obj1.setName("ChildThread")
    # start - Starts the thread
    obj1.start()
    # isDaemon - Checks if the thread is a daemon (which is a thread that exits when the main program exits)
    print(obj1.isDaemon())
    # _bootstrap & _bootstrap_inner - Internal methods used to start the thread's execution
    
    # _delete - Cleans up the thread object after it has finished
    
    # _reset_internal_locks - Resets internal locks used for thread synchronization
    
    # _set_indent - Sets the indentation level for thread debugging output
    
    # _set_native_id - Sets the native thread ID
    
    # _set_tstate_lock - Sets the thread-state lock
    
    # _stop - Tries to stop the thread
    
    # _wait_for_tstate_lock - Waits for the thread-state lock to be released
    
    # __class__ - Returns the thread's class object
    
    # __delatrr__ - It customizes the behavior of attribute deletion
    
    # __dir__ - Returns a list of the thread's attributes and methods
    
    # __eq__ - Defines equality comparison for threads
    
    # __format__ - Defines formatting behavior for threads
    
    # __get_attribute__ - Implements attribute access for threads
    
    # __hash__ - Returns the thread's hash value
    
    # __init__ - Initializes a new thread object
    
    # __init_subclass__ - Called when a subclass of Thread is created
    
    # __ne__ - Defines inequality comparison for threads
    
    # __new__ - Creates a new thread object
    
    # __reduce__ - Defines how to pickle a thread object
    
    # __reduce_ex__ - Defines extended pickling behavior for thread objects
    
    # __repr__ - Returns a string representation of the thread object
    
    # __setattr__ - Implements attribute assignment for threads
    
    # __sizeof__ - Returns the size of the thread object in bytes
    
    # __str__ - Returns a string representation of the thread object

    # Python is both object-oriented and procedure-oriented, meaning that it isn't neccessary to have a class in order to write a program.

# Staircase
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
"""
     #
    ##
   ###
  ####
 #####
######
"""
def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("#", end="")
        print()

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)

# Grading students
# Number line jumps
# Migratory birds