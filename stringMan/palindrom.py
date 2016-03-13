check if String is Palindrome (radar, madam)
str1 = raw_input("Enter string:")
rstr = reversed(str1)
if list(str1) == list(rstr):
    print ("this is a palandrom")
else:
    print ("this is not a palandrom")
