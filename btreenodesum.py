##Given a binary search tree which contains integers as values, calculate the sum of all the numbers. 
def getsum(node):
    if node is None:
        return 0
    else: 
        return node.data + getsum(node.left) + getsum(node.right)