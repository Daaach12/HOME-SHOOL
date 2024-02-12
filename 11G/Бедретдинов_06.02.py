from random import randint
'''
A=[]
N=20

for i in range (N):
    A.append(randint(1,9))
print(A)
for i in range (0,19,2):
    c=A[i]
    A[i]=A[i+1]
    A[i+1]=c
print(A)
'''

A=[]
N=20
q=0

for i in range (N):
    A.append(randint(0,9))
K=int(input('K='))
M=int(input('M='))
print(A)

for i in range (K,M):
    q+=1
    if q<(M-K)//2:
        c=A[i]
        A[i]=A[M-q]
        A[M-q]=c

print(A)