# Program to find number of each character in a string
my_str = input("Please enter string: ")
ltr_count ={}

for letter in my_str:
    if letter in ltr_count:
        ltr_count[letter]+=1
    else:
        ltr_count[letter] = 1

max_count = -1
max_char = ''

for letter in ltr_count:
    if ltr_count[letter] > max_count:
        max_count = ltr_count[letter]
        max_char = letter

print max_char + " occurs max number of times i.e. " + str(max_count)

min_count = len(my_str)+1
min_char = ''
for letter in ltr_count:
    if ltr_count[letter] == 1:
        min_count = 1
        min_char = letter
        break

    if ltr_count[letter] < min_count:
        min_count = ltr_count[letter]
        min_char = letter

print min_char + " occurs min number of times i.e. " + str(min_count)