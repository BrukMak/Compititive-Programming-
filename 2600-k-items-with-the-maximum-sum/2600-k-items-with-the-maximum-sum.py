class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans += k
            k = 0
        elif k > numOnes:
            ans += numOnes
            k -= numOnes
        if k <= numZeros:
            k = 0
        elif k > numZeros:
            k -= numZeros
        if k <= numNegOnes:
            ans -= k
            k = 0
        elif k > numNegOnes:
            ans -= numNegOnes
            k -= numNegOnes
            
        return ans
        
            