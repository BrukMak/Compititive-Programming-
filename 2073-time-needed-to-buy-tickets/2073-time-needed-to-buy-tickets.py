class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = tickets[k]
        if ans == 1:
            return ans + k
        
        for i in range(len(tickets)):
            if i != k and i < k:
                ans += min(tickets[k], tickets[i])
            elif i != k and i > k:
                ans += min(tickets[k] - 1, tickets[i])
        return ans
