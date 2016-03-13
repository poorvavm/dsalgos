# Print duplicate characters from String
my_str = raw_input("enter string: ")
count ={}
for char in my_str:
    if char in count:
        count[char]+=1
    else:
        count[char] = 1

for char in count:
    if count[char]>1:
        print count[char], char