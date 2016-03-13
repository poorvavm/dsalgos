
#------------------------------------------
# Linear search function
#------------------------------------------
def linear_search(array,element):
    if element == None or array  == None:
        print "Please enter value"

    for i in range(0,len(array)):
        if array[i] != element: 
            continue
        else:
            print i
