def trailing_zeroes(n):
    count = 0
    powFive = 5

    while(powFive <= n):
        count += n//powFive
        powFive *= 5

    return count

print(trailing_zeroes(int(input())))