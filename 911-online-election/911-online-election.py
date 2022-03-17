class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winner = []
        freq = Counter()
        prev_count = prev_winner = 0
        
        for i in range(len(persons)):
            freq[persons[i]] += 1
            count = freq[persons[i]]
            
            if count >= prev_count:
                prev_winner = persons[i]
                prev_count = count
            self.winner.append(prev_winner)
        
        
                
    def binary_search(self, val):
        l = 0
        r  = len(self.times) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if self.times[mid] == val:
                return mid
            elif self.times[mid] < val:
                l = mid + 1
            else:
                r = mid - 1
        return r
    def q(self, t: int) -> int:
        index = self.binary_search(t)
        
        return self.winner[index]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
