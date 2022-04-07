class BankAccount:
    """
    The class is an example of using the @property decorator to get getter, setter, deleter properties
    """

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # функция вернет баланс
    # property сделает из функции свойство
    @property
    def my_balance(self):
        print('Get balance')
        return self.__balance

    # функция изменит баланс
    # my_balance.setter сделает свойство из данной функции
    @my_balance.setter
    def my_balance(self, new_balance):
        print('Set balance')
        if not isinstance(new_balance, (int, float)):
            raise ValueError('Its not digit')
        self.__balance = new_balance

    # функция удалит баланс
    # my_balance.deleter сделает свойство из данной функции
    @my_balance.deleter
    def my_balance(self):
        del self.__balance