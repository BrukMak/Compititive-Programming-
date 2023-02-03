import random
class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(w[i] + self.prefix[i-1])
        
    def pickIndex(self) -> int:
        random_no = random.randint(1, self.total)
        left, right = 0, len(self.prefix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.prefix[mid] == random_no:
                return mid
            elif self.prefix[mid] < random_no:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()