## Write the pseudocode for breadth-first search on a binary tree. Try to be as detailed as possible. 

def bfs(root_element, search_element):
    q1 = queue()
    q1.enque(root_element)

    while (q1 is not empty):
        current_val = q1.deque(q1)
        if current_val.data = search_element.data:
            return True
        else:
            q1.enque(root_element.left)
            q1.enque(root_element.right)
    return False