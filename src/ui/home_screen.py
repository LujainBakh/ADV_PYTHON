from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Line
import datetime

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)  # Set to white to avoid any color bleeding
        
        # Main layout
        self.layout = MDFloatLayout()
        self.add_widget(self.layout)
        
        # Background image
        self.bg_image = Image(
            source='src/assets/images/homepage.jpg',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1)
        )
        self.layout.add_widget(self.bg_image)
        
        # Content layout (will be placed on top of background)
        self.content_layout = MDFloatLayout()
        self.layout.add_widget(self.content_layout)

        # Hamburger menu
        self.menu_btn = MDIconButton(icon='menu', pos_hint={'x':0.03, 'top':0.97}, theme_text_color='Custom', text_color=get_color_from_hex('#607D8B'))
        self.content_layout.add_widget(self.menu_btn)

        # Welcome box with clock
        self.welcome_card = MDCard(
            size_hint=(0.9, None),
            height=170,
            pos_hint={'center_x': 0.5, 'top': 0.78},
            radius=[28],
            style='elevated',
            md_bg_color=(1, 1, 1, 1),
            line_color=(0, 0, 0, 1),
            elevation=0,
        )
        self.welcome_box = MDBoxLayout(orientation='vertical', padding=[0, 10, 0, 0], spacing=0)
        self.welcome_label = MDLabel(text='Welcome to Coded!', halign='center', font_style='H4', theme_text_color='Custom', text_color=(0,0,0,1), bold=True)
        self.clock_label = MDLabel(text='', halign='center', font_style='H5', theme_text_color='Custom', text_color=(0,0,0,1), bold=True)
        self.welcome_box.add_widget(self.welcome_label)
        self.welcome_box.add_widget(self.clock_label)
        self.welcome_card.add_widget(self.welcome_box)
        self.content_layout.add_widget(self.welcome_card)
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)

        # Four gradient buttons
        self.buttons_box = MDBoxLayout(orientation='vertical', spacing=18, size_hint=(0.92, None), height=340, pos_hint={'center_x': 0.5, 'top': 0.60})
        self.content_layout.add_widget(self.buttons_box)
        self.add_gradient_button('Calculate your GPA', 'arrow-right', 0)
        self.add_gradient_button('Open map', 'arrow-right', 1)
        self.add_gradient_button('Resources', 'arrow-right', 2)
        self.add_gradient_button('Contact Us', 'arrow-right', 3)

        # Bottom navigation bar
        self.bottom_nav = MDBottomNavigation()
        self.bottom_nav.panel_color = get_color_from_hex('#90A4AE')
        self.bottom_nav.text_color_active = (1,1,1,1)
        self.bottom_nav.text_color_normal = (1,1,1,0.7)
        self.bottom_nav.selected_color_background = get_color_from_hex('#607D8B')
        self.bottom_nav.size_hint = (1, None)
        self.bottom_nav.height = 80
        self.bottom_nav.pos_hint = {'center_x': 0.5, 'y': 0}
        self.content_layout.add_widget(self.bottom_nav)
        self.add_nav_item('Home', 'home')
        self.add_nav_item('Profile', 'account')
        self.add_nav_item('Campus', 'bank')
        self.add_nav_item('Calendar', 'calendar')

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

    def add_nav_item(self, text, icon):
        nav_item = MDBottomNavigationItem(
            name=text.lower(),
            text=text,
            icon=icon,
        )
        nav_item.add_widget(MDLabel(text=f'{text} Page', halign='center'))
        self.bottom_nav.add_widget(nav_item)

    def update_time(self, *args):
        now = datetime.datetime.now().strftime('%H:%M:%S')
        self.clock_label.text = now 