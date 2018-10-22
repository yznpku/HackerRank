"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    if root != None :
        print(root.info,end=" ")
        preOrder(root.left)
        preOrder(root.right)
    return