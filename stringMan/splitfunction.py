# write a split function in python
my_str = input("Please enter string: ")
m_list = []
word =""
for letter in m_str:
    if letter!=" ":
        word += letter
    else:
        m_list.append(word)
        word =""
print m_list