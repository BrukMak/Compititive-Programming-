class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        self.endCount = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True  
        cur.endCount += 1      
        
    def search(self, indexLookUp):
        count = [0]
        self.dfs(-1, self.root, indexLookUp, count)
        return (count)
            
    def dfs(self, index, node, indexLookUp, count):
        for curNode in node.children:
            if curNode in indexLookUp:
                indexArr = indexLookUp[curNode]
                idx = bisect.bisect(indexArr, index)
                if idx < len(indexArr):
                    # print(indexArr[idx], index)
                    if node.children[curNode].isEnd:
                        count[0] += node.children[curNode].endCount
                    self.dfs(indexArr[idx], node.children[curNode], indexLookUp, count)
                        
        
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)

        indexLookUp = defaultdict(list)
        for i, c in enumerate(s):
            indexLookUp[c].append(i)
        # print(indexLookUp)
        return trie.search(indexLookUp)[0]
        