from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    output_message = StringProperty

    def build(self):
        self.title = "Convert Miles to Km App"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_input(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def calculate_data(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)






