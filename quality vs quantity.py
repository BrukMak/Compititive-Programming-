import sys
sys.stdin.readline

def inp_arr():
    return list(map(int, input().split()))
def inp_int():
    return int(input())
test = inp_int()
for i in range(test):
    n = inp_int()
    nums = inp_arr()
    nums.sort()
    red = 0
    blue = nums[0]
    left = 1
    right = n - 1
    found = False
    while left < right:
        blue += nums[left]
        red += nums[right]
        if red > blue:
            found = True
            break
        left += 1
        right -= 1
    if found:
        print("YES")
    else: print("NO")
    
