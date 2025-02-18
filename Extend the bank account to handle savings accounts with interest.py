class Bank():
  
  def __init__(self):
     self.blnc = 0
 
  def showbalance(self):
   
    print(f"the Balance is {self.blnc:.2f} ") #2f for 0.00 (for cents/paisa)

  def deposit(self):
    try:
         
         amount = float(input("enter the deposit amount: \n "))
     
         if amount < 0:
             
             print("deposit cannot be lesser then 0")
             
             return 
         self.blnc += amount 
         print(f"deposit: {amount}") 
                
    except ValueError:
        
        print("Invalid amount")
     


  def widhraw(self):
    amount = float(input("enter the withdrawal amount: \n"))
    try:
        if amount > self.blnc:
            
            print("insuffisient funds")
           
            return 
        
        
        if amount < 0:
            
            print("withdrawal cannot be less than 0")
           
            return 0
        
        self.blnc -= amount
       
        print(f"The withdrawn amount is:  {amount}")
        
            
    except ValueError:
       
        print("Invalid value")
        
  
  
  def main(self):
    
    while True:

    
        print("welcome to Savings: ")
        
        print("1: Show balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: exit")
        

        choice = input("enter he choice: \n")


        if choice == '1':
            self.showbalance()

        elif choice == '2':
            self.deposit()

        elif choice == '3':
           self.widhraw()

        

        elif choice == '4':
           
           print("bye bye")
          
           break

        else:
            
            print("invalid input")
           


   

class Savings(Bank):
   def __init__(self):
      super().__init__()
      self.rate = 0

   def upintrest(self):
      amount = float(input("intrest rate"))
      if self.rate < 0:
        
         print("enter valid number")
         
         return
      
      self.rate = amount
    
      print(f"The Updated Intrest = {amount}")
   
   def calcintrest(self):
      self.blnc += self.blnc*self.rate//100
     
      print(f"The intrest rate is {self.blnc}")
    
   def main(self):     
     while True:

    
        print("Welcome to Savings: ")
        
        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Update Intrest")
        print("5: Intrest rate")
        print("6: exit")
    

        choice = input("Enter the choice: \n")


        if choice == '1':
            self.showbalance()

        elif choice == '2':
            self.deposit()

        elif choice == '3':
           self.widhraw()

        elif choice == '4':
           self.upintrest()

        elif choice == '5':
           self.calcintrest()


        elif choice == '6':
           print("bye bye")
          
           break

        else:
         
            print("invalid input")
         


if __name__ == "__main__":
   type = input("select if it is Savings or Bank \n").lower()
   if type == "savings":
      bank = Savings()
   else:
      bank = Bank()
  
   bank.main()