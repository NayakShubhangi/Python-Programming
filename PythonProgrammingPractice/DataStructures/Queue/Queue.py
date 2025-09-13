# Queue is a built-in module in Python to implement a data structure queue.
# Queue follows a FIFO rule: First In, First Out.
# queue.Queue(maxsize) initializes a variable to a maximum size of maxsize.
# A maxsize of 0 means it is an infinite queue.
# The process of adding an element to the queue is called enqueue. (.put())
# The process of removing an element to the queue is called dequeue. (.get())

from queue import Queue
from QueueFunctions import enqueue, dequeue, is_empty, queue_size

queue1 = Queue(maxsize=4)
# print(queue1.qsize())
# # To insert a value into a queue, we have to use .put(), just like how lists use .append()
# queue1.put(1)
# queue1.put(2)
# queue1.put(3)
# print(queue1.qsize())
# queue1.put(4)
# print(queue1.qsize())
# # To remove a value from a queue, we have to use .get(), where the "first" value always gets removed, and returns it as well
# print(queue1.get())
# print(queue1.qsize())
# # To check if a queue is empty, we use .empty(): If the queue is empty, it prints True, and if the queue is not empty, it prints False.
# print(queue1.empty())
# # To check if a queue is full, we use .full(): If the queue is full- or at its maxsize- , it prints True, and if the queue isn't, it prints False.
# print(queue1.full())


# Write a program to take space separated inputs from the user
# Ask each "person" whether they want to enque, getsize, check if queue is full, and check if queue is empty, and dequeue.
# check if queue is empty before dequeueing, and don't throw error; just don't dequeue.
# EX:
# INPUT: Bob Alice Xavier James
# OUTPUT: *ask each person*

# Note: Following program uses import QueueFunctions
# persons = [i for i in input("Enter space separated names of people: ").split()]
# people_queue = Queue(maxsize=len(persons))
# valid_actions = ["enqueue", "getsize", "queuefull", "queueempty", "dequeue"]
# for person in persons:
#     action = input(f"{person}, enter an action (enqueue, getsize, queuefull, queueempty, dequeue): ").lower()
#     while action not in valid_actions:
#         print("That's not a valid action.")
#         action = input(f"{person}, enter an action (enqueue, getsize, queuefull, queueempty, dequeue): ").lower()
#     if action == "enqueue":
#         result = QueueFunctions.enqueue(people_queue, person)
#         result2 = QueueFunctions.queue_size(people_queue)
#         print(f"The size of the queue is {result2}.")
#     elif action == "getsize":
#         result = QueueFunctions.queue_size(people_queue)
#         print(f"The size of the queue is {result}.")
#     elif action == "queuefull":
#         result = QueueFunctions.is_full(people_queue)
#         if result:
#             print("The queue is full.")
#         else:
#             print("The queue is not full.")
#         result2 = QueueFunctions.queue_size(people_queue)
#         print(f"The size of the queue is {result2}.")
#     elif action == "queueempty":
#         result = QueueFunctions.is_empty(people_queue)
#         if result:
#             print("The queue is empty.")
#         else:
#             print("The queue is not empty.")
#         result2 = QueueFunctions.queue_size(people_queue)
#         print(f"The size of the queue is {result2}.")
#     elif action == "dequeue":
#         if QueueFunctions.is_empty(people_queue):
#             print("Cannot dequeue: Queue is empty!")
#         else:
#             result = QueueFunctions.dequeue(people_queue)
#             print(f"{result} was dequeued.")
#         result2 = QueueFunctions.queue_size(people_queue)
#         print(f"The size of the queue is {result2}.")

# TASK ONE:
# Modification: If you ask for queuefull, queueempty, enqueue, and dequeue, you should also include the size of the queue.

# TASK TWO:
# Write a program to take one integer input on one line (referred to as n), and comma separated integer inputs on the second line.
# The task is to reverse the order of the first n elements of the queue, leaving the other elements in the same relative order
# EX:
# INPUT: n = 5
# INPUT2: 10,20,30,40,50,60,70,80,90,100
# Note: input2 is a list, but it gets turned into a queue for the output
# OUTPUT: 50,40,30,20,10,60,70,80,90,100

# Note: Following program uses from QueueFunctions import enqueue, dequeue, is_empty, queue_size
# n = int(input("Enter an integer: "))
# elements_list = input("Enter comma-separated integers: ").split(",")
# element_queue = Queue()
# for i in elements_list:
#     enqueue(element_queue, i)
# list1 = []
# for j in range(n):
#     list1.append(dequeue(element_queue))
# while list1:
#     enqueue(element_queue, list1.pop())
# size = queue_size(element_queue)
# for k in range(size - n):
#     enqueue(element_queue, dequeue(element_queue))
# output_list = []
# while not is_empty(element_queue):
#     output_list.append(dequeue(element_queue))
# print(",".join(output_list))

# TASK FIVE:
# Circular queue: A data structure that connects the last element to the first.

# TASK SIX:
# Priority queue: Arranges elements based on their priority values- the higher the priority value, the higher the priority.

# TASK SEVEN:
# Show the difference between linear queue versus circular queue,
# and the difference between circular queue versus priority queue.
# Linear vs circular: In a linear queue, the order has a "fixed" start and a "fixed" end,
# while in a circular queue, the end connects back to the start (Which improves memory efficiency by reusing space,
# while linear queues can have wasted space).
# Circular vs Priority: In a circular queue, the order is FIFO,
# while in a priority queue, the elements are prioritized based off their priority value.

# task three goes here**
def reverse_queue(queue_box):
    if queue_box.empty():
        return queue_box
    front = queue_box.get()
    reverse_queue(queue_box)
    queue_box.put(front)
    return queue_box

queue2 = Queue()
queue2.put(1)
queue2.put(2)
queue2.put(4)
queue2.put(3)
queue2.put(5)
print("Original Queue:", list(queue2.queue)) 
reversed_queue = reverse_queue(queue2)
print("Reversed Queue:", list(reversed_queue.queue))