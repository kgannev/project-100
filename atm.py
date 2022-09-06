class Atm:
    def_init_(self,cardno, pin):
        self.cardno = cardno
        self.pin = pin
        
    def checkbalance(self):
        print("your balance is 50000")

    def withdrawal(self,amount):
        newbalance =50000-amount 
        print("you have withdraw amount"+amount)
        print("you remaining balance"+new balance)

