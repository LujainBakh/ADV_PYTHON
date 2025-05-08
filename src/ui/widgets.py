from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        
    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*get_color_from_hex('#2196F3'))
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10,])

class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''  # Ensure no default background blocks input
        self.cursor_color = get_color_from_hex('#2196F3')
        self.foreground_color = get_color_from_hex('#333333')
        self.multiline = False
        self.padding = [20, 15, 20, 15]
        self.write_tab = False
        self.disabled = False  # Ensure input is enabled
        self.readonly = False  # Ensure input is editable
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        # Optionally, set focus to True for the first field in the login screen
        
    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*get_color_from_hex('#F5F5F5'))
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10,])
            
    def on_focus(self, instance, value):
        if value:
            self.canvas.before.clear()
            with self.canvas.before:
                Color(*get_color_from_hex('#E0E0E0'))
                RoundedRectangle(pos=self.pos, size=self.size, radius=[10,])
        else:
            self.canvas.before.clear()
            with self.canvas.before:
                Color(*get_color_from_hex('#F5F5F5'))
                RoundedRectangle(pos=self.pos, size=self.size, radius=[10,]) 