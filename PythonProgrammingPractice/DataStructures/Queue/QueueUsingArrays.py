# storage = [None] * 4
# print(storage)
# size, capacity, front, rear
# enqueue, dequeue
class Queue:
    def __init__(self, capacity):
        self.size = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity
    
    def enqueue(self, element):
        if self.size < self.capacity:
            self.storage[self.rear] = element
            self.size += 1
            self.rear += 1
        else:
            raise Queue_is_full("Queue is full; cannot add any more elements.")
    
    def dequeue(self):
        if self.size == 0:
            raise Queue_is_empty("Queue is empty; cannot remove any elements.")        
        else:
            temp = self.storage[self.front]
            self.storage[self.front] = None
            self.size -= 1
            self.front += 1
        if self.front == self.rear:
            self.front = 0
            self.rear = 0
        return temp

class Queue_is_full(Exception):
    pass

class Queue_is_empty(Exception):
    pass

# arr_queue1 = Queue(5)
# print(f"storage = {arr_queue1.storage}")
# arr_queue1.enqueue(1)
# print(f"storage = {arr_queue1.storage}")
# arr_queue1.enqueue(2)
# print(f"storage = {arr_queue1.storage}")
# print(f"Dequeued {arr_queue1.dequeue()}")
# print(f"storage = {arr_queue1.storage}")
# print(f"Dequeued {arr_queue1.dequeue()}")
# print(f"storage = {arr_queue1.storage}")
# print(f"Size: {arr_queue1.size}")
# print(f"Capacity: {arr_queue1.capacity}")
# print(f"Front: {arr_queue1.front}")
# print(f"Rear: {arr_queue1.rear}")

# NOTE: CODE HAS BEEN MOVED HERE FROM BinarySearchUsingArrays.py
def LinearSearch_Queue(queue, search_val):
    index = queue.front
    count = 0
    while count < queue.size:
        if queue.storage[index] == search_val:
            return count
        index = (index + 1) % queue.capacity
        count += 1
    return -1

linearqueue = Queue(5)
linearqueue.enqueue(10)
linearqueue.enqueue(20)
linearqueue.enqueue(30)
linearqueue.enqueue(40)
search_val = int(input("Enter a number: "))
print(LinearSearch_Queue(linearqueue, search_val))

# TASK ONE:
# What is: Time complexity, space compexity, denotions
# Time complexity measures how the execution time of an algorithm scales with the size of the input.
# Essentially, it sees how long it takes an algorithm to run as the amount of input increases.
# Space complexity measures the amount of space/memory an algorithm needs to run as a function of the input size.
# how to get time & space complexity (if possible)
# Denotions:
# O(1): Constant time.
# O(log n): Logarithmic time.
# O(n): Linear time.
# O(n log n): Log-linear time.
# O(n^2): Quadratic time.
# O(2^n): Exponential time.
# O(n!): Factorial time.

# TASK TWO:
# Write a program to sort a queue in ascending order (put in QueueFunctions.py)

# TASK THREE:
# Write a program to reverse a queue using recursion (put in Queue.py)