class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort()
        ans = 0
        count = 0
        for i in range(n-1, -1, -1):
            ans += max(happiness[i] - count, 0)
            count += 1
            k -= 1
            if not k:
                break
        
        return ans
            