from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from CSVHelper import CSVHelper
from Notification import Notification


class ThirdTask(MDScreen):
    s = ObjectProperty(None)
    s1 = ObjectProperty(None)
    language = ObjectProperty(None)
    dialog = None
    note = Notification(dialog)

    def LCS_RECURSIVE(self, x, y):
        """
        Рекурсивная функция поиска общих символов двух строк
        :param x: строка 1
        :param y: строка 2
        :return: list of symbols
        """
        if len(x) == 0 or len(y) == 0:
            return []
        if x[-1] == y[-1]:
            return self.LCS_RECURSIVE(x[:-1], y[:-1]) + [x[-1]]
        else:
            left = self.LCS_RECURSIVE(x[:-1], y)
            right = self.LCS_RECURSIVE(x, y[:-1])
            return left if len(left) > len(right) else right

    def check_s1_is_subsequence_of_s(self, *args):
        """
        Функция проверки того, что строка s1 является подпоследовательностью строки s
        :param args: входные аргументы
        :return: bool
        """
        string_s1 = self.s1.text
        string_s = self.s.text
        ans = self.LCS_RECURSIVE(string_s, string_s1)
        if "".join(ans) == string_s1 and string_s1 != string_s:
            return True
        return False

    def check_s1_is_prefix_of_s(self, *args):
        """
        Функция проверки того, что строка s1 является префиксом строки s
        :param args: входные аргументы
        :return: bool
        """
        string_s = self.s.text
        for i in range(len(string_s) - 1):
            if string_s[:i + 1] == self.s1.text:
                return True
        return False

    def check_s1_is_suffix_of_s(self, *args):
        """
        Функция проверки того, что строка s1 является суффиксом строки s
        :param args: входные аргументы
        :return: bool
        """
        string_s = self.s.text
        for i in range(len(string_s) - 1):
            if string_s[i:] == self.s1.text:
                return True
        return False

    def check_s1_is_substring_of_s(self, *args):
        """
        Функция проверки того, что строка s1 является подстрокой строки s
        :param args: входные аргументы
        :return: bool
        """
        return self.s1.text in self.s.text

    def __draw_shadow__(self, origin, end, context=None):
        pass

    def next_task(self, *args):
        """
        Функция перехода к следующему заданию
        :param args: входные аргументы
        :return: None
        """
        pass

    def previous_task(self, *args):
        """
        Функция перехода к предыдущему заданию
        :param args: входные аргументы
        :return: None
        """
        self.manager.transition.direction = 'right'
        self.manager.current = 'second_task'

    def load_string_s1(self, *args):
        """
        Функция импорта строки s1
        :param args: входные аргументы
        :return: None
        """
        ans = CSVHelper().import_str()
        if ans is not None:
            self.s1.text = ans

    def load_string_s(self, *args):
        """
        Функция импорта строки s
        :param args: входные аргументы
        :return: None
        """
        ans = CSVHelper().import_str()
        if ans is not None:
            self.s.text = ans

    def load_language(self, *args):
        """
        Функция импорта языка
        :param args: входные аргументы
        :return: bool
        """
        ans = CSVHelper().import_language()
        if ans is not None:
            self.language.text = ans
            return False
        return True

    def check_word_inside_language(self, string, language, *args):
        """
        Функция проверки принадлежности слова языку
        :param string: строка
        :param language: язык
        :param args: входные аргументы
        :return: bool
        """
        for symbol in string:
            if symbol not in language:
                self.note.universal_note(f'Слово \"{string}\" не принадлежит языку \"{language}\"', [])
                return False
        return True

    def check(self, *args):
        """
        Основная функция в задании - выводит заключение о том, чем является строка s1 для s
        :param args: входные аргументы
        :return: None
        """
        language = self.language.text.split(',')
        s = self.s.text
        s1 = self.s1.text
        if not self.check_word_inside_language(s, language):
            return
        if not self.check_word_inside_language(s1, language):
            return
        ans = ""
        flag = False
        if self.check_s1_is_substring_of_s():
            flag = True
            ans += "вторая подстрока (S1) является подстрокой первой строки (S);\n"
        if self.check_s1_is_subsequence_of_s():
            flag = True
            ans += "вторая подстрока (S1) является подпоследовательностью первой строки (S);\n"
        if self.check_s1_is_prefix_of_s():
            flag = True
            ans += "вторая подстрока (S1) является префиксом первой строки (S);\n"
        if self.check_s1_is_suffix_of_s():
            flag = True
            ans += "вторая подстрока (S1) является суффиксом первой строки (S);\n"
        if not flag:
            ans += "вторая подстрока (S1) не является подпоследовательностью первой строки (S);\n"
        self.note.universal_note(ans, [])
