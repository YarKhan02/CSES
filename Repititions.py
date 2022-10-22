def repititions(n: list):

    max = 0
    count = 0
    
    for i in range(len(n) - 1):

        if n[i] == n[i + 1]:
            count += 1

            if max <= count:
                max = count

        elif n[i] != n[i + 1]:
            count = 0

    return max + 1

print(repititions(list(input())))