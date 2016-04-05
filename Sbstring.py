
## To check assert and substring of a string
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

def test_sbstr():
    assert not sbstr(None, None), "negative test case 1: strings are none"
    assert not sbstr(None, "poorvavm"), "Negative test case 2: substring is none"
    assert not sbstr("Poorva", None), "Negative test case 3: main string in none"
    assert not sbstr("poorvavm1","poorvavm"), "negative test case 4: substring is longer then main string"
    assert not sbstr("porva","poorvavm"), "negative test case 5 substring is not in order as main string"
    assert not sbstr("poopoorva","vmpoorvavm"), " negative Test case 6: substring is repeting in parts"
    assert not sbstr("avroop","vmpoorva"), "negative Test case 7: substring is revers of main string"
    assert not sbstr("poorvapoorva","vmpoorva"), "negative test case 8: substring is repetation"
    assert not sbstr("   ","vmpoorva"), "negative test case 9: substring is a space"
    assert not sbstr("vmpoorva   ","     "), "negative test case 10 main string is a space"
    assert not sbstr(""," "),"one strings is empty"
    assert not sbstr(9,10), "both strings are integer"
    
    assert sbstr("poorva","poorva"), "positive Test case 1: both strings are same"
    assert sbstr("poorva","poorvavm"), "positive Test case 2: substring is smaller then main string"
    assert sbstr("poorva","vmpoorva"), "positive Test case 3: substring is a part of of main string"
    assert sbstr("poorva","vmpoorvavm"), "positive Test case 4: substring is in middle of main string"
    assert sbstr("poorva","vmpoorva poorva"), "positive Test case 5: main string has mulitple time substring"
    assert sbstr("poorvapoorva","vmpoorvapoorvapoorva"), "positive Test case 6: substring and main string is repeting"
    assert sbstr("   ","    "), "positive Test case 7: both strings are space"
    assert sbstr("",""),"both strings are empty"
    assert sbstr('9','910'), "both integres are string"
    print "All test cases pass"

test_sbstr()
