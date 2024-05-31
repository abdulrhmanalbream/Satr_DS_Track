from datetime import datetime

class AR_BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"تم إيداع {amount} ريال لرصيدك البنكي في يوم {datetime.now().strftime('%A')}، {datetime.now().strftime('%d %B %Y')}، الساعة {datetime.now().strftime('%I:%M%p')}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"تم خصم {amount} ريال من رصيدك البنكي في يوم {datetime.now().strftime('%A')}، {datetime.now().strftime('%d %B %Y')}، الساعة {datetime.now().strftime('%I:%M%p')}.")
        else:
            print("لا يوجد رصيد كافي في حسابك.")

    def check_balance(self):
        print(f"رصيدك الحالي هو: {self.balance} ريال.")

class En_BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} SAR to your bank account on {datetime.now().strftime('%A')}, {datetime.now().strftime('%d %B %Y')}, at {datetime.now().strftime('%I:%M%p')}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} SAR from your bank account on {datetime.now().strftime('%A')}, {datetime.now().strftime('%d %B %Y')}, at {datetime.now().strftime('%I:%M%p')}.")
        else:
            print("Insufficient funds in your account.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance} SAR.")


lang = int(input('Enter: \n 1. للغة العربية \n 2. for English \n '))
if lang == 1:
    Ar_user_account = AR_BankAccount() 
    
    while True:
        opreation = int(input("ادخل التالي للعمليات التالية: \n 1. لل إيداع \n 2. لل سحب \n 3. للتحقق من الرصيد"))
        if opreation ==1:
            amount_deposit = int(input("ادخل المبلغ التي تود ان تودعه : "))
            Ar_user_account.deposit(amount_deposit)    
        elif opreation == 2:
            amount_withdraw = int(input("ادخل المبلغ التي تود ان تودعه : "))
            Ar_user_account.withdraw(amount_withdraw)    
        elif opreation == 3:
            Ar_user_account.check_balance()  

        else:
            print("Invalid choice. Please try again.")

elif lang == 2:
    En_user_account = En_BankAccount() 
    
    while True:
        opreation = int(input("Enter the following for the following operations: \n 1. for deposit \n 2. for withdrawal \n 3. to check balance \n "))
        if opreation ==1:
            amount_deposit = int(input("Enter the amount you would like to deposit : "))
            En_user_account.deposit(amount_deposit)    
        elif opreation == 2:
            amount_withdraw = int(input("Enter the amount you wish to deposit : "))
            En_user_account.withdraw(amount_withdraw)    
        elif opreation == 3:
            En_user_account.check_balance()  

        else:
            print("Invalid choice. Please try again.")
else:
    print('Invalid choice. Please try again.')

