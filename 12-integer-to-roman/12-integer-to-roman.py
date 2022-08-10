class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
                0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII","IX"],
                1 : ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
                2: ['' ,'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                3: ["", "M", "MM", "MMM"]
        }
        res = []
        num = str(num)
        for i in range(len(num)):
            res.append(romans[i][int(num[-(i+1)])])
        return "".join(res[::-1])
            