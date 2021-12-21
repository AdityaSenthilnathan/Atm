

class Atm (object):
    def __init__(self, money, cardnum, pin):
        if cardnum == 1 & pin == 1:
            self.cardnum = cardnum
            self.pin = pin
            self.money = money
            self.orignal = money
        else:
            print("wrong inputed cardnum/pin")
            

    def Withdraw(self):
            money = input("money you want to withdraw")
            print(money + " dollars is being witdrawed")
            self.money = self.money - int(money)
            print("Money Transfered!")       

    def PutMoneyIn(self):
            money = input("money you want to put into acccont")
            print(money + " dollars is being put into your account")
            self.money = self.money + int(money)
            print("Money Transfered!")
            

    def MoneyCheck(self):
            print("You have " + str(self.money) + " dollors in your account!")


Atm = Atm(20, 1, 1)
Atm.Withdraw()
Atm.PutMoneyIn()
Atm.MoneyCheck()