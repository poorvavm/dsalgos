# write a program to reverse a string
my_str = input("Please enter string: ")
r_str =""
for i in range(0,len(my_str)):
    r_str += my_str[-1-i]
print r_str