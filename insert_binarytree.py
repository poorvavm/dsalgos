# Insert an element into a binary search tree (in order). 
#You may assume that the binary search tree contains integers. 
def insertnode(rootnode, newnode):
    if (newnode.data < rootnode.data and rootnode.left is None):
        rootnoode.left = newnode
    elif(newnod.data > rootnode.data and rootnode.right is None):
        rootnode.right = newnode
    elif(newnode.data < rootnode.data):
        insertnode(rootnode.left, newnode)
    elif(newnode.data > rootnode.data):
        insertnode(rootnode.right, newnode)
    else:
        print "please enter node"
 