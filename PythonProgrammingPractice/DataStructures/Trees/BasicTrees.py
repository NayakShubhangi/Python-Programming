# Trees are recursive data structures that starts with the root node, followed by children nodes recusively.
# Nodes are essentially the elements of the tree.
# The level of a node is decided based on how many "ancestors" it has.


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def AddChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def ShowTree(self):
        print("     " * self.GetLevel()+self.data)
        if self.children:
            for childnode in self.children:
                childnode.ShowTree()
    
    def GetLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def GetParent(self):
        return self.parent

    def GetChild(self):
        if self.children:
            return self.children
        else:
            return None

    def BinaryTree(self):
        if len(self.children) >= 1 and len(self.children) <=2:
            return True
        else:
            return False

    def LeafNode(self):
        if len(self.children) == 0:
            return True
        else:
            return False


# Home: Bedroom, Kitchen, Living Area
# Bedroom: Bathroom, Dressing Area
# Kitchen: Refridgerator Area, Sink Area
# Living Area: TV Area, Study Area

homeNode = Tree("Home")
bedroomNode = Tree("Bedroom")
kitchenNode = Tree("Kitchen")
livingareaNode = Tree("Living Area")
bathroomNode = Tree("Bathroom")
dressingareaNode = Tree("Dressing Area")
refridgeratorNode = Tree("Refridgerator Area")
sinkareaNode = Tree("Sink Area")
tvareaNode = Tree("TV Area")
studyareaNode = Tree("Study Area")

homeNode.AddChild(bedroomNode)
homeNode.AddChild(kitchenNode)
# homeNode.AddChild(livingareaNode)
bedroomNode.AddChild(bathroomNode)
bedroomNode.AddChild(dressingareaNode)
kitchenNode.AddChild(refridgeratorNode)
kitchenNode.AddChild(sinkareaNode)
livingareaNode.AddChild(tvareaNode)
livingareaNode.AddChild(studyareaNode)

# homeNode.ShowTree()
# print(homeNode.GetLevel())

# TASK ONE:
# Create two new trees tree with two different examples, with at least five levels each.
# Tree 1:
# Nodea = Tree("A")
# Nodeb = Tree("B")
# Nodec = Tree("C")
# Noded = Tree("D")
# Nodee = Tree("E")
# Nodef = Tree("F")
# Nodeg = Tree("G")
# Nodeh = Tree("H")
# Nodei = Tree("I")
# Nodej = Tree("J")
# Nodek = Tree("K")
# Nodel = Tree("L")
# Nodem = Tree("M")
# Noden = Tree("N")
# Nodeo = Tree("O")
# Nodep = Tree("P")
# Nodeq = Tree("Q")

# Nodea.AddChild(Nodeb)
# Nodea.AddChild(Nodec)
# Nodeb.AddChild(Noded)
# Nodec.AddChild(Nodee)
# Nodec.AddChild(Nodef)
# Noded.AddChild(Nodeg)
# Nodee.AddChild(Nodeh)
# Nodef.AddChild(Nodei)
# Nodef.AddChild(Nodej)
# Nodef.AddChild(Nodek)
# Nodeg.AddChild(Nodel)
# Nodeg.AddChild(Nodep)
# Nodeh.AddChild(Nodem)
# Nodeh.AddChild(Noden)
# Nodej.AddChild(Nodeo)
# Nodem.AddChild(Nodeq)
# Nodea.ShowTree()

# Tree 2:
# Node1 = Tree("1")
# Node2 = Tree("2")
# Node3 = Tree("3")
# Node4 = Tree("4")
# Node5 = Tree("5")
# Node6 = Tree("6")
# Node7 = Tree("7")
# Node8 = Tree("8")
# Node9 = Tree("9")
# Node10 = Tree("10")
# Node11 = Tree("11")
# Node12 = Tree("12")
# Node13 = Tree("13")
# Node14 = Tree("14")
# Node15 = Tree("15")
# Node16 = Tree("16")
# Node17 = Tree("17")

# Node1.AddChild(Node2)
# Node1.AddChild(Node3)
# Node2.AddChild(Node4)
# Node3.AddChild(Node5)
# Node3.AddChild(Node6)
# Node4.AddChild(Node7)
# Node5.AddChild(Node8)
# Node6.AddChild(Node9)
# Node6.AddChild(Node10)
# Node7.AddChild(Node11)
# Node7.AddChild(Node12)
# Node8.AddChild(Node13)
# Node3.AddChild(Node14)
# Node8.AddChild(Node15)
# Node9.AddChild(Node16)
# Node10.AddChild(Node17)
# Node1.ShowTree()

# TASK TWO:
# Make a new method called GetParent(), which gets immediate parent of the node.
print(bedroomNode.GetParent().data)

# TASK THREE:
# Make a new method called GetChild(): (If no children, return None, otherwise, return child/children node(s))
if bedroomNode.GetChild():
    for child in bedroomNode.GetChild():
        print(child.data)
else:
    print("No children")

# TASK FOUR:
# Binary tree is a tree where the nodes have at least one children, and at most two children each.
# Make a new method called BinaryTree() that returns True or False based on whether the node is a binary tree.
# (EX: homeNode.BinaryTreeNum() -> False) because the number of immediate children that homeNode has is three (binary trees have at maximum two).
# If the node has zero children, return False
print(homeNode.BinaryTree())

# TASK FIVE:
# When there are no children for a node, that node is called a "Leaf Node."
# Make a new method called LeafNode() that returns True or False based on whether the node is a leaf node (meaning whether the node has no children).
print(bedroomNode.LeafNode())