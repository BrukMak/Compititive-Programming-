class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char] = TrieNode()
            cur = cur.nodes[char]
        cur.is_word = True 
    def search(self, word: str) -> bool:
        
            
        def dfs(idx, root):
            cur = root
            for i in range(idx, len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.nodes.values():

                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in cur.nodes:
                        return False
                    cur = cur.nodes[char]
            return cur.is_word
        #     self.search_memo[word] = dfs(0, self.root)
        # return self.search_memo[word]
        return dfs(0, self.root)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)