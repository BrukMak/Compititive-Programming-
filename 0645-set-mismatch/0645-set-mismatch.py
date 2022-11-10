class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        running_xor = nums[0]
        for i in range(1, len(nums)):
            running_xor ^= nums[i]
            if not running_xor:
                ans.append(nums[i])
                break
            running_xor ^= nums[i-1]
        diff = []
        for i in range(len(nums)):
            if (nums[i] ^ (i + 1))  != 0:
                diff.append((nums[i] , (i + 1)))
        if len(diff) > 1:
            can1, can2 = diff[0], diff[-1]
            if ans[0] == can1[0]:
                ans.append(can2[1])
            else:
                ans.append(can1[1])
        else:
            ans.append(diff[0][1])
        return ans