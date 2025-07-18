class Zanachka:
    def __init__(self):
        self.__count = 0

    def view_cash(self):
        return self.__count
    
    def add_cash(self, add_to_cash):
        if add_to_cash >= 0:
            self.__count += add_to_cash

    def withdraw_cash(self, withdraw_to_cash):
        if self.__count >= withdraw_to_cash:
            self.__count -= withdraw_to_cash
        else:
            print("В заначке недостаточно средств")


odissey = Zanachka()
print(odissey.view_cash())

odissey.add_cash(50_000)
print(odissey.view_cash())

odissey.withdraw_cash(1000)
print(odissey.view_cash())

odissey.withdraw_cash(60000)
print(odissey.view_cash())

odissey.__count = 1_000_000
print(odissey.view_cash())

odissey.withdraw_cash(-50_000)
print(odissey.view_cash())