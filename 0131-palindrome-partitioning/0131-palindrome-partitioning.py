class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.backTrack(0, s, [], answer)
        return answer
    def backTrack(self, index, s, cur_ds, answer):
        if index >= len(s):
            answer.append(cur_ds[:])
            return
        for i in range(index, len(s)+1):
            candidate = s[index:i]
            if len(candidate) > 0 and candidate == candidate[::-1]:
                cur_ds.append(candidate)
                self.backTrack(i, s, cur_ds, answer)
                cur_ds.pop()
                