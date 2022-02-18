from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from FirstTask import FirstTask
from SecondTask import SecondTask
from ThirdTask import ThirdTask


class GUILogic(MDApp):
    def __init__(self, **kwargs):
        self.title = "Методы трансляции"
        self.manager = ScreenManager(transition=SlideTransition())
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "A700"
        self.manager.add_widget(FirstTask(name='first_task'))
        self.manager.add_widget(SecondTask(name='second_task'))
        self.manager.add_widget(ThirdTask(name='third_task'))
        return self.manager
