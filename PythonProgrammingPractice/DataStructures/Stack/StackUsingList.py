# Stack is a linear data structure that stores items in a Last-in-First-Out (LIFO) or FILO manner.
# Insert and delete operations are often called push and pop.
# To add an element to a stack, we can use append()- which adds to the front of the stack.
# To remove an element from a stack, we can use pop()- which removes from the rear of the stack.
# top()/peak() - Returns a reference to the topmost element of the stack.
# insert_element(), remove_element(), size(), is_empty(), is_full()
# input1 gets maxsize value

class Stack:
    def __init__(self, maxsize):
        self.stack_box = []
        self.maxsize = maxsize

    # Inserts the element at the top of the stack
    def push_element(self, new_value):
        if not self.full():
            self.stack_box.append(new_value)
        else:
            raise Stack_size_overflow("Stack maxsize is being exceeded")
    
    # Deletes the topmost element of the stack
    def pop_element(self):
        if not self.empty():
            self.stack_box.pop()
        else:
            raise Stack_lacks_elements("Stack has no elements to remove")

    # Returns the size of the stack
    def size(self):
        return len(self.stack_box)
    
    # Returns whether the stack is empty or not
    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    # Returns whether the stack is full or not
    def full(self):
        if self.size() == self.maxsize:
            print("The stack is full; you can't add any more elements.")
        else:
            print(f"The stack is not full; you can add {self.maxsize - self.size()} more elements.")

    # Returns the topmost item of the stack
    def peak(self):
        return self.stack_box[-1]
    
    # Returns the entire stack
    def display_stack(self):
        print(self.stack_box)
        if self.empty():
            print(f"The stack is empty; you can have {self.maxsize} more elements.")
        elif not self.full():
            print(f"Some of the stack is occupied, but {self.maxsize - self.size()} more elements can be added.")
        else:
            print("The stack is full; you can't add any more elements.")


class Stack_size_overflow(Exception):
    pass

class Stack_lacks_elements(Exception):
    pass


stack1 = Stack(maxsize=5)
stack1.push_element(9)
stack1.push_element(7)
stack1.push_element(5)
stack1.push_element(3)
stack1.push_element(1)
stack1.display_stack()
stack1.pop_element()
stack1.pop_element()
stack1.pop_element()
stack1.display_stack()
print(stack1.peak())
stack1.pop_element()
stack1.pop_element()
stack1.empty()
stack1.push_element(2)
stack1.full()
stack1.pop_element()
stack1.display_stack()

# TASK ONE:
# Create a new folder and name it "Queue."
# Convert a list into a queue using classes