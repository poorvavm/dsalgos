# writing a program to calculate prime numbers in Python.
def primnumber(number):
    isPrime = True
    for i in range(2,number):
        if number%i == 0:
            isPrime = False
    return i

