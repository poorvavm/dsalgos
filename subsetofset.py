# Given two lists (A and B) of unique strings, 
#write a program to determine if A is a subset of B. 
#That is, check if all the elements from A are contained in B. 

def subsetofset_1(list_a, list_b):
    if list_b == None or list_a == None:
        return False
    for element in list_b:
        if element not in list_a:
            return False
    return True
#print subsetofset(["aa","cc","dd"],["aa","bb"])

def subsetofset(list_a, list_b):
    m_di = {}
    if list_b == None or list_a == None:
        return False
    if len(list_a) < len(list_b):
        return False

    for element in list_a:
        m_di[element] = 1

    for element in list_b:
        if element not in m_di:
            return False

    return True

def test_subsetofset():
    assert not subsetofset(["aa","bb","cc","dd"],["aa","xx"]), "b is not a subset of a"
    assert not subsetofset(["aa","bb","cc","dd"],["yy","xx"]), "b is not a subset of a"
    
    assert subsetofset(["aa","bb","cc","dd"],["aa","bb"]), "b is subset of a"
    assert subsetofset([],[]),"both list are empty"
    assert subsetofset(["aa","bb","cc","dd"],[]), "b is empty"
    assert subsetofset(["aa","bb"],["aa","bb"]), " both are identical"
    assert not subsetofset([],["aa"]), "a is empty"
    assert not subsetofset(["aa"],[""]), "b is empty string"
    assert not subsetofset(["aa","bb"],["aa","bb","cc","dd"]), " b is not subset of a"
    assert subsetofset([1,2,3,4],[1,2]),"numeric sbset"
    assert not subsetofset([1,2],[1,2,3]),"numeric sbset"
    assert not subsetofset(None, None), "both are none"
    assert not subsetofset([12], None), "b is none"
    assert not subsetofset(None, [12]), "a is none"
    assert subsetofset([1,2, "hello","aa"],["hello","aa",1]), "b is a mix subset of a"
    print "all test passed"

test_subsetofset()


