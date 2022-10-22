def permutation(n: list):

    if n == 1:
        return n
    elif n < 4:
        return 'NO SOLUTION'
    else:
        for i in range(2, n + 1, 2):
            print(i, end = ' ')
            
        for i in range(1, n + 1, 2):
            print(i, end = ' ')

    return 
    
print(permutation(int(input())))