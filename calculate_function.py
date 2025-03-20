def sum(a,b):
    add = a+b
    return add

def sub(a,b):
    minus = a-b
    return minus

def multiplication(a,b):
    multiply = a*b
    return multiply 

def division(a,b):
    divide = a/b
    return divide

def compare(a,b):
    if a>b:
        return True
    else:
        return False
    

def lmultiple(l):
    for i in l:
        print("the multiple with two is ",i*2)
    
def lmultiple2(l):
    a = []
    for m in l:
        a.append(m*3)
    return a    

def mama(m,k):
    if m>k:
        print("ans will be subtraction ",m-k)
    elif m==k:
        print("the answer will be multiplication ",m*k)
    else:
        print("the ans will be addition ",m+k)    
