mod = 1000000007
def bit_strings(n):
    x = 1
    for i in range(0, n):
        x = (x * 2) % mod

    return x

print(bit_strings(int(input())))
