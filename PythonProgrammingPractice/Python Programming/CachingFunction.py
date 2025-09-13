from time import perf_counter
from functools import cache, lru_cache

@cache
def fibonacci(n:int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# start = perf_counter()
# print(fibonacci(60))
# end = perf_counter()
# print("It took:", end-start, "seconds")

@lru_cache(maxsize=5)     # lru stands for Least Recently Used
def fibonacci2(n:int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)
    
start = perf_counter()
print(fibonacci2(200))
end = perf_counter()
print("It took:", end-start, "seconds")

# The difference between lru_cache and cache is that lru_cache only remembers the most recent outputs.
# The advantage with this is that
# when using just cache, you may run into a memory issue if you're computing a very large function and remembering everything,
# while lru_cache won't have that problem because it only remembers a certain amount of recent outputs rather than all of them.