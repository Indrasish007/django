class Bank:
    def interest(self):
        print("5% interest")
        
    def rohosso(self):
        print('123456789')
        
class SBI(Bank):
    def interest(self):
        print("7% interest")
    
    def newinterest(self):
        print("125645")
        
b=SBI()
b.interest()

a=Bank()
a.interest()

b.rohosso()

