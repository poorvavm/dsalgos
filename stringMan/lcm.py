# find lowest common multiple / least common denominator (LCM / LCD) in Python

def lcm(num1, num2):
    if num1>num2:
        num1, num2 = num2, num1
    for x in range(num2, num1*num2+1, num2):
        if x%num1 ==0:
            return x

num1 =3
num2 =4
print (str(lcm(num1,num2)))

# def lcm for list of 3 numbers:
def lcm3(num_list):
    num_list.sort()
    worst = num_list[0] * num_list[1] * num_list[2]
    for x in range(num_list[2], worst+1, num_list[2]):
        if x%num_list[0] ==0 and x%num_list[1] == 0:
            return x


num_list = [3, 2, 16]
print (str(lcm3(num_list)))
