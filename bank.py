class User:
    def __init__(self):
        self.loan_count = 0
        self.total_loan = 0
        self.my_account = {}

    def Create_account(self, name, email, address, account_type, bank):
        bank.Create_account(name, email, address, account_type)

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

    def Send(self, amount, account_number, another_account, bank):
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

    def Create_account(self, name, email, address, account_type):
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

    def see_all_user(self):
        cc = 0
        for account in self.savings_account.values():
            print(f"{cc}. Account Name: {account['name']}, Account_number: {account['account_number']}, Account type: {account['account_type']}")
            cc += 1

    def check_total_balance(self):
        print(f"Total Bank Balance: {self.bank_balance}")

    def Total_loan(self):
        print(self.total_loan)

    def Loan_off(self):
        pass


bbl = Bank()
siam = User()
siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "savings", bbl)
siam.Create_account("Siam", "siam@gmail.com", "Gaibandha", "current", bbl)
siam.Deposit(5000, '100c', bbl)
siam.Deposit(10000, '100s', bbl)

siam.Withdraw(500, "100s", bbl)
siam.Available_balance("100s", bbl)
siam.Available_balance("100c", bbl)


while True:
    print("\nMain Menu")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        acc_num = int(input("Enter your account number: "))
        if acc_num in bank.accounts:
            user_interface(bank.accounts[acc_num])
        else:
            print("Account does not exist")
    elif choice == '2':
        admin_interface()
    elif choice == '3':
        break
