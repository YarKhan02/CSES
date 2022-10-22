def missing_numbers(n: int):

    nums = [int(x) for x in input().split()]
    sum1 = sum(nums)

    return int(n * (n + 1) / 2 - sum1)

print(missing_numbers(int(input())))