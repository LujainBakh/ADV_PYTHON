from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from src.ui.home_screen import HomeScreen
from kivymd.uix.button import MDRaisedButton
from PIL import Image

class MyApp(MDApp):
    def build(self):
        # Get image dimensions
        img = Image.open('src/assets/images/homepage.jpg')
        width, height = img.size
        
        # Set window size to match image dimensions
        Window.size = (width, height)
        Window.clearcolor = (1, 1, 1, 1)
        return HomeScreen()

    def add_gradient_button(self, text, icon, idx):
        # Simulate gradient with color alternation
        colors = [
            [(0.62, 0.74, 0.80, 1), (0.85, 0.88, 0.85, 1)],
            [(0.85, 0.88, 0.85, 1), (0.62, 0.74, 0.80, 1)],
        ]
        bg_color = colors[idx % 2][0] if idx % 2 == 0 else colors[idx % 2][1]
        btn = MDRaisedButton(
            text=f'   {text}',
            icon=icon,
            size_hint=(1, None),
            height=64,
            md_bg_color=bg_color,
            text_color=(1,1,1,1),
            font_size=22,
        )
        self.buttons_box.add_widget(btn)

if __name__ == "__main__":
    MyApp().run()
