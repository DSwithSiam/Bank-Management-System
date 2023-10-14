class Bank():
    def __init__(self) -> None:
        self.savings_account = {}
        self.current_account = {}
        self.bank_balance = 0
        self.total_loan = 0
        self.all_user = 0
        
        
    def Create_account(self, name, email, address, account_type):
        if account_type == "savings" or account_type == "Savings" :
            account_number = str((len(self.savings_account) + 100)) + "s"
            self.savings_account[account_number] = {"name": name, "email": email, "address": address, "account_type": account_type, "balance": 0, "transaction_history": []}
            print(f"Your bank account number is {account_number}")
        else:
            account_number = str((len(self.current_account) + 100)) + "c"
            self.current_account[account_number] = {"name": name, "email": email, "address": address, "account_type": account_type, "balance": 0, "transaction_history": []}
            print(f"Your bank account number is {account_number}")
            
    def Delete_user_account(self, account_number):
        try:
            if "c" in account_number:
                self.current_account.pop("account_number")
                print(f"Your bank account has been deleted")
            else:
                self.savings_account.pop("account_number")
                print(f"Your bank account has been deleted")
        except:
            print("Wrong account number")
            
            
            
    def Deposit(self, tk, account_number):
        try:
            if "c" in account_number:
                self.current_account[account_number]["balance"] += tk
                self.current_account[account_number]["transaction_history"].append(f"Deposit : {tk} tk. ")
            else:
                self.savings_account[account_number]["balance"] += tk
                self.savings_account[account_number]["transaction_history"].append(f"Deposit : {tk} tk. ")
        except:
            print("Wrong account number")
        
    def Withdraw(self, tk, account_number):
        try:
            if "c" in account_number:
                if self.current_account[account_number]["balance"] >= tk:
                    self.current_account[account_number]["balance"] -= tk
                    self.current_account[account_number]["transaction_history"].append(f"withdraw : {tk} tk. ")
                else: 
                    print("Withdrawal amount exceeded")
            else:
                if self.savings_account[account_number]["balance"] >= tk:
                    self.savings_account[account_number]["balance"] -= tk
                    self.savings_account[account_number]["transaction_history"].append(f"withdraw : {tk} tk. ")
                else:
                    print("Withdrawal amount exceeded")
        except:
            print("Wrong account number")
    
    def Available_balance(self, account_number):
        try:
            if "c" in account_number:
                print (self.current_account[account_number]["balance"])
            else:
                print (self.savings_account[account_number]["balance"])
        except:
            print ("Wrong account number")    
        
    def Transaction_history(self, account_number):
        try:
            if "c" in account_number:
                print (self.current_account[account_number]["transaction_history"])
            else:
                print (self.savings_account[account_number]["transaction_history"])
        except:
            print("Wrong account number")
    
    
    
siam = Bank()
siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "savings")
siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "current")
siam.Deposit(5000, '100c')
siam.Deposit(10000, '100s')

siam.Withdraw(500, "100s")
siam.Available_balance("100s")
siam.Available_balance("100c")