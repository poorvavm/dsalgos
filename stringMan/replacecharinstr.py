#Replace a character in a string:
my_str = raw_input("Enter string:")
new_str = ""
replace_char = raw_input("enter old character")
new_char = raw_input("enter character")

for i in range(0,len(my_str)):
    if my_str[i]=='replace_char':
        new_str=new_str+'new_char'
    else:
        new_str = new_str+my_str[i]
print new_str