class ATM(object):
    def __init__(self,cardnumber,pin,balance=0):
        self.cardnumber=cardnumber
        self.pin=pin
        self.balance=balance
    def CashWithDrawal(self,Amount):
        self.Amount=Amount
        self.balance=self.balance-Amount
   
    def BalanceEnquiry(self):
        return self.balance     
    def CashDeposit(self,Amount):
        self.Amount1=Amount
        self.balance=self.balance+self.Amount1
       
student=ATM("Student1",14,1000)
student.balance=1000
widthdraw=int(input("Type the amount you want to withdraw: "))
student.CashWithDrawal(widthdraw)
deposit=int(input("Type the amount you want to deposit: "))
student.CashDeposit(deposit)
print(student.BalanceEnquiry())
