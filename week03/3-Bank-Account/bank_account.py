class BankAccount:

    def __init__(self, name, balance, currency):
        self.acc_name = name
        self.acc_balance = balance
        self.acc_currency = currency
        self.acc_history = ['Account was created']

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.acc_name, self.acc_balance, self.acc_currency)

    def __int__(self):
        self.acc_history.append('__int__ check -> {}{}'.format(self.acc_balance, self.acc_currency))
        return int(self.acc_balance)

    def deposit(self, amount):
        self.acc_history.append('Deposited {}{}'.format(amount, self.acc_currency))
        self.acc_balance += amount

    def balance(self):
        self.acc_history.append('Balance check -> {}{}'.format(self.acc_balance, self.acc_currency))
        return self.acc_balance

    def withdraw(self, amount):
        if self.acc_balance > amount:
            self.acc_balance -= amount
            self.acc_history.append('{}{} was withdrawed'.format(amount, self.acc_currency))
            return True
        else:
            self.acc_history.append('Withdraw for {}{} failed'.format(amount, self.acc_currency))
            return False

    def __eq__(self, other):
        return self.acc_currency == other.acc_currency

    def __hash__(self):
        return hash(self.acc_currency)

    def transfer_to(self, other, amount):
        if self == other:
            if self.acc_balance > amount:
                self.withdraw(amount)
                other.deposit(amount)
                self.acc_history.pop()
                other.acc_history.pop()
                self.acc_history.append('Transfer to {} for {}{}'.format(other.acc_name, amount, self.acc_currency))
                other.acc_history.append('Transfer from {} for {}{}'.format(self.acc_name, amount, self.acc_currency))
                return True
            else:
                return False
        else:
            return False

    def history(self):
        return self.acc_history
