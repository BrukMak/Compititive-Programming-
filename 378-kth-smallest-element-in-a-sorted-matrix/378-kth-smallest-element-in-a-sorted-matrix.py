class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, i, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(m):
            count = 0 # count
            for i in range(N):
                # binary search 
                x = bisect_right(matrix[i], m) #bisect
                count = count + x
            return count
        
        while l<i:
            mid = (l+i) // 2
            
            if less_k(mid) < k:
                l = mid + 1
            else:
                i = mid
        return l 