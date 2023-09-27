class bank_card:
    def __init__(self,card_number,name,cvv,balance = 0):
        self.card_number = card_number
        self.name = name
        self.cvv = cvv
        self.balance = balance
    def add_balance(self,count):
        self.balance += count
    def withdraw(self,count):
        if self.balance < count:
            print("Недостаточно средств")
            return
        else:
            self.balance -= count
    def my_balance(self):
        return (f'На карте № {self.card_number} : {self.balance} рублей')
    def card_data(self):
        return (f'Ваша карта № {self.card_number} на имя {self.name}, имеет баланс {self.balance} рублей')
    pass

my_card = bank_card(12315,"Dmitrii",111)
my_card_2 = bank_card(12316,"Igor Nikolaevich",131,5000)
my_card.add_balance(200)
my_card.withdraw(123)
print(my_card.my_balance())
print(my_card_2.my_balance())
print(my_card_2.card_data())

class bank:

    def __init__(self):
        self.account_list = []
    
    def add_account(self,account):
        if isinstance(account,bank_card):
            self.account_list.append(account)
            print("Счет успешно создан")
        else:
            print("Некоректный номер счета")
            return
    pass
my_bank = bank()
my_bank.add_account(my_card)
my_bank.add_account(my_card_2),
for i in my_bank.account_list:
    print (f'{i.name} - {i.balance} рублей')
