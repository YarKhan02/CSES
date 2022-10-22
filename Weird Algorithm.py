def weird_algorithm(n):

    while n != 1:
        
        if n == 1:
            return n
            
        elif n % 2 == 0:
            print(n, end = ' ')
            n = n // 2
            
        elif n % 2 != 0:
            print(n, end = ' ')
            n = (n * 3) + 1

    return n

print(weird_algorithm(int(input())))