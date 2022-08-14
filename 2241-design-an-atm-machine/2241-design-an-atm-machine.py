class ATM:

    def __init__(self):
        self.index = {
            0:20,
            1:50,
            2:100,
            3:200,
            4:500
        }
        self.remaining = {
            20:0,
            50:0,
            100:0,
            200:0,
            500:0
        }
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,v in enumerate(banknotesCount):
            self.remaining[self.index[i]] += v

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        prevRemaining = self.remaining.copy()
        for i in range(4, -1, -1):
            largest = self.index[i]
            while self.remaining[largest] > 0:
                
                if amount - largest < 0:
                    break
                times = amount // largest
                if self.remaining[largest] >= times:
                    
                    amount -= (largest * times)
                    self.remaining[largest] -= times
                    res[i] += times
                else:
                    amount -= (self.remaining[largest] * largest)
                    res[i] += self.remaining[largest]
                    self.remaining[largest] = 0
                    
                if amount == 0:
                    return res
        self.remaining = prevRemaining
        return [-1]
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)