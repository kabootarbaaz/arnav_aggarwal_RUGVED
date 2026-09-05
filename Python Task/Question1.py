# Define a function named “triple_and” that takes three parameters and returns True only if all three are 
# True; otherwise, return False 


def triple_and(a,b,c):
    if a==True and b==True and c==True:
        return True
    else:
        return False
print(triple_and(True,True,True))
#print(triple_and(True, False, True))  {if one of a,b,c is false then this will show False}