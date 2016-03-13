# Factorial of a number
num= raw_input("Enter a number:")
num =int(num)
Factorial = 1

if num < 0:
    print ("Factorial doesn't exist")
elif num == 0:
    print ("0 factorial is 1")
else:
    for i in range (1,num + 1):
        Factorial = Factorial*i

print("The factorial of",num,"is",Factorial)