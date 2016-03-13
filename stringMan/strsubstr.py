#find out if str_a is substring of str_b

def sbstr(str_a, str_b):
    if type(str_a) is not str or type(str_b) is not str:
        return False
    if str_a is None or str_b is None or len(str_a)>len(str_b):
        return False

    if str_a==str_b:
        return True

    if len(str_a)==0 or len(str_b)==0:
        return False

    for i in range(0, len(str_b)):
        if str_b[i:i+len(str_a)]==str_a[0: ]:
            return True
    
    return False