# #94
# #Ходы +2*2
# #Выигрыш 63-74
def F(s1,s2,c,m):
    if s1+s2>= 63 and s1+s2<=74: return c%2==m%2
    if s1+s2>74: return (c+1)%2!=m%2
    if c==m: return 0
    h=[F(s1+2,s2,c+1,m),F(s1,s2+2,c+1,m),F(s1*2,s2,c+1,m),F(s1,s2*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for s2 in range (1,47+1):
    for m in range(1,5):
        if F(15,s2,0,m):
            if m == 2:
                print(m,s2)
            break
# #12
# #2 22
# # 20

# #97
# Ходы +1+3*2
# Выигрыш 55

# def F(s1,c,m):
#     if s1>=55: return c%2==m%2
#     if c==m: return 0
#     h=[F(s1+1,c+1,m),F(s1+3,c+1,m),F(s1*2,c+1,m)]
#     return any(h) if (c+1)%2==m%2 else all(h)
#
# for s1 in range (1,55):
#     for m in range(1,5):
#         if F(s1,0,m):
#             print(m,s1)
#         break
