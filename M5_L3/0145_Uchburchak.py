
def f(nums):
    nums.sort(reverse=True)

    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return [nums[i+2], nums[i+1], nums[i]]

    return -1


n = int(input())
nums = list(map(int, input().split()))

if (res := f(nums)) != -1:
    print(*res)
else: print(-1)



# def f(nums):
#     a, b, c = nums

#     return a + b + c if a + b > c and a + c > b and b + c > a else -1
    

# res = []
# n = int(input())
# nums = sorted(map(int, input().split()), reverse=True)

# for i in range(3, n+1):
#     res.append(f(nums[i-3: i]))

# print(*sorted(nums[:3]))
