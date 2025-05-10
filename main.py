from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from src.ui.home_screen import HomeScreen
from src.ui.login_screen import LoginScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.button import Button
from PIL import Image
from src.database.db_manager import DatabaseManager
from src.ui.profile_screen import ProfileScreen
from src.ui.instructors_screen import InstructorsScreen
from src.ui.officehours_screen import OfficeHoursScreen


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.current_user = None
        self.current_user_id = None

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
        self.profile_screen = ProfileScreen(name='profile')
        self.instructors_screen = InstructorsScreen(name='instructors')
        self.officehours_screen = OfficeHoursScreen(name='office_hours')
        
        # Add screens to manager
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.home_screen)
        self.sm.add_widget(self.profile_screen)
        self.sm.add_widget(self.instructors_screen)
        self.sm.add_widget(self.officehours_screen)
        
        # Set initial screen
        self.sm.current = 'login'
        
        # Set up callbacks
        self.login_screen.on_login_success = self.handle_login
        
        return self.sm

    def handle_login(self, email, password):
        user = self.db.verify_user(email, password)
        if user:
            self.current_user = user  # This will be a tuple of (id, first_name, last_name)
            self.current_user_id = user[0]
            print(f"User logged in: {self.current_user}")
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
