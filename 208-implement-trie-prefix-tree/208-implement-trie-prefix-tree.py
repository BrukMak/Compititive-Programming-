class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.is_word = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.is_word = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.nodes:
                return False
            cur = cur.nodes[ch]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)