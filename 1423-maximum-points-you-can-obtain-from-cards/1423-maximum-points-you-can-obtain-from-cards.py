class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = right_sum = 0
        for i in range(k):
            left_sum += cardPoints[i]
        max_sum = left_sum
        
        for i in range(k):
            left_sum -= cardPoints[k - 1 - i]
            right_sum += cardPoints[len(cardPoints) - 1 - i]
            
            max_sum = max(max_sum, left_sum + right_sum)
        
        return max_sum