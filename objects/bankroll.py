class bankroll():

    balance: int

    def __init__(self, balance: int):
        self.balance = balance

    def add_to_balance(self, income: int):
        self.balance = self.balance + income

    def remove_from_balance(self, amount: int):
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance