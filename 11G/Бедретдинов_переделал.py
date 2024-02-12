
c=int(input())
def cif (k):
    print('в обратную сторону:')
    while k>0:
        b = k % 10
        k //= 10
        print(b)

def obr(q):
    print("по порядку:")
    a = len(str(q))
    while q>0:
        a-=1
        b=q//10**a
        q%=10**a
        print(b)
cif(c)
obr(c)