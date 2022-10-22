n = int(input())

for i in range(1, n + 1):
    result = (i * i * ((i * i) - 1)) - 8 - 24 - 16 * (i - 4) - 16 - 24 * (i - 4) - (i - 4)**2 * 8
    print(result//2)