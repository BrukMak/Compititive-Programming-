class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s_arr = list(s)
        answer = []
        self.backTrack(s_arr, 0, answer)
        return answer
    def backTrack(self, s_arr, index, answer):
        if index == len(s_arr):
            answer.append("".join(s_arr))
            return
        self.backTrack(s_arr, index + 1, answer)
        if not s_arr[index].isdigit():
            if s_arr[index].islower():
                s_arr[index] = s_arr[index].upper()
                self.backTrack(s_arr, index + 1, answer)
                s_arr[index] = s_arr[index].lower()
            else:
                s_arr[index] = s_arr[index].lower()
                self.backTrack(s_arr, index + 1, answer)
                s_arr[index] = s_arr[index].upper()
    
        