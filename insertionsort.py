def insertionsort(my_list):
    for i in rang(1, len(my_list)):
        for j in range(i-1, -1, -1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            else:
                break