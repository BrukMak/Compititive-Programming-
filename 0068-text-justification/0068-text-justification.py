class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left, right = 0, 0
        left_over = maxWidth
        justified = []
        
        while right < (len(words)):
            # print(left, right)
            if left_over >= len(words[right]):
                left_over -= len(words[right]) + 1
                
            else:
                justified.append(self.justifier(words, left, right, left_over + 1))
                left = right
                right -= 1
                left_over = maxWidth
                
            right += 1
            if right == len(words):
                justified.append(self.justifier(words, left, right, left_over + 1))
        
        return justified
            
    def justifier(self, words, left, right, left_over):
        num_of_words = right - left
        if right == len(words) or num_of_words == 1:
            l = [" "] * left_over
            l_space = "".join(l)
            return " ".join(words[left:right]) + l_space
        space = left_over // (num_of_words - 1)
        extra_space = left_over % (num_of_words - 1)
        
        joiner_space = [" "] * space
        joiner_space = "".join(joiner_space)
        
        res = []
        pointer = left
        while extra_space:
            res.append(words[pointer] + joiner_space + " ")
            extra_space -= 1
            pointer += 1
        while pointer < right:
            if pointer < right -1:
                res.append(words[pointer] + joiner_space)
            else:
                res.append(words[pointer])
            pointer += 1
        
        return " ".join(res)