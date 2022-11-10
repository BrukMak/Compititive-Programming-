class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.backTrack("", s, [], answer)
        return answer
    def backTrack(self, cur, s, cur_ds, answer):
        if s == "":
            answer.append(cur_ds[:])
            return
        for i in range(1, len(s)+1):
            candidate = s[:i]
            if candidate == candidate[::-1]:
                cur_ds.append(candidate)
                cur = candidate
                s = s[i:]
                self.backTrack(cur, s, cur_ds, answer)
                cur_ds.pop()
                cur = ""
                s = candidate + s
        