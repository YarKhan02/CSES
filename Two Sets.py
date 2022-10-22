def two_set(n):
    sum = ((n*(n+1)) // 2)
    if sum % 2 != 0:
        print("NO")
    else:
        sum = sum // 2
        c1 = 0
        c2 = 0
        s1 = set()
        s2 = set()
        for i in range(n, 0, -1):
            if sum >= i:
                s1.add(i)
                sum -= i
                c1 += 1
            else:
                s2.add(i)
                c2 += 1

        print("YES")
        print(c1)
        print(*s1)
        print(c2)
        print(*s2)
    
    return

print(two_set(int(input())))
