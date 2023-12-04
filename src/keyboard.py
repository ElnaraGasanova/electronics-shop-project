from src.item import Item


class MixinLanguage:
    '''Класс-миксин, добавляет функционал
    по изменению раскладки клавиатуры, где
    по умолчанию - раскладка "EN" '''
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        '''Функция для изменения раскладки клавиатуры'''
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self
        if self.__language.upper() == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    '''Класс Keyboard, наследуемый от MixinLanguage и Item'''
    pass

