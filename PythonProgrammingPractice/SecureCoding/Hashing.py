import hashlib

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

# hash_var = hashlib.new("sha256")
hash_var = hashlib.sha256()     # Sets the algorithm
hash_var.update("Shubhangi".encode())     # Update takes bytes data (use b before the plaintext) to convert into hash
print(hash_var.digest())     # Digest displays the hash value
print(hash_var.hexdigest())     # Hexdigest displays the hash value in a slightly easier to read format

hashed_var = "9ca4eaa73e572cb3e8320ca2f1b2973b46c9b4b0a9d6b9abff085c3e8c9f11da"
hash_var2 = hashlib.sha256()
input_var = input("Enter text: ")
hash_var2.update(input_var.encode())
print(hash_var2.digest())
print(hash_var2.hexdigest())
print(hash_var2.hexdigest() == hashed_var)