# rear=((rear+1)%capacity)
# front=((front+1)%capacity)
# For circular queues, we don't really know the start point, so the front and rear are set to -1.

class CircularQueue:
    def __init__(self, capacity):
        self.head = -1
        self.tail = -1
        self.capacity = capacity
        self.storage = [] * self.capacity
    
    def enqueue(self, element):
        if (self.tail + 1) % self.capacity == self.head:  # We are checking whether the queue is full or not
            print("The circular queue is full.")
        elif self.head == -1:                  # Through this condition, we make sure that enqueue is happening for the first time
            self.head = 0
            self.tail = 0
            self.storage.insert(self.tail, element)
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.storage.insert(self.tail, element) 
    
    def dequeue(self):
        if self.head == -1:         # We are checking whether dequeue is happening for the first time
            print("The circular queue is empty.")
        elif self.head == self.tail: # We are verifying whether the capacity is full
            temp = self.storage[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.storage[self.head]
            self.storage.pop(self.head)
            self.head = (self.head + 1) % self.capacity
            return temp
    
    def isFull(self):
        if (self.tail + 1) % self.capacity == self.head:
            return True
        else:
            return False

    def isEmpty(self):
        if self.head == -1:
            return True
        else:
            return False

circQueue1 = CircularQueue(5)
circQueue1.enqueue(8)
print(circQueue1.storage)
circQueue1.enqueue(2)
print(circQueue1.storage)
circQueue1.enqueue(9)
print(circQueue1.storage)
circQueue1.dequeue()
print(circQueue1.storage)
circQueue1.dequeue()
print(circQueue1.storage)
circQueue1.enqueue(3)
print(circQueue1.storage)
circQueue1.enqueue(1)
print(circQueue1.storage)
circQueue1.enqueue(7)
print(circQueue1.storage)
circQueue1.enqueue(11)
print(circQueue1.storage)
print(circQueue1.isEmpty())
print(circQueue1.isFull())

# TASK ONE: -fix-
# [8]
# [8, 2]
# [8, 2, 9]
# [2, 9]
# [2]           <- in this line, 9 got removed, but 2 should be removed. fix that
# [2, 3]
# [2, 3, 1]
# [7, 2, 3, 1]
# [7, 11, 2, 3, 1]
# False
# True