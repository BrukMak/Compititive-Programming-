class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        prefix = [0]
        postfix = [0]*(N + 1)
        for i in nums:
            prefix.append(prefix[-1] + i)
        for j in range(N-1, -1, -1):
            postfix[j] = postfix[j+1] + nums[j]
        # postfix.reverse()
        # print(prefix, postfix)
        minOp = float('inf')
        for i in range(N+1):
            l, r = i, N
            
            while r >= l:
                mid = l + (r - l) // 2
                curSum = prefix[i] + postfix[mid]
                if curSum == x:
                    minOp = min(minOp, i + N-mid)
                    break
                elif   curSum < x:
                    r = mid - 1
                else:
                    l = mid + 1
        return minOp if minOp < float('inf') else -1
            