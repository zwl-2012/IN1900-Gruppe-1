
class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance
    
    
    def transfer(self, new_account, new_amount):
        if new_amount > self.get_balance():
            print("Amount too high, not transferrable!")
        elif new_amount < 0:
            print("Amount is negative,, not transferrable!")
        else:
            self.withdraw(new_amount)
            new_account.deposit(new_amount)
            

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)





print("\n---------- BankAccountP.py ----------\n")
a1 = BankAccountP('John', 'Olsson', '19371554951', 20000)
a2 = BankAccountP('Liz', 'Olsson',  '19371564761', 20000)
#a1.deposit(1000)
#a1.withdraw(4000)
#a2.withdraw(10500)
#a1.withdraw(3500)
#print("a1's balance:", a1.get_balance())


"""Before transfer"""
a1.print_info()
a2.print_info()
a1.transfer(a2, 5000)


"""After transfer"""
a1.print_info()
a2.print_info()