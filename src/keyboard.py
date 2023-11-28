from src.item import Item


class MixinLanguage:
    '''Класс-миксин, добавляет функционал
    по изменению раскладки клавиатуры, где
    по умолчанию - раскладка "EN" '''
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        '''Функция для изменения раскладки клавиатуры'''
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self


class Keyboard(MixinLanguage, Item):
    '''Класс Keyboard, наследуемый от MixinLanguage и Item'''
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language
        MixinLanguage.__init__(self, name, price, quantity)
        if self.__language.upper() != "EN" and self.__language.upper() != "RU":
            raise ValueError('AttributeError: property "language" of "Keyboard" object has no setter')
