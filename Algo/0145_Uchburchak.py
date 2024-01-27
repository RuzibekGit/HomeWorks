def f(nums):
    a, b, c = nums

    return a + b + c if a + b > c and a + c > b and b + c > a else -1
    

res = []
n = int(input())
nums = sorted(map(int, input().split()), reverse=True)

for i in range(3, n+1):
    res.append(f(nums[i-3: i]))

print(*sorted(nums[:3]))
