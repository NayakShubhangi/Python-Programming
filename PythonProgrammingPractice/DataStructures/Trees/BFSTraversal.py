# Make a program which can perform Level Order Search / BFS




# print(tree.keys())
# print(tree.values())
# print(tree.items())
# print(tree["F"][0])

# def BreadthFirstSearch(tree):
#     output = []
#     keys = list(tree.keys())
#     values = list(tree.values())
#     output.append(keys[0])
    
#     for i in tree:
#         print(tree[i])

# BreadthFirstSearch(tree)


tree = {
    "F": ["D", "J"],
    "D": ["B", "E"],
    "B": ["A", "C"],
    "J": ["G", "K"],
    "G": [None, "I"],
    "I": ["H", None]
}

def bfs_traversal(tree, start_node):
    if start_node not in tree:
        print("Start node not found in the tree")
        return
    queue = [start_node]
    visited = set()
    bfs_result = []
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            if current_node != None:
                bfs_result.append(current_node)
            for child in tree.get(current_node, []):
                if child not in visited:
                    queue.append(child)
    print("BFS Traversal Order:", bfs_result)
 
# bfs_traversal(tree, 'F')



# TASK ONE:
# For the same tree, perform the same BFS traversal for stack or perform BFS traversal using recursion.
def bfs_recursive(tree, queue, visited, bfs_result):
    if not queue:
        return
    current_node = queue.pop(0)
    if current_node not in visited:
        visited.add(current_node)
        if current_node is not None:
            bfs_result.append(current_node)
        for child in tree.get(current_node, []):
            if child not in visited:
                queue.append(child)
    bfs_recursive(tree, queue, visited, bfs_result)

start_node = "F"
if start_node in tree:
    visited = set()
    bfs_result = []
    bfs_recursive(tree, [start_node], visited, bfs_result)
    print("BFS Traversal Order:", bfs_result)
else:
    print("Start node not found in the tree")

# TASK TWO:
# Create a program to make pre order traversal (without stack or recursion).
def dfs_pre_order_traversal(tree, start_node):
    current = start_node
    pre_order_result = []
    stack = []
    while current or stack:
        if current:
            pre_order_result.append(current)
            if tree.get(current):
                right_child = tree[current][1]
                if right_child:
                    stack.append(right_child)
            current = tree.get(current, [None, None])[0]
        else:
            current = stack.pop()
    
    print("Pre-order Traversal:", pre_order_result)

# dfs_pre_order_traversal(tree, "F")

# TASK THREE:
# Create a program to make pre order traversal for stack or using recursion.
def dfs_pre_order_traversal_recursive(tree, node, pre_order_result = None):
    if pre_order_result == None:
        pre_order_result = []
    if node != None:
        pre_order_result.append(node)
        left_child = tree.get(node, [None, None])[0]
        right_child = tree.get(node, [None, None])[1]
        dfs_pre_order_traversal_recursive(tree, left_child, pre_order_result)
        dfs_pre_order_traversal_recursive(tree, right_child, pre_order_result)
    return pre_order_result

pre_order_result = dfs_pre_order_traversal_recursive(tree, "F")
# print("Pre-order Traversal:", pre_order_result)

# TASK FOUR:
# Brush up on linked list, double linked list, circular linked list, and circular queue.