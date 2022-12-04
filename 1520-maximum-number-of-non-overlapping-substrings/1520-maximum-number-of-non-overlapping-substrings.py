from heapq import heappush, heappop
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        st_en = {}
        for i, c in enumerate(s):
            if c in st_en:
                st_en[c][1] = i
            else:
                st_en[c] = [i, i]
        vis = set()
        for i, c in enumerate(s):
            if c not in vis:
                start , end = st_en[c]
                if start == i:
                    index = start
                    while index <= end:
                        start = min(start, st_en[s[index]][0])
                        end = max(end, st_en[s[index]][1])
                        index += 1
                    st_en[c] = [start, end]
            vis.add(c)
            
        seen = set()
        answer = []
        # print(st_en)
#         intervals = list(st_en.values())
        
#         for ind, interval in enumerate(intervals):
#             st, en = interval
#             intervals[ind] = [en-st+1, st, en]
#         # intervals.sort()
        end_idx = -1
        st_idx = -1
        for c in s:
            new_s, new_e = st_en[c]
            if new_s > end_idx:
                answer.append(s[new_s: new_e + 1])
                end_idx = new_e
                st_idx = new_s
            elif new_s >= st_idx and new_e <= end_idx:
                answer.pop()
                answer.append(s[new_s: new_e + 1])
                end_idx = new_e
                st_idx = new_s
        return answer
            
            
                