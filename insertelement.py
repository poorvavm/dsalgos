# 16.1 Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order. 
# jump to question
# We can imagine that our array looks something like this (with a blank spot at the end):
# 1 4 7 8 9 _
# If we need to insert an element like 6, we can’t just insert it at the end. We are supposed to put it in order.
# 1 4 6 7 8 9
# This requires “shifting” all elements down to make space for 6 and then inserting it.
# There are two ways of approaching this problem.
# Approach 1: Shift From Back, Then
def ins_element(mlist, new_val = 0):
    if new_val < 0:
        return mlist
    if len(mlist) == 1:
        mlist[0] = new_val
        return mlist

    for i in range(0,len(mlist)):
        if new_val < mlist[i]:
            temp = mlist[i]
            mlist[i] = new_val
            new_val = temp
    mlist[len(mlist)-1] = new_val
    return mlist

print ins_element([0,1,3,4,5,6,0], 2)
