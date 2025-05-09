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
            pos_hint={'center_x': 0.15, 'center_y': 0.5}
        )
        home_btn.bind(on_press=lambda x: self.go_home())
        self.add_widget(home_btn)
        
        # Profile icon
        self.add_widget(MDIconButton(
            icon="account",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.38, 'center_y': 0.5}
        ))
        
        # Resources icon
        self.add_widget(MDIconButton(
            icon="bank",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.62, 'center_y': 0.5}
        ))
        
        # Calendar icon
        self.add_widget(MDIconButton(
            icon="calendar",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.85, 'center_y': 0.5}
        ))

    def go_home(self):
        # Get the app's screen manager and switch to home screen
        app = MDApp.get_running_app()
        app.root.current = 'home' 