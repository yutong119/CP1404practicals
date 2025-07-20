from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('dynamic_labels.kv')


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

