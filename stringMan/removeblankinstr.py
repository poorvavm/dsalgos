# remove blank space in a string:
my_str = raw_input("Enter string:")
new_str = ""

for i in range(0, len(my_str)):
    if my_str[i]==' ':
        new_str = new_str+""
    else:
        new_str = new_str+my_str[i]
print new_str