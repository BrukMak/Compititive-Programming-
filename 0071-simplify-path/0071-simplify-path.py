class Solution:
    def simplifyPath(self, path: str) -> str:
        given = path.split('/')
        answer = []
        for s in given:
            if len(s) > 0:
                if s == '..' and answer:
                    answer.pop()
                elif s == '.' or s == '..':
                    continue
                else:
                    answer.append(s)
        return "/" + "/".join(answer)