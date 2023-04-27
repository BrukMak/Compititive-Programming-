class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Sice we are togling the bulbs, the ones that are toggled odd number of times will remain on
        # To be toggled odd number of times, the number need to have odd number of factors
        # Factors always exist in pairs, so its always even except a number multiplied by it self result
            # the required number. Which shows us it happend if the number is perfect square
        
        # To count perfect square, we just need to know the largeest number whose square is less than or 
            # equal to the number given, which can be easily given by the sqrt(number) floor
            
        return int(sqrt(n))