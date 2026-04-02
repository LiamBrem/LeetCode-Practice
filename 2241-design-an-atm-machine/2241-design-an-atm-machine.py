class ATM:

    def __init__(self):
        self.quantities = [0] * 5
        self.vals = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.quantities[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        temp = self.quantities[:]

        for i in range(len(self.vals) -1, -1, -1):
            res = [0] * 5
            for i in range(4, -1, -1):
                take = min(temp[i], amount // self.vals[i])
                res[i] = take
                amount -= take * self.vals[i]
                temp[i] -= take

        
            if amount == 0:
                for i in range(5):
                    self.quantities[i] -= res[i]
                return res
    
        return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)