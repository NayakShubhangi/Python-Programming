# this is where TASK ONE goes
class Queue:
    def __init__(self, maxsize):
        self.queue_box = []
        self.maxsize = maxsize

    # Inserts the element at the top of the queue
    def enqueue(self, new_value):
        if not self.full():
            self.queue_box.append(new_value)
        else:
            raise Queue_size_overflow("Queue maxsize is being exceeded")
    
    # Deletes the topmost element of the queue
    def dequeue(self):
        if not self.empty():
            self.queue_box.pop(0)
        else:
            raise Queue_lacks_elements("Queue has no elements to remove")

    # Returns the size of the queue
    def size(self):
        return len(self.queue_box)
    
    # Returns whether the queue is empty or not
    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    # Returns whether the queue is full or not
    def full(self):
        if self.size() == self.maxsize:
            print("The queue is full; you can't add any more elements.")
        else:
            print(f"The queue is not full; you can add {self.maxsize - self.size()} more elements.")
    
    # Returns the entire queue
    def display_queue(self):
        print(self.queue_box)
        if self.empty():
            print(f"The stack is empty; you can have {self.maxsize} more elements.")
        elif not self.full():
            print(f"Some of the stack is occupied, but {self.maxsize - self.size()} more elements can be added.")
        else:
            print("The stack is full; you can't add any more elements.")


class Queue_size_overflow(Exception):
    pass

class Queue_lacks_elements(Exception):
    pass


queue1 = Queue(maxsize=5)
queue1.enqueue(9)
queue1.enqueue(7)
queue1.enqueue(5)
queue1.enqueue(3)
queue1.enqueue(1)
queue1.display_queue()
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
queue1.display_queue()
queue1.dequeue()
queue1.dequeue()
print(queue1.empty())
queue1.enqueue(2)
print(queue1.full())
queue1.dequeue()
queue1.display_queue()