#1
a=int(input())
b=int(input())
def NOD(a,b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return NOD ( a % b, b )
    else:
        return NOD ( a, b % a )
print(NOD(a,b))
#2
w=int(input('число для простых множетелей: '))
def func(q):
    def prost(c,k):
        if k > 1:
            for i in range(2, k):
                if (k % i) == 0:
                    return False
                    break
            else:
                return k
        else:
            return prost(c+1,w)
    def mnoz(k):
        if k==0 or k==1: return
        elif k<0: return print('error')
        else:
            if k%2==0:
                return
                print(2)
                mnoz(k/2)
            elif k%3==0:
                return
                print(3)
                mnoz(k/3)
            elif k%5==0:
                return
                print(5)
                mnoz(k/5)
