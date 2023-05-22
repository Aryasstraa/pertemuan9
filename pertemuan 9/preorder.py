import os
os.system('cls')


print("=========== TREE preorder ===========")

class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    def PreOrderTraversal(self,tree):
        res =[]
        if tree:
            res.append(tree.data)
            res = res + self.PreOrderTraversal(tree.left)
            res = res + self.PreOrderTraversal(tree.right)
        return res
        
tree = Node(2)#root
tree.left = Node(3)#child root kiri
tree.right = Node(4)#child root kanan
tree.left.left = Node(5) #child 3 bagian kiri
tree.left.right = Node(6) #child 3 bagian kanan
tree.right.left = Node(7) #child 4 bagian kiri
tree.right.right = Node(8) #child 4 bagian kanan

# tree.PrintTree()
print(tree.PreOrderTraversal(tree))

# OUTPUT
# [2, 3, 5, 6, 4, 7, 8]







