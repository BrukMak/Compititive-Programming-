class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        if n == 1: return n
        minHeap = [(val, i) for i, val in enumerate(ratings)]
        heapq.heapify(minHeap)
        resArr = [float('inf')] * n
        
        while minHeap:
            val, i = heapq.heappop(minHeap)
            if i > 0 and i < n-1:
                if resArr[i-1] == float('inf') and resArr[i+1] == float('inf'):
                    resArr[i] = 1
                elif resArr[i-1] != float('inf') and resArr[i+1] != float('inf'):
                    if ratings[i-1] == val and ratings[i+1] == val:
                        resArr[i] = 1
                    elif ratings[i-1] == val:
                        resArr[i] = resArr[i+1] + 1
                    elif ratings[i+1] == val:
                        resArr[i] = resArr[i-1] + 1
                    else:
                        resArr[i] = max(resArr[i-1], resArr[i+1]) + 1
                elif  resArr[i-1] != float('inf'):
                    if ratings[i-1] == val:
                        resArr[i] = 1
                    else:
                        resArr[i] = resArr[i-1] + 1
                
                elif resArr[i+1] != float('inf'):
                    if ratings[i+1] == val:
                        resArr[i] = 1
                    else:
                        resArr[i] = resArr[i+1] + 1
            elif i == 0 and i < n-1:
                if resArr[i+1] == float('inf'):
                    resArr[i] = 1
                elif resArr[i+1] != float('inf'):
                    if ratings[i+1] == val:
                        resArr[i] = 1
                    else:
                        resArr[i] = resArr[i+1] + 1
                    
            elif i == n-1 and i > 0: 
                if resArr[i-1] == float('inf'):
                    resArr[i] = 1
                elif resArr[i-1] != float('inf'):
                    if ratings[i-1] == val:
                        resArr[i] = 1
                    else:
                        resArr[i] = resArr[i-1] + 1
        # print(resArr)
        return sum(resArr)
                        
                        
                        
                        
                