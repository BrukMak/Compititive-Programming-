class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        prefix_sum = [0] * 1001
        for trip in trips:
            num_pass, start, end  = trip
            prefix_sum[start] += num_pass
            prefix_sum[end] += -num_pass
            
        max_cap = prefix_sum[0]
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
            max_cap = max(max_cap, prefix_sum[i])
        return max_cap <= capacity
        
            
            
                