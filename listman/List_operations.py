# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    n = len(numbers)-1
    for num in range(n,0):
        print num
        if numbers[n]%2 ==1:
            break
        n-=1
    numbers.pop(n)


"""
    Given a list of numbers, remove the last odd number from the list. 
    """
    
    def remove_last_odd(num_list):
        if not num_list or len(num_list)==0:
            return num_list
    
        n = len(num_list)-1
        while(n >= 0):
            if num_list[n] % 2 == 1:
                break
            n -= 1
        num_list.pop(n)
        return num_list
    
    def test_code():
        assert remove_last_odd([1,2,5,7,3,2,11,14]) == [1,2,5,7,3,2,14]
        assert remove_last_odd([1,2,3,4,6,8]) == [1,2,4,6,8]
        assert remove_last_odd([]) == []
        assert remove_last_odd(None) == None
        print "Tests passed!!"

    
  

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()