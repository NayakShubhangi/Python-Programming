class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            self.left = None
            self.right = None
    
    def addChild(self, value):
        if self.value == value:
            return
        if self.value == None:
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        if value < self.value:
            if self.left:
                self.left.addChild(value)
            else:
                self.left.BinarySearchTree(value)
        if value > self.value:
            if self.right:
                self.right.addChild(value)
            else:
                self.right.BinarySearchTree(value)
    
    def InOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.InOrderTraversal()
        if self.value is not None:
            elements.append(self.value)
        if self.right:
            elements += self.right.InOrderTraversal()
        return elements
    
    def searchNode(self, value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.searchNode(value)
            else:
                return False
        else:
            if self.right:
                return self.right.searchNode(value)
            else:
                return False

elements = [14, 8, 5, 10, 12, 78, 53, 89]
root = BinarySearchTree(elements[0])
for i in range(1, len(elements)):
    root.addChild(elements[i])
print(root.InOrderTraversal())
print(root.searchNode(11))
# In Order, Pre Order, & Post Order
#     4
#    / \
#   2   6
#  /|   |\
# 1 3   5 7
# Pre Order (Root, left subtree, right subtree): 4, 2, 1, 3, 6, 5, 7
# In Order (Left subtree, root, right subtree): 1, 2, 3, 4, 5, 6, 7
# Post Order (Left subtree, right subtree, root): 1, 3, 2, 5, 7, 6, 4