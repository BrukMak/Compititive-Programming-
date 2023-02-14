class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        letters = [0] * 26
        for i in range(1, 27): letters[i % 26] = chr(i + 64)

        while columnNumber:
            rem = columnNumber % 26
            res.append(letters[rem])
            columnNumber -= rem if rem else 26
            columnNumber //= 26
            
        return "".join(res[::-1])