
#------------------------------------------
# Binary search function
#------------------------------------------
def binary_search(array,element):
    lower = 0
    upper = len(array)

    while lower<upper:
        mid_val = lower + (upper-lower)//2
        val = array[mid_val]
        if element == val:
            return mid_val
        elif element > val:
            if lower == mid_val:
                break
            lower = mid_val
        elif element < val:
            upper = mid_val
    return val