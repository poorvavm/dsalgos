def quick_sort(my_list):
    quicksort2(my_list,0,len(my_list)-1)


def quicksort2(my_list,low, high):
    if low<hight:
        p = partition(my_list, low, high)
        quicksort2(my_list, low, p-1)
        quicksort2(my_list, p, high)


def get_pivot(my_list, low, high):
    mid = (high+low)//2
    pivot = high
    if my_list[low]<my_list[mid]:
        if my_list[mid]<my_list[high]:
            pivot =mid
        elif my_list[low]<my_list[high]:
            pivot = low
        return pivot

def partition(my_list, low, high):
    pivotindex = get_pivot(my_list, low, high)
    pivotvalue = my_list[pivotindex]
    my_list[pivotindex], my_list[low] = my_list[low], my_list[pivotindex]
    border = low

    for i in range(low, high+1):
        if my_list[i] <pivotvalue:
            border+=1
            my_list[i], my_list[border] = my_list[border], my_list[i]
        my_list[low], my_list[border] = my_list[border], my_list[low]

        return (border)