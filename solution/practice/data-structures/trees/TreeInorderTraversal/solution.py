"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root != None :
        inOrder(root.left)
        print(root.info,end=" ")
        inOrder(root.right)
    