from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        '''Создан новый класс `Phone` с атрибутами класса Item
        и доп.атрибутом - кол-во поддерживаемых сим-карт'''

        # РАСШИРЯЕМ функц-л через super() - вызовом __init__ родит.класса
        super().__init__(name, price, quantity)
        # иниц-ем новую иниц-цию number_of_sim
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        """"Метод реализации оператора сложения экземпляров класса
        `Phone` и `Item` по количеству товара в магазине."""
        if not isinstance(other, Item):
            raise ValueError("Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.")
        return self.quantity + other.quantity

    def chek_number_of_sim(self, number_of_sim):
        """Проверка количества сим-карт"""
        self.number_of_sim = number_of_sim
        if number_of_sim <= 0:
            print(f'ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        return self.number_of_sim


    # @classmethod
    # def chek_number_of_sim(self, number_of_sim):
    #     """Проверка количества сим-карт"""
    #     if type(number_of_sim) != int or number_of_sim <= 0:
    #         raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля.')
    #
    # @property
    # def num_of_sim(self):
    #     return self.num_of_sim
    #
    # @num_of_sim.setter
    # def num_of_sim(self, number_of_sim):
    #     self.chek_number_of_sim(number_of_sim)
    #     self.num_of_sim = number_of_sim