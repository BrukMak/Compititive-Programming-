class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        idx_dict = defaultdict(list)
        
        
        # Make a dictionary containing all the index for the occurrence of each char
        for i in range(len(s)):
            idx_dict[s[i]].append(i)
            
        # Make 2d list using the indices from the dictionary
        intervals = list(idx_dict.values())
        
        ptr = 0
        while ptr < len(intervals):
            s = intervals[ptr][0]
            e = intervals[ptr][-1]
            
            while True:
                ptr += 1
                if ptr < len(intervals) and e > intervals[ptr][-1]:
                    continue
                else:
                    if  ptr < len(intervals) and e > intervals[ptr][0]:
                        e = intervals[ptr][-1]
                    else:
                        ans.append(e - s + 1)
                        break
        return ans
                    
            
            