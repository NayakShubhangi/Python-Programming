# The in-built hash() takes an object as a parameter, but the object can't be modifiable
# Integer, float, string, tuple, frozenset (Non-Modifiable) <- Hashable
# List, set, dictionary (Modifiable) <- Unhashable
# (Only the objects on line 2 can be used in hash())

# plainText = eval(input("Enter: "))
# print(hash(plainText))

# TASK ONE:
# Create a function, name it isHashable(), with a parameter of obj.
# The function should return True or False based on whether the object is hashable for the in-built hash().
# Use try and except to attempt to hash, if success, then True, if fail, then False.
# Integer, float, string, tuple, frozenset (Non-Modifiable) <- Hashable
# List, set, dictionary (Modifiable) <- Unhashable
def isHashable(obj):
    try:
        hash(obj)
        print("The object is hashable.")
    except TypeError:
        print("The object is not hashable.")

hashinput = eval(input("Enter: "))
isHashable(hashinput)

# TASK TWO:
# Go through bytes, byte array, and memory view, with examples for each.
# Bytes: Immutable sequence of bytes.
byte_ex = bytes([65, 66, 67, 68])
# ASCII values for 'A', 'B', 'C', 'D'
print(byte_ex)
# Byte Array: Mutable sequence of bytes.
barray = bytearray([65, 66, 67, 68])
print(barray)
# Memory View: Provides a way to access and manipulate the internal buffer of an object (like bytes or bytearray) without copying the data.
mv = memoryview(barray)
print(mv[0])

# TASK THREE:
# Test on everything related to class objects (static methods/variables, class methods/variables, properties, decorators, data classes, inheritance,
# anything)

# TASK FOUR (continued):
# Go through callable built-in function, breakpoint function, complex, isinstance, compile, with examples for each.
# Callable:
# Breakpoint: 
# Complex: 
# Isinstance: 
# Compile: 