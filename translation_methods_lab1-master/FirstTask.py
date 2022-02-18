from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from CSVHelper import CSVHelper
from Notification import Notification


class FirstTask(MDScreen):
    my_string = ObjectProperty(None)
    language = ObjectProperty(None)
    dialog = None
    note = Notification(dialog)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def next_task(self, *args):
        """
        Функция перехода к следующему заданию
        :param args: передаваемые аргументы
        :return: None
        """
        self.manager.transition.direction = 'left'
        self.manager.current = 'second_task'

    def previous_task(self, *args):
        """
        Функция перехода к предыдущему заданию
        :param args: передаваемые аргументы
        :return: None
        """
        pass

    def load_string(self, *args):
        """
        Функция импорта строки
        :param args: передаваемые аргументы
        :return: None
        """
        ans = CSVHelper().import_str()
        if ans is not None:
            self.my_string.text = ans

    def load_language(self, *args):
        """
        Функция импорта языка
        :param args: передаваемые аргументы
        :return: None
        """
        ans = CSVHelper().import_language()
        if ans is not None:
            self.language.text = ans

    def check(self, *args):
        """
        Функция для проверки принадлежности слова алфавиту
        :param args: передаваемые аргументы
        :return: None
        """
        language = self.language.text.split(',')
        my_string = self.my_string.text
        for symbol in my_string:
            if symbol not in language:
                self.note.universal_note(f'Слово \"{self.my_string.text}\" не принадлежит языку \"{self.language.text}\"', [])
                return False
        self.note.universal_note(f'Слово \"{self.my_string.text}\" принадлежит языку \"{self.language.text}\"', [])

