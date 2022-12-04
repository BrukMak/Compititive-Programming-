class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        start_end = {}
        for index, c in enumerate(s):
            if c in start_end:
                start_end[c][1] = index
            else:
                start_end[c] = [index, index]
        index = 0
        visited = set()
        answer = []
        while index < len(s):
            ch = s[index]
            start, end = start_end[ch]
            if ch not in visited:
                i = start
                while i < end:
                    end = max(end, start_end[s[i]][1])
                    visited.add(s[i])
                    i += 1
                    # print(s[i], i)
                answer.append(end - start + 1)
                index = end + 1
                
            # else: 
            #     index += 1
        return answer
                