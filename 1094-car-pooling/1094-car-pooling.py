class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        max_cap = defaultdict(int)
        for trip in trips:
            num_pass, start, end  = trip
            
            for i in range(start, end):
                max_cap[i] += num_pass
        return max(max_cap.values()) <= capacity
                
                