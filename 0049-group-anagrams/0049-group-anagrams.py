class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            curWord = [*word]
            curWord.sort()
            sorted_word = "".join(curWord)
            group[sorted_word].append(word)
        answer = []
        for val in group.values():
            answer.append(val)
        answer.sort()
        return answer
            
                