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

    