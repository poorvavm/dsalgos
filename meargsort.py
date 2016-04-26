def meargesort(my_list):
    mearge_sort2(my_list,0, len(my_list)-1)

def meargesort2(my_list, first, last):
    if first<last:
        middle = (first+last)//2
        meargesort2(my_list, first, middle)
        meargesort2(my_list, middle+1, last)
        mearge(my_list, first, middle, last)


def mearge(my_list, first, middle, last):
    left = my_list[first:middle]
    right = my_list[middle:last]
    i=j=0
    for k in range(first, last+1):
        if left[i] <= right[j]:
            my_list[k] = left[i]
            i += 1
        else:
            my_list[k]= right[j]
            j += 1
