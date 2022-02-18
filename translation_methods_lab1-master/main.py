from kivy.config import Config


Config.set('graphics', 'borderless', 'True')
Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set("graphics", "width", 1000)
Config.set("graphics", "height", 850)


from kivy.core.window import Window
from GUILogic import GUILogic
from kivy.lang import Builder


Builder.load_file("kv-files/FirstTask.kv")
Builder.load_file("kv-files/SecondTask.kv")
Builder.load_file("kv-files/ThirdTask.kv")


def main():
    # Убирает панель со стандартными кнпками (свернуть, закрыть окно)
    Window.bordeless = 'True'

    GUILogic().run()


if __name__ == "__main__":
    main()
