class Trienode:
    def __init__(self):
        self.nodes = defaultdict(Trienode)
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = Trienode()
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = Trienode()
            cur = cur.nodes[char]
    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        t = Trie()
        max_heap = []
        freq_dict = defaultdict(int)
        for word in words:
            if not t.search(word):
                t.insert(word)
            freq_dict[word] += 1
        for key, val in freq_dict.items():
            max_heap.append([-1*val, key])
        heapify(max_heap)
        
        ans = []
        
        for _ in range(k):
            cur = heappop(max_heap)[1]
            ans.append(cur)
        
        return ans
            
                