class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        special_Digit = {
            0:"",
            1:"Thousand",
            2:"Million",
            3:"Billion"
            
        }
        
        below_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        below_hundred = ["","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
                        
        def threeDigit(num):
            if num < 20:
                return [below_twenty[num]]
            if num < 100:
                return [below_hundred[num//10]] + threeDigit(num % 10)
            if num < 1000:
                first_d, rest = num // 100, num % 100
                return [below_twenty[first_d], "Hundred"] + threeDigit(rest)
                        
                        
        ans = ""
        
        bil = num // 1000000000
        num %= 1000000000
        mil = num // 1000000
        num %= 1000000
        tous = num // 1000
        num %= 1000
        if bil:
            ans += (" ".join(threeDigit(bil))).strip()
            ans += (' Billion ')
        if mil:
            ans += (" ".join(threeDigit(mil))).strip()
            ans += (' Million ')
        if tous:
            ans += (" ".join(threeDigit(tous))).strip()
            ans += (' Thousand ')
        ans += (" ".join(threeDigit(num))).strip()
            
        return ans.strip()