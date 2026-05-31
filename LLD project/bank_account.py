
class Bank_account:
    # constructor
    def __init__(self, acc_num, acc_holder_name, balance, acc_type, is_active):
        self.acc_num = acc_num
        self.acc_holder_name = acc_holder_name
        self.balance = balance
        self.acc_type = acc_type
        self.is_active = is_active

    # deposite method --> deposite money to bank account
    def deposit(self, amount):
        if amount > 0 and self.is_active:
            self.balance += amount
            return f"{amount}.00 credited to your bank. your current balance is {self.balance}"

    # withdraw method ==> for withdrawing money
    def withdraw(self, amount):
        if amount < self.balance and self.is_active:
            self.balance -= amount
            return f"{amount} has been withdrawn from your account. current balance: {self.balance}"

        else:
            return f"your bank does not have enough funds to withdraw {amount} from your account"


    # check account is active or not
    def check_balance(self):
        return f"your current balance is {self.balance}"

    # delete the account
    def deactivate_account(self):
        self.is_active = False
        return f"your account has been deactivated"



account_holder_1 = Bank_account(1, "pulakeh", 42_000, "saving", True)
account_holder_2 = Bank_account(2, "parthib", 34_000, "saving", True)

print(account_holder_1.deposit(100))
