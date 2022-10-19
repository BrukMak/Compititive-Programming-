class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Heap sort by first value of a tuple but if the first 
        #value is equal sort by the second one
        frequency = Counter(words)
        freq_word = [(-v, k) for k, v in frequency.items()]
        
        # sort from the largest frequency
        heapq.heapify(freq_word)
        words = []
        for _ in range(k):
            top = heapq.heappop(freq_word)
            words.append(top[1])
        return words
        