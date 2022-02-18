from plyer import filechooser
from kivymd.toast import toast
from Notification import Notification
import csv


class CSVHelper:
    dialog = None
    note = Notification(dialog)

    def __init__(self):
        self.file_manager_answer = '?'

    @staticmethod
    def read_language(files_title):
        ans = []
        with open(files_title, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                ans = row
                ans = ','.join(ans)
        return ans

    @staticmethod
    def read_str(files_title):
        ans = []
        with open(files_title, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                ans = row[0]
        return ans

    def choose_file_using_manager(self, *args):
        try:
            path = filechooser.open_file()[0]
            toast(path)
            self.file_manager_answer = path
        except:
            self.note.universal_note('Вы не выбрали файл!', [])
            return False
        return True

    def import_language(self, *args):
        if self.choose_file_using_manager():
            return self.read_language(self.file_manager_answer)

    def import_str(self, *args):
        if self.choose_file_using_manager():
            return self.read_str(self.file_manager_answer)

    @staticmethod
    def export_answer(ans, file="/csv/answer.csv"):
        with open(file, encoding='utf-8') as w_file:
            pass
