class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []  # 初始化一个空列表来存储交易记录

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))  # 记录存款交易
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.transactions.append(('withdraw', amount, 'Insufficient funds'))  # 记录失败的取款交易
            return 'Insufficient funds'
        self.balance -= amount
        self.transactions.append(('withdraw', amount))  # 记录取款交易
        return self.balance
