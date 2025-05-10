from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex

class BottomNav(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(60)
        self.md_bg_color = get_color_from_hex('#A9BCBD')
        
        # Home icon with navigation
        home_btn = MDIconButton(
            icon="home",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.25, 'center_y': 0.5}
        )
        home_btn.bind(on_press=lambda x: self.go_home())
        self.add_widget(home_btn)
        
        # Profile icon with navigation
        profile_btn = MDIconButton(
            icon="account",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        profile_btn.bind(on_press=lambda x: self.go_instructors())
        self.add_widget(profile_btn)
        
        # Resources icon (change to navigate to office hours)
        office_hours_btn = MDIconButton(
            icon="bank",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.75, 'center_y': 0.5}
        )
        office_hours_btn.bind(on_press=lambda x: self.go_office_hours())
        self.add_widget(office_hours_btn)

    def go_home(self):
        # Get the app's screen manager and switch to home screen
        app = MDApp.get_running_app()
        app.root.current = 'home'

    def go_instructors(self):
        # Get the app's screen manager and switch to instructors screen
        app = MDApp.get_running_app()
        app.root.current = 'instructors'

    def go_office_hours(self):
        # Get the app's screen manager and switch to office hours screen
        app = MDApp.get_running_app()
        app.root.current = 'office_hours' 