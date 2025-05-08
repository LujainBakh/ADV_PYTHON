from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from src.ui.login_screen import LoginScreen
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR

class MyApp(App):
    def build(self):
        # Set window size for desktop
        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        Window.clearcolor = get_color_from_hex(BACKGROUND_COLOR)
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()
