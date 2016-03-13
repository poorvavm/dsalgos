#check if two Strings are anagrams of each other(“abcd”, “dcba”)
str_1 = input("please enter string1: ")
str_2 = input("please enter string2: ")

if len(str_1)==len(str_2):
    str1 = sorted(str_1)
    str2 = sorted(str_2)
    if str2==str1:
        print str_1+ " and " + str_2 + " are anagrams"
    else: 
        "not anagrams"
else: 
    "please enter valid strings"