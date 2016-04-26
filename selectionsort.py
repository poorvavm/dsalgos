def selectionsort(my_list):
    for i in range(0, len(my_list) -1):
        minindex =i
        for j in (i+1,len(my_list)):
            if my_list[j]< my_list[minindex]:
                minindex =j
        if minindex!=i:
            my_list[i], my_list[minindex] = my_list[minindex], my_list[i]
