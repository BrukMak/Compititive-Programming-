class WordDictionary:

    def __init__(self):
        self.d = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)
                

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.d[len(word)]
        
        for w in self.d[len(word)]:
            for i, v in enumerate(word):
                if w[i] != v and v != ".":
                    break
            else:
                return True
        return False