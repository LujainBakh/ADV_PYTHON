from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from src.ui.home_screen import HomeScreen
from src.ui.login_screen import LoginScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.button import Button
from PIL import Image
from src.database.db_manager import DatabaseManager


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.current_user = None

    def build(self):
        # Get image dimensions
        img = Image.open('src/assets/images/homepage.jpg')
        width, height = img.size
        
        # Set window size to match image dimensions
        Window.size = (width, height)
        Window.clearcolor = (1, 1, 1, 1)
        
        # Set theme colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        
        # Set up ScreenManager
        self.sm = ScreenManager()
        
        # Create screens
        self.login_screen = LoginScreen(name='login')
        self.home_screen = HomeScreen(name='home')
        
        # Add screens to manager
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.home_screen)
        
        # Set initial screen
        self.sm.current = 'login'
        
        # Set up callbacks
        self.login_screen.on_login_success = self.handle_login
        
        return self.sm

    def handle_login(self, email, password):
        user = self.db.verify_user(email, password)
        if user:
            self.current_user = user
            self.go_to_home()
            return True
        return False

    def go_to_home(self):
        self.sm.current = 'home'

    def add_gradient_button(self, text, icon, idx):
        # Simulate gradient with color alternation
        colors = [
            [(0.62, 0.74, 0.80, 1), (0.85, 0.88, 0.85, 1)],
            [(0.85, 0.88, 0.85, 1), (0.62, 0.74, 0.80, 1)],
        ]
        bg_color = colors[idx % 2][0] if idx % 2 == 0 else colors[idx % 2][1]
        btn = Button(
            text=f'   {text}',
            size_hint=(1, None),
            height=64,
            background_color=bg_color,
            color=(1,1,1,1),
            font_size=22,
        )
        self.buttons_box.add_widget(btn)

if __name__ == "__main__":
    MyApp().run()
