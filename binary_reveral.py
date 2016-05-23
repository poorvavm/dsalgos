def dec_to_bin(x):
    return int(bin(x)[2:])

def bin_to_dec(b):
    return int(b, 2)

def reverse_bin(decimal_number):
    bin_number = dec_to_bin(decimal_number)
    binary_list = list(str(bin_number))
   
    for i in range (0, len(binary_list)/2):
        temp = binary_list[i]
        binary_list[i] = binary_list[-1-i]
        binary_list[-1-i] = temp
    return bin_to_dec("".join(binary_list))

num = int(raw_input("Enter number: "))
reverse_number = reverse_bin(num)
print reverse_number
