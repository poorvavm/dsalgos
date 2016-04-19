##Using depth-first search, check if a tree contains a value. 
def dfs(root_element, search_element):
    if (root_element is None or search_element is None):
        return False
    elif(root_element.data == search_element.data):
        return True
    elif (root_element.data> search_element.data):
        return dfs(root_element.left, search_element)
    else:
        return dfs(root_element.right, search_element)



## depth first place
def dfp(root_element):
    if root_element == None:
        return False
    else:
        print root_element.data
        dfp(root_element.left)
        dfp(root_element.right)