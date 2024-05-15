import sys

class BankAccount:
    def __init__(self, acno, holno):
        self.accountholdername = holno
        self.accountnumber = acno
        self.balance = 300001
    

    def display(self):
        print(f"Account holder name: {self.accountholdername}")
        print(f"Account number: {self.accountnumber}")
        print(f"Your balance: {self.balance}")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Amount {amount} is deposited")
        print(f"Balance amount: {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount < self.balance:
            self.balance -= amount
            print(f"Balance amount: {self.balance}")
        else:
            print("Insufficient funds")

def main():
    bank = BankAccount("SBI220303", "GOWTHAMREDDY")

    print("Enter the option you want:")
    print("1. Display user details")
    print("2. Deposit")
    print("3. Withdraw Amount")

    expression = int(input())
    if expression == 1:
        bank.display()
    elif expression == 2:
        bank.deposit()
    elif expression == 3:
        bank.withdraw()
    else:
        print("Invalid input!!")

if __name__ == "__main__":
    main()

