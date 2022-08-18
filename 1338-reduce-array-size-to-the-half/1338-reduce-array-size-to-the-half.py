class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))
        numsToBeRemoved = 0
        l = len(arr)
        for i in freq.values():
            if (l - i) <= len(arr) //2:
                return numsToBeRemoved+1
            numsToBeRemoved += 1
            l-= i
        
            