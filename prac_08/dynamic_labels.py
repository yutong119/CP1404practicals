from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('dynamic_labels.kv')


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        root_layout = self.root.ids.main

        for name in self.names:
            new_label = Label(text=name)
            root_layout.add_widget(new_label)

        return self.root

