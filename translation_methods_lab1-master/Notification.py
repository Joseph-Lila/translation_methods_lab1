from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class Notification:
    def __init__(self, dialog):
        self.dialog = dialog

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def universal_note(self, title, params, *args):
        for i in range(len(params)):
            params[i].text = ''
        self.dialog = MDDialog(
            type="simple",
            text=title,
            buttons=[
                MDFlatButton(
                    text='OK',
                    on_release=self.dialog_close
                )
            ],
            radius=[25, 7, 25, 7],
            md_bg_color=[1, 1, 1, 1],
            size_hint=(1, 1)
        )
        self.dialog.open()

    def note_with_container(self, cont, title, size_hint, *args):
        self.dialog = MDDialog(
            title=title,
            type="custom",
            content_cls=cont[0],
            buttons=[
                MDFlatButton(
                    text='Выйти',
                    on_release=self.dialog_close
                )
            ],
            radius=[20, 7, 20, 7],
            size_hint=(1, 1)
        )
        self.dialog.open()