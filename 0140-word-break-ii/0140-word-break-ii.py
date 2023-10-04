class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True
    
    def dfs(self, l, r, node, s, currAns, output):
        
        if r == len(s):
            if node.isEnd:
            
                currAns.append(s[l:r])
                output.append(" ".join(currAns))
                currAns.pop()
            return
        
        if node.isEnd:
            currAns.append(s[l:r])
            self.dfs(r, r, self.root, s, currAns, output)
            currAns.pop()
            
        if r < len(s) and s[r] in node.children:
            self.dfs(l, r+1, node.children[s[r]], s,currAns, output)
        
        
            
    def findAns(self, s):
        output = []
        self.dfs(0,0, self.root, s, [], output)
        return output
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)
        result = trie.findAns(s)
        return result
        
                