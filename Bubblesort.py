def bubblesort(mylist):
    for i in range(0, len(mylist)-1):
        for j in range(0, len(mylist)-1-i):
            if mylist[j]> mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

mylist =[7,2,5,4,6,1]
print (bubblesort(mylist))


