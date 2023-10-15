class User:
    def __init__(self):
        self.loan_count = 0
        self.total_loan = 0
        self.my_account = {}

    def Create_account(self, name, email, address, account_type, bank):
        bank.Create_User_account(name, email, address, account_type)

    def Deposit(self, amount, account_number, bank):
        bank.Deposit(amount, account_number)

    def Withdraw(self, amount, account_number, bank):
        bank.Withdraw(amount, account_number)

    def Available_balance(self, account_number, bank):
        bank.Available_balance(account_number)

    def Transaction_history(self, account_number, bank):
        bank.Transaction_history(account_number)

    def Loan(self, amount, name, bank):
        if not bank.Loan_off_on:
            print("Loan OFF")
        else:
            if self.total_loan < 2:
                if name in bank.all_users_name:
                    bank.Loan(amount, name)
                    bank.total_loan += amount
                    self.total_loan += amount
                    self.loan_count += 1
                else:
                    print("Invalid bank account name.")
            else:
                print("You have borrowed twice and can't borrow anymore.")

    def Transfer_amount(self, amount, account_number, another_account, bank):
        if account_number in bank.all_users_name and another_account in bank.all_users_name:
            if 'ç' in account_number and 'c' in another_account:
                if bank.current_account[account_number]["balance"] >= amount:
                    bank.current_account[account_number]["balance"] -= amount
                    bank.current_account[another_account]["balance"] += amount
                else:
                    print ("Send amount exceeded.")
            elif 's' in account_number and 's' in another_account:
                if bank.savings_account[account_number]["balance"] >= amount:
                    bank.savings_account[account_number]["balance"] -= amount
                    bank.savings_account[another_account]["balance"] += amount
                else:
                    print ("Send amount exceeded.")
            else:
                print("Send tk to same type of account only")
        else:
            print("Invalid bank account name.")


class Bank:
    def __init__(self):
        self.savings_account = {}
        self.current_account = {}
        self.bank_balance = 0
        self.total_loan = 0
        self.Loan_off_on = True
        self.all_users_name = []
        self.all_admin = {}
    
    def Create_admin_account(self, name, email, password):
        self.all_admin[password] = {"name" : name, "email" : email, "password" : password}
        print(f"Your account has been created.")
    
    def Change_admin_password(self, password, new_password):
        pass

    def Create_User_account(self, name, email, address, account_type):
        if account_type.lower() == "savings":
            account_number = str(len(self.savings_account) + 100) + "s"
            self.savings_account[account_number] = {"name": name, "account_number": account_number, "email": email, "address": address, "account_type": account_type, "balance": 0, "transaction_history": []}
            self.all_users_name.append(name)
            print(f"Your bank account number is {account_number}")
        else:
            account_number = str(len(self.current_account) + 100) + "c"
            self.current_account[account_number] = {"name": name, "account_number": account_number, "email": email, "address": address, "account_type": account_type, "balance": 0, "transaction_history": []}
            self.all_users_name.append(name)
            print(f"Your bank account number is {account_number}")

    def Delete_user_account(self, account_number):
        try:
            if "c" in account_number:
                self.current_account.pop(account_number)
                self.all_users_name.remove(self.current_account[account_number]["name"])
                print(f"Your bank account has been deleted")
            else:
                self.savings_account.pop(account_number)
                self.all_users_name.remove(self.savings_account[account_number]["name"])
                print(f"Your bank account has been deleted")
        except KeyError:
            print("Wrong account number")

    def Deposit(self, amount, account_number):
        try:
            if "c" in account_number:
                self.bank_balance += amount
                self.current_account[account_number]["balance"] += amount
                self.current_account[account_number]["transaction_history"].append(f"Deposit: {amount} tk.")
            else:
                self.bank_balance += amount
                self.savings_account[account_number]["balance"] += amount
                self.savings_account[account_number]["transaction_history"].append(f"Deposit: {amount} tk.")
        except KeyError:
            print("Wrong account number")

    def Withdraw(self, amount, account_number):
        try:
            if "c" in account_number:
                if self.current_account[account_number]["balance"] >= amount:
                    self.bank_balance -= amount
                    self.current_account[account_number]["balance"] -= amount
                    self.current_account[account_number]["transaction_history"].append(f"Withdraw: {amount} tk.")
                else:
                    print("Withdrawal amount exceeded")
            else:
                if self.savings_account[account_number]["balance"] >= amount:
                    self.bank_balance -= amount
                    self.savings_account[account_number]["balance"] -= amount
                    self.savings_account[account_number]["transaction_history"].append(f"Withdraw: {amount} tk.")
                else:
                    print("Withdrawal amount exceeded")
        except KeyError:
            print("Wrong account number")

    def Available_balance(self, account_number):
        try:
            if "c" in account_number:
                print(self.current_account[account_number]["balance"])
            else:
                print(self.savings_account[account_number]["balance"])
        except KeyError:
            print("Wrong account number")

    def Transaction_history(self, account_number):
        try:
            if "c" in account_number:
                print(self.current_account[account_number]["transaction_history"])
            else:
                print(self.savings_account[account_number]["transaction_history"])
        except KeyError:
            print("Wrong account number")

    def See_all_user(self):
        cc = 0
        for account in self.savings_account.values():
            print(f"{cc}. Account Name: {account['name']}, Account_number: {account['account_number']}, Account type: {account['account_type']}")
            cc += 1

    def Check_total_balance(self):
        print(f"Total Bank Balance: {self.bank_balance}")

    def Check_Total_loan(self):
        print(self.total_loan)

    def Loan_off(self):
        self.Loan_off_on = True
    
    def Loan_on(self):
        self.Loan_off_on = False


bbl = Bank()
user = User()

# siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "savings", bbl)
# siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "current", bbl)
# siam.Deposit(5000, '100c', bbl)
# siam.Deposit(10000, '100s', bbl)

# siam.Withdraw(500, "100s", bbl)
# siam.Available_balance("100s", bbl)
# siam.Available_balance("100c", bbl)
bo = True

while True:
    print("""
            1. Login
            2. Create account.
            3. Exit
            """)
    choice = input("Enter your choice: ")

    if choice == '1':
        print("""
                1. User Login.
                2. Admin Login.
                3. Exit
                """)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #user login
            acc_num = input("Enter your account number: ")
            if acc_num in bbl.all_users_name:
                while bool:
                    print("""
                            1. Deposit.
                            2. Withdraw.
                            3. Check balance.
                            4. Loan.
                            5. Transfer amount.
                            6. Exit.
                            """)
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        #Deposit
                        amount = int(input("Enter Deposit amount: "))
                        user.Deposit(amount, acc_num, bbl)
                        
                    elif choice == '2':
                        #Withdraw
                        amount = int(input("Enter withdraw amount: "))
                        user.Withdraw(amount, acc_num, bbl)
                        
                    elif choice == '3':
                        #Check balance
                        user.Available_balance(acc_num, bbl)
                        
                    elif choice == '4':
                        #Loan
                        name = input("Enter your bank account name: ")
                        amount = int(input("Enter loan amount: "))
                        user.Loan(amount, name, bbl)
                        
                    elif choice == '5':
                        #Transfer
                        another_account = input("Receiver account number: ")
                        amount = int(input("Enter amount: "))
                        user.Transfer_amount(amount, acc_num, another_account, bbl)
                        
                    elif choice == '6':
                        bool = False
                
            else:
                print("Account does not exist")
                
                
        elif choice == '2':
            #admin login
            email = input("Enter your email: ")
            pas11 = input("Enter your password: ")
            if bbl.all_admin[pas11]['email'] == email:
                while bool:
                    print("""
                            1. Delete user account.
                            2. See all user account.
                            3. Check total bank balance.
                            4. Check total loan.
                            5. Loan OFF.
                            6. Loan ON.
                            7. Exit.
                            """)
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        #Delete user account
                        account_user = input("User account number: ")
                        bbl.Delete_user_account(account_user)
                        
                    elif choice == '2':
                        #See all user account
                        bbl.See_all_user()
                        
                    elif choice == '3':
                        #Check total bank balance
                        bbl.Check_total_balance()
                        
                    elif choice == '4':
                        #Check total loan
                        bbl.Check_Total_loan()
                        
                    elif choice == '5':
                        #Loan OFF
                        bbl.Loan_off()
                        
                    elif choice == '6':
                        #Loan ON
                        bbl.Loan_on()
                        
                    elif choice == '7':
                        bool = False
                
            else:
                print("Account does not exist")
                break
        elif choice == '3':
            break

    elif choice == '2':
        #create account
        print("""
                1. Create User account.
                2. Create Admin account.
                3. Exit
                """)
        choice = input("Enter your choice: ")
        if choice == '1':
            #Create User account
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Account Type (savings / current): ")
            user.Create_account(name, email, address, account_type, bbl)
            
        elif choice == '2':
            #Create Admin account
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Password: ")
            bbl.Create_admin_account(name, email, password)
        elif choice == '3':
            break

    elif choice == '3':
        break


#  acc_num = int(input("Enter your account number: "))
#         if acc_num in bbl.see_all_user:
#             print("""
#                     1. Deposit.
#                     2. Withdraw.
#                     3. Check balance.
#                     4. Loan.
#                     5. Transfer amount.
#                     """)
#         else:
#             print("Account does not exist")


# if choice == '1':
                    
#                 elif choice == '2':
                    
#                 elif choice == '3':
                    
#                 elif choice == '4':
                    
#                 elif choice == '5':
                    
#                 else:
#                     break