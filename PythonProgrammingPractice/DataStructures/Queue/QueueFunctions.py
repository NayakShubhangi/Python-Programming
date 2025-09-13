# Build up a queue, and make a function for literally each method/operation
from queue import Queue
import copy

def enqueue(queue_box, input_item):
    queue_box.put(input_item)

def dequeue(queue_box):
    return queue_box.get()

def is_full(queue_box):
    return queue_box.full()

def is_empty(queue_box):
    return queue_box.empty()

def queue_size(queue_box):
    return queue_box.qsize()

def front(queue_box):
    if is_empty(queue_box):
        return None
    # does not work- FIX
    temp_queue = copy.copy(queue_box)
    return temp_queue.get()

def display(queue_box):
    queue_list = []
    for i in range(queue_size(queue_box)):
        queue_list.append(queue_box.get())
    print(queue_list)
    for item in queue_list:
        queue_box.put(item)


# TASK THREE:
# Create another method- call it front()- which should return the first element that is supposed to be removed from the front.
queue1 = Queue(maxsize=4)
enqueue(queue1, 10)
enqueue(queue1, 20)
enqueue(queue1, 40)
enqueue(queue1, 30)
front1 = front(queue1)
front2 = front(queue1)
print(front1)
print(front2)
print(queue_size(queue1))

# put task two here**
def sort(queue_box):
    sorted_queue = Queue()
    temp_list = []
    while not queue_box.empty():
        temp_list.append(queue_box.get())
    temp_list.sort()
    for element in temp_list:
        sorted_queue.put(element)

    return sorted_queue

sorted_queue = sort(queue1)
display(sorted_queue)