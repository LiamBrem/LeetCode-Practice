class Bank:

    def __init__(self, balance: List[int]):
        self.balances = {}
        self.n = len(balance)

        for i in range(len(balance)):
            self.balances[1 + i] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False

        if self.balances[account1] < money:
            return False

        self.balances[account1] -= money
        self.balances[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False
        
        self.balances[account] += money 
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False

        if self.balances[account] < money:
            return False

        self.balances[account] -= money
        return True
        

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)