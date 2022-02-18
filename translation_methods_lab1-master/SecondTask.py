from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from CSVHelper import CSVHelper
from Notification import Notification


class SecondTask(MDScreen):
    my_string = ObjectProperty(None)
    language = ObjectProperty(None)
    outcome = ObjectProperty(None)
    dialog = None
    note = Notification(dialog)

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def clear_fields(self, *args):
        """
        Очащиет окно вывода
        :param args: передаваемые параметры
        :return: None
        """
        self.outcome.text = ''

    def next_task(self, *args):
        """
        Функция перехода к следующему заданию
        :param args: передаваемые параметры
        :return: None
        """
        self.manager.transition.direction = 'left'
        self.manager.current = 'third_task'

    def previous_task(self, *args):
        """
        Функция перехода к предыдущему заданию
        :param args: передаваемые параметры
        :return: None
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'first_task'

    def load_string(self, *args):
        """
        Функция для импорта строки из CSV-файла
        :param args: передаваемые аргументы
        :return: None
        """
        ans = CSVHelper().import_str()
        if ans is not None:
            self.my_string.text = ans

    def load_language(self, *args):
        """
        Функция для импорта языка из CSV-файла
        :param args: передаваемые аргументы
        :return: None
        """
        ans = CSVHelper().import_language()
        if ans is not None:
            self.language.text = ans

    def check(self, *args):
        """
        Функция проверки принадлежности сроки языку
        :param args: передаваемые аргументы
        :return: None
        """
        language = self.language.text.split(',')
        my_string = self.my_string.text
        for symbol in my_string:
            if symbol not in language:
                self.note.universal_note(f'Слово \"{self.my_string.text}\" не принадлежит языку \"{self.language.text}\"', [])
                return False
        return True

    def get_suffixes(self, *args):
        """
        Функция определения и вывода суффиксов
        :param args: передаваемые аргументы
        :return: None
        """
        self.clear_fields()
        if self.check():
            language = self.language.text.split(',')
            my_string = self.my_string.text
            answer = ['  ' * left_index + my_string[left_index:] for left_index in range(len(my_string)) if my_string[left_index:] != my_string and my_string[left_index:] != ""]
            answer = "\n".join(answer)
            self.outcome.text = answer

    def get_prefixes(self, *args):
        """
        Функция определения и вывода префиксов
        :param args: передаваемые аргументы
        :return: None
        """
        self.clear_fields()
        if self.check():
            language = self.language.text.split(',')
            my_string = self.my_string.text
            answer = [my_string[:len(my_string) - right_index] for right_index in range(len(my_string)) if my_string[:len(my_string) - right_index] != my_string and my_string[:len(my_string) - right_index] != ""]
            answer = "\n".join(answer)
            self.outcome.text = answer

    def get_substrings(self, *args):
        """
        Функция определения и вывода подстрок имеющейся строки
        :param args: передаваемые аргументы
        :return: None
        """
        self.clear_fields()
        if self.check():
            language = self.language.text.split(',')
            my_string = self.my_string.text
            answer = ['  ' * left_index + my_string[left_index:left_index + right_index + 1] for left_index in range(len(my_string)) for right_index in range(len(my_string) - left_index) if my_string[left_index:left_index + right_index + 1] != my_string and my_string[left_index:left_index + right_index + 1] != ""]
            answer = "\n".join(answer)
            self.outcome.text = answer
