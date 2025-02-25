class User:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.balance = 0.0
        self.transaction_history = []
        self.savings_goal = 0.0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            return True
        return False

    def set_savings_goal(self, goal):
        self.savings_goal = goal

    def check_balance(self):
        return self.balance

    def show_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def create_user(self, username, pin):
        if username not in self.users:
            self.users[username] = User(username, pin)
            print(f"User  {username} created successfully.")
        else:
            print("Username already exists.")

    def login(self, username, pin):
        if username in self.users and self.users[username].pin == pin:
            self.current_user = self.users[username]
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or PIN.")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Set Savings Goal")
        print("5. Transaction History")
        print("6. Logout")

    def run(self):
        while True:
            action = input("Do you want to (1) Create User or (2) Login? ")
            if action == '1':
                username = input("Enter username: ")
                pin = input("Enter PIN: ")
                self.create_user(username, pin)
            elif action == '2':
                username = input("Enter username: ")
                pin = input("Enter PIN: ")
                self.login(username, pin)
                if self.current_user:
                    while True:
                        self.display_menu()
                        choice = input("Select an option (1-6): ")
                        if choice == '1':
                            print(f"Your current balance is: ${self.current_user.check_balance():.2f}")
                        elif choice == '2':
                            amount = float(input("Enter amount to deposit: $"))
                            if amount > 0:
                                self.current_user.deposit(amount)
                                print(f"${amount:.2f} deposited successfully.")
                            else:
                                print("Invalid deposit amount.")
                        elif choice == '3':
                            amount = float(input("Enter amount to withdraw: $"))
                            if self.current_user.withdraw(amount):
                                print(f"${amount:.2f} withdrawn successfully.")
                            else:
                                print("Insufficient funds or invalid amount.")
                        elif choice == '4':
                            goal = float(input("Enter your savings goal: $"))
                            self.current_user.set_savings_goal(goal)
                            print(f"Savings goal set to: ${goal:.2f}")
                        elif choice == '5':
                            print("\nTransaction History:")
                            for transaction in self.current_user.show_transaction_history():
                                print(transaction)
                        elif choice == '6':
                            print("Logging out...")
                            self.current_user = None
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")
            else:
                print("Invalid action. Please select 1 or 2.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()