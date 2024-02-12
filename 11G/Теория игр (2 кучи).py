def F(s1, s2, c, m):
    if s1 + s2 >= 75: return c % 2 == m % 2
    if c == m: return 0
    h = [F(s1 + 1, s2, c + 1, m), F(s1 * 2, s2, c + 1, m), F(s1, s2 + 1, c + 1, m), F(s1, s2 * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s2 in range(1, 66 + 1):
    for m in range(1, 5):
        if F(8, s2, 0, m):
            if m == 3:
                print(m, s2)
            break