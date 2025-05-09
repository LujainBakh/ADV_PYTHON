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
from kivy.graphics import Color, Rectangle
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from src.ui.bottom_nav import BottomNav
from src.ui.gpacalculator_screen import GPACalculatorScreen
from src.ui.resources_screen import ResourcesScreen

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
        
        # White background
        with self.layout.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.bg_rect = Rectangle(pos=self.layout.pos, size=self.layout.size)
        self.layout.bind(pos=self.update_bg, size=self.update_bg)
        
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

        # Navigation Drawer
        self.nav_drawer = MDNavigationDrawer(
            id="nav_drawer",
            radius=(0, 16, 16, 0),
            size_hint_y=1,  # Full height
            pos_hint={"top": 1},
        )
        
        # Drawer content
        drawer_content = MDBoxLayout(orientation="vertical", spacing="2dp", padding=[8, 0, 8, 8])
        
        # User info section
        user_info = MDBoxLayout(orientation="vertical", size_hint_y=None, height="160dp", padding=[8, 8, 8, 8])
        user_info.md_bg_color = get_color_from_hex('#A9BCBD')
        
        # User avatar and name
        avatar = MDIconButton(
            icon="account-circle",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#FFFFFF'),
            font_size="48sp",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        user_name = MDLabel(
            text="Lujain Bakhurji",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#FFFFFF'),
            halign="center",
            font_style="H6"
        )
        user_email = MDLabel(
            text="2210002938@iau.edu.sa",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#FFFFFF'),
            halign="center",
            font_style="Body2"
        )
        
        user_info.add_widget(avatar)
        user_info.add_widget(user_name)
        user_info.add_widget(user_email)
        drawer_content.add_widget(user_info)
        
        # Menu items
        menu_items = [
            {"icon": "account-circle", "text": "Profile"},
            {"icon": "map", "text": "Map"},
            {"icon": "calculator-variant", "text": "GPA Calculator"},
            {"icon": "cog", "text": "Settings"},
            {"icon": "logout", "text": "Log out"}
        ]
        
        menu_list = MDList()
        for item in menu_items:
            list_item = OneLineIconListItem(text=item["text"])
            list_item.add_widget(IconLeftWidget(icon=item["icon"]))
            menu_list.add_widget(list_item)
        
        drawer_content.add_widget(menu_list)
        self.nav_drawer.add_widget(drawer_content)
        # Add the drawer as a direct child of the screen so it overlays everything
        self.add_widget(self.nav_drawer)

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
            self.add_gradient_button(text, icon, on_press=self.handle_button_press)

        # Add bottom navigation
        self.bottom_nav = BottomNav()
        self.content_layout.add_widget(self.bottom_nav)

        # Hamburger menu
        self.menu_btn = MDIconButton(
            icon="menu",
            pos_hint={'x': 0.02, 'top': 0.98},
            theme_text_color="Custom",
            text_color=get_color_from_hex('#000000')  # Black for visibility
        )
        self.menu_btn.bind(on_release=self.toggle_nav_drawer)
        
        # Add hamburger menu button last to ensure it's on top
        self.content_layout.add_widget(self.menu_btn)

    def toggle_nav_drawer(self, *args):
        self.nav_drawer.set_state("open" if self.nav_drawer.state == "close" else "close")

    def update_bg(self, *args):
        self.bg_rect.pos = self.layout.pos
        self.bg_rect.size = self.layout.size

    def add_gradient_button(self, text, icon, on_press=None):
        btn = MDRaisedButton(
            text=text,
            icon=icon,
            size_hint=(1, None),
            height=64,
            md_bg_color=get_color_from_hex('#A9BCBD'),
            elevation=2,
            _no_ripple_effect=False,
            font_size='18sp'
        )
        if on_press:
            btn.bind(on_press=on_press)
        self.buttons_box.add_widget(btn)

    def handle_button_press(self, instance):
        app = MDApp.get_running_app()
        if instance.text == 'Calculate your GPA':
            if 'gpa_calculator' not in app.root.screen_names:
                app.root.add_widget(GPACalculatorScreen(name='gpa_calculator'))
            app.root.current = 'gpa_calculator'
        elif instance.text == 'Resources':
            if 'resources' not in app.root.screen_names:
                app.root.add_widget(ResourcesScreen(name='resources'))
            app.root.current = 'resources'

    def update_time(self, *args):
        now = datetime.datetime.now().strftime('%H:%M:%S')
        self.clock_label.text = now 