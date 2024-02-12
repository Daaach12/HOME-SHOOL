def F(x):
    x=str(x)
    y=''
    for i in x:
        y=i+y
    return y
print(F(1234))
def Q(x):
    x=str(x)
    y=''
    for i in range(len(x),0,-1):
        y+=str(i)
    return y
print(Q(12345))
def W(x):
    x=str(x)
    return x[::-1]
print(W(123456))