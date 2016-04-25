# write a Python program to calculate greatest common factor (GCF), also called greatest common divisor (GCD).
def gcf(num1, num2):
    if num1>num2:
        num1, num2 = num2, num1

    for x in range(num1,0,-1):
        if num1%x ==0 and num2%x ==0:
            return x

num1 =10
num2 = 25

print (str(gcf(num1,num2)))