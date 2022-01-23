import datetime
import pytz

#  One little Note here: With encapsulation, I can change the method implementation keeping the method signature
# intact, so that my existing code will keep running as it is.


# 1. 1st draft is coming up with a basic bank account with a opening balance, deposit and withdraw method
# 2. At the 2nd go, trying to create a list of transactions
# 3. then adding a static method, transaction_list is going to be used by deposit , withdrawal or any
# other kind of transaction in future. and you will need current time to timestamp that. So instead of
# writing duplicate code in every transaction method, we can reuse the code by having a static method.
# Why static? because this is a feature(getting the current time when adding to the list at the time of any
# kind of transaction happens) that's not going to be used by
# objects (Bank account holders), only they are going to access them as information via another feature
# as all good people do.


class BankAccount:
    """Simple account class with balance
        Methods:
            1. deposit method helps you deposit and tells you balance after if successful
            2. withdraw method helps you withdraw and tells you balance after if successful
    """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._tran_list = []
        print(f"Account created for {self._name} with a balance of {self._balance}")
        if self._balance > 0:
            self._tran_list.append((BankAccount._current_time(), self._balance))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            # self.tran_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._tran_list.append((BankAccount._current_time(), amount))
        else:
            print('deposit amount should be greater than zero')

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.show_balance()
            self._tran_list.append((BankAccount._current_time(), -amount))
        else:
            print('Please try withdrawing again with correct withdrawal amount')

    def show_balance(self):
        print(f"{self._name}'s balance is {self._balance}")

    def show_transaction(self):
        for date, amount in self._tran_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print(f"{amount} {tran_type} on {date.astimezone()}")
            # astimezone() method comes from pytz


if __name__ == '__main__':
    person1 = BankAccount('PseudoFunc', 200)
    person1.deposit(200)
    person1.withdraw(100)
    person1.show_transaction()

