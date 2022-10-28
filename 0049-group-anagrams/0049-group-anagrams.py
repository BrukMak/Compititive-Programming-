class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            group[sorted_word].append(word)
        
        answer = sorted(group.values())
        return answer
            
                