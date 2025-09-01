# Chapter 2: If Else
class IfElse:
    def __init__(self, wallet):
        self.wallet = wallet
        self.price = 80

    def purchase(self):
        if self.wallet >= self.price:
            self.wallet -= self.price
            print(f"Purchase successful! Remaining wallet balance: {self.wallet}")
        elif self.wallet < 0:
            print("Wallet balance cannot be negative!")
            self.wallet = 0
        else:
            print("Insufficient funds!")
        return self.wallet
