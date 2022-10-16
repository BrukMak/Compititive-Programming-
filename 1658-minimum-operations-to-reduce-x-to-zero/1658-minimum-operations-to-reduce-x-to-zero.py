class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        prefix = [0]
        postfix = defaultdict(int)
        postfix[0] = N
        for i in nums:
            prefix.append(prefix[-1] + i)
        post = 0
        for j in range(N-1, -1, -1):
            post += nums[j]
            postfix[post] = j
        minOp = float('inf')
        for i in range(N+1):
            cur = x - prefix[i]
            if cur in postfix:
                index_from_back = postfix[cur]
                if index_from_back >= i:
                    minOp = min(minOp, i + (N - index_from_back))
                    
        return minOp if minOp < float('inf') else -1
    
    """
    Creating prefix sum list ad postfix hash table for fast look up 
        Trying to find the target as a combination of the prefix and 
            find candidate from the hash table
        Time O(n)
        Space O(n)
    """
            