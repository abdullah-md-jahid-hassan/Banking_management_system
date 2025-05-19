class Banking:
    def __init__(self, user_name, initial_deposit):
        self.name = user_name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! Your new balance is: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")
            
    def get_balance(self):
        print(f"Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is: {self.balance}")
        else:
            print("Withdrawal amount must be greater than 0.")


# Create an account
account1 = Banking(input("Enter your name: "), int(input("Enter your first deposit: ")))

print(f"{account1.name}, welcome to our Bank.")

while True:
    print("\n1 for Deposit.\n2 for Balance Inquiry.\n3 for Withdraw.\n4 for Exit.")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        account1.deposit(amount)
    elif choice == 2:
        account1.get_balance()
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        account1.withdraw(amount)
    elif choice == 4:
        print("Thank you for using our bank. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
