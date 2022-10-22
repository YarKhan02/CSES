n = int(input())
nums = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    x = nums[i][0]
    y = nums[i][1]
    
    if y > x:
        if y % 2 == 1:
            print((y * y) - x + 1)
        else:
            y -= 1
            print((y * y) + x)
                
    else:
        if x % 2 == 0:
            print((x * x) - y + 1)
        else:
            x -= 1
            print((x * x) + y)