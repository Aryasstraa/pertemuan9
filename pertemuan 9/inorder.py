import os
os.system('cls')


print("=========== TREE inorder ===========")

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
            
    def inorderTraversal(self,tree):
        res = []
        if tree:
            res = self.inorderTraversal(tree.left)
            res.append(tree.data)
            res = res +self.inorderTraversal(tree.right)
        return res
        
        
tree = Node(2)#root
tree.left = Node(3)#child root kiri
tree.right = Node(4)#child root kanan
tree.left.left = Node(5) #child 3 bagian kiri
tree.left.right = Node(6) #child 3 bagian kanan
tree.right.left = Node(7) #child 4 bagian kiri
tree.right.right = Node(8) #child 4 bagian kanan

# tree.PrintTree()
print(tree.inorderTraversal(tree))

# OUTPUT 
# [5, 3, 6, 2, 7, 4, 8]







