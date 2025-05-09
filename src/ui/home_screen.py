from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.app import MDApp
import datetime
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage

img = CoreImage('src/assets/images/homepage.jpg')
Window.size = (img.width, img.height)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls
        Window.clearcolor = (1, 1, 1, 1)
        
        # Main layout
        self.layout = MDFloatLayout()
        self.add_widget(self.layout)
        
        # Background image
        self.bg_image = Image(
            source='src/assets/images/homepage.jpg',
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=True
        )
        self.layout.add_widget(self.bg_image)
        
        # Content layout
        self.content_layout = MDFloatLayout()
        self.layout.add_widget(self.content_layout)

        # Welcome card with clock
        self.welcome_card = MDCard(
            size_hint=(0.9, None),
            pos_hint={'center_x': 0.5, 'top': 0.85},
            padding=20,
            elevation=3,
            radius=[20]
        )
        
        self.welcome_box = MDBoxLayout(orientation='vertical', spacing=20, adaptive_height=True, size_hint_y=None)
        self.welcome_label = MDLabel(
            text='Welcome to Coded!',
            font_style='H4',
            halign='center',
            theme_text_color='Primary',
            size_hint_y=None,
            height=self.welcome_label.texture_size[1] if hasattr(self, 'welcome_label') else 48
        )
        self.clock_label = MDLabel(
            text='',
            font_style='H6',
            halign='center',
            theme_text_color='Secondary',
            size_hint_y=None,
            height=self.clock_label.texture_size[1] if hasattr(self, 'clock_label') else 32
        )
        self.welcome_box.add_widget(self.welcome_label)
        self.welcome_box.add_widget(self.clock_label)
        self.welcome_card.add_widget(self.welcome_box)
        self.content_layout.add_widget(self.welcome_card)
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)
        self.welcome_card.height = self.welcome_box.height + 40  # Add some padding

        # Four gradient buttons
        self.buttons_box = MDBoxLayout(
            orientation='vertical',
            spacing=15,
            size_hint=(0.92, None),
            height=340,
            pos_hint={'center_x': 0.5, 'top': 0.65}
        )
        self.content_layout.add_widget(self.buttons_box)
        
        # Add buttons with the same blue-gray color
        button_colors = {
            'Calculate your GPA': 'calculator',
            'Open map': 'map',
            'Resources': 'book',
            'Contact Us': 'email'
        }
        for text, icon in button_colors.items():
            self.add_gradient_button(text, icon)

        # Bottom navigation bar
        self.bottom_nav = MDBoxLayout(
            size_hint=(1, None),
            height=80,
            pos_hint={'center_x': 0.5, 'y': 0},
            md_bg_color=get_color_from_hex('#A9BCBD'),  # Updated to new color
            orientation='horizontal',
            padding=[0, 0, 0, 0],
            spacing=20
        )
        self.content_layout.add_widget(self.bottom_nav)

        # Add a spacer widget before the icons
        self.bottom_nav.add_widget(Widget())
        # Add navigation items
        self.add_nav_item('Home', 'home')
        self.add_nav_item('Profile', 'account')
        self.add_nav_item('Campus', 'school')
        self.add_nav_item('Calendar', 'calendar')
        # Add a spacer widget after the icons
        self.bottom_nav.add_widget(Widget())

        # Hamburger menu
        self.menu_btn = MDIconButton(
            icon="menu",
            pos_hint={'x': 0.02, 'top': 0.98},
            theme_text_color="Custom",
            text_color=get_color_from_hex('#000000')  # Black for visibility
        )
        
        # Add hamburger menu button last to ensure it's on top
        self.content_layout.add_widget(self.menu_btn)

    def add_gradient_button(self, text, icon, palette=None, hue=None):
        btn = MDRaisedButton(
            text=text,
            icon=icon,
            size_hint=(1, None),
            height=64,
            md_bg_color=get_color_from_hex('#A9BCBD'),  # Updated to new color
            elevation=2,
            _no_ripple_effect=False,
            font_size='18sp'
        )
        self.buttons_box.add_widget(btn)

    def add_nav_item(self, text, icon):
        nav_btn = MDIconButton(
            icon=icon,
            theme_text_color="Custom",
            text_color=get_color_from_hex('#FFFFFF'),
            icon_size="24sp"
        )
        self.bottom_nav.add_widget(nav_btn)

    def update_time(self, *args):
        now = datetime.datetime.now().strftime('%H:%M:%S')
        self.clock_label.text = now 