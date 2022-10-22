def increasing_array(n: int):

    nums = [int(x) for x in input().split()]

    x = 0 
    count = 0

    while x < len(nums) - 1:

        if nums[x + 1] >= nums[x]:
            x += 1
                
        elif nums[x + 1] <= nums[x]:
                
            original = nums[x + 1]

            nums[x + 1] = nums[x]

            differnece = nums[x + 1] - original

            count += differnece

            x += 1

    return count


print(increasing_array(int(input())))