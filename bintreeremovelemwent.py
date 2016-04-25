##How to remove / delete a node from a binary search tree (BST) in Python.

parent =None
node = self.root

# find the node to remove
while node and node.value != data:
    parent = node
    if data< node.value:
        node = node.leftchild
    elif data > node.value:
        node = node.rightchild

# Data is in the root node
elif self.root.value = data:
    if self.root.leftchild is None and self.root.rightchild is None:
        self.root = None
    elif self.root.leftchild and self.root.rightchild is None:
        self.root = self.root.leftchild
    elif self.root.rightchild is None and slef.root.rightchild:
        self.root = self.root.rightchild
    elif self.root.leftchild and self.root.rightchild:
        delNodeparent = node
        delNode = node.rightchild
        while delNode.leftchild:
            delNodeparent = delNode
            delNode = delNode.leftchild
        self.root.value = delNode.value
        if delNode.rightchild:
            if delNodeparent.value > delNode.value:
                delNodeparent.leftchild = delNodeparent.rightchild
            elif delNodeparent.value < delNode.value:
                delNodeparent.rightchild = delNode.rightchild
        else:
            if delNode.value < delNodeparent.value:
                delNodeparent.leftchild =None
            else:
                delNodeparent.rightchild = None


# data not found
if node in None or node.value!= data:
    return False

# remove node has no child
elif node.leftchild is None and node.rightchild is None:
    if data < parent.value:
        parent.leftchild = None
    else: 
        parent.rightchild = None
    return True

# remove node has left child only
elif node.leftchild and node.rightchild is None:
    if data < parent.value:
        parent.leftchild = node.leftchild
    else: 
        parent.rightchild = node.leftchild
    return True

# remove node has right child only
elif node.leftchild is None and node.rightchild:
    if data < parent.value:
        parent.leftchild = node.rightchild
    else: 
        parent.rightchild = node.rightchild
    return True

# remove node has left and right child:
else:
    delNodeparent = node
    delNode = node.rightchild
    while delNode.leftchild:
        delNodeparent = delNode
        delNode = delNode.leftchild

    node.value = delNode.value
    if delNode.rightchild:
        if delNodeparent.value > delNode.value:
            delNodeparent.leftchild = delNodeparent.rightchild
        elif delNodeparent.value < delNode.value:
            delNodeparent.rightchild = delNode.rightchild
    else:
        if delNode.value < delNodeparent.value:
            delNodeparent.leftchild =None
        else:
            delNodeparent.rightchild = None






