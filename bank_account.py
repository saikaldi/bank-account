class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")
    
    def deposite(self, amount):
        self.balance=self.balance+amount
        print(f"\nDeposite complete. ")
        self.getBalance()
    def viabl_transaction(self, amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viabl_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    