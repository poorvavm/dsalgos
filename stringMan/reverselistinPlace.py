## write a program to reverse a list:
my_list =['a','b','c','d','e']
var = None
for i in range(0,len(my_list)/2):
    var = my_str[i]
    my_str[i] = my_str[-i-1]
    my_str[-1-i]=var
print my_str