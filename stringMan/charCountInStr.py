# write a program to find number of each character in a string
my_str = input("Please enter string: ")

ltr_count ={}

for letter in my_str:
    if letter in ltr_count:
        ltr_count[letter]+=1
    else:
        ltr_count[letter] = 1
print ltr_count