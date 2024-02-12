# # №39
# # Ходы +2*2
# # Выигрыш 25
#
# def F(s,c,m):
#     if s>=25: return c%2==m%2
#     if c==m: return 0
#     h=[F(s+2,c+1,m), F(s*2,c+1,m)]
#     return any(h) if (c+1)%2==m%2 else all(h)
#
#
# for s in range(1,24+1):
#     for m in range(1,5):
#         if F(s,0,m):
#             if m==4: print(m,s)
#             break




# # №40
# # Ходы +3*2
# # Выигрыш 33
#
# def F(s,c,m):
#     if s>=33: return c%2==m%2
#     if c==m: return 0
#     h=[F(s+3,c+1,m),F(s*2,c+1,m)]
#     return any(h) if (c+1)%2==m%2 else all(h)
# for s in range (1,34):
#     for m in range(1,5):
#         if F(s,0,m):
#             if m==4:print(m,s)
#             break


#43
def F(s,c,m):
    if s>=34: return c%2==m%2
    if c==m: return 0
    h=[F(s+1,c+1,m),F(s+2,c+1,m),F(s+3,c+1,m),F(s*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for s in range(1,34):
    for m in range(1,5):
        if F(s,0,m):
            if m==4: print(m,s)
            break
#16/8,13/12

















