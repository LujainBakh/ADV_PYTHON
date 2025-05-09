from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel, MDIcon
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from src.ui.bottom_nav import BottomNav
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import webbrowser
from kivy.graphics import Color, Rectangle
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.clock import Clock
from kivymd.uix.card import MDCard

class ResourcesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'resources'
        
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

        # Foreground content
        foreground = MDBoxLayout(orientation='vertical')

        # Top bar
        top_bar = MDBoxLayout(
            size_hint_y=None,
            height=dp(48),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            padding=[dp(10), 0, 0, 0]
        )
        back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            on_release=self.go_back
        )
        title = MDLabel(
            text="Resources",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        top_bar.add_widget(back_button)
        top_bar.add_widget(title)

        # Content
        content = MDBoxLayout(
            orientation='vertical',
            padding=[dp(16), dp(20), dp(16), dp(16)],
            spacing=dp(15)
        )

        # Spacer to push buttons down
        content.add_widget(MDBoxLayout(size_hint_y=0.2))

        # Grid for buttons
        buttons_grid = MDBoxLayout(
            orientation='vertical',
            spacing=dp(15),
            size_hint=(0.8, None),  # Make grid narrower
            height=dp(160),  # Reduce total height
            pos_hint={'center_x': 0.5}  # Center horizontally
        )

        # First row
        row1 = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(15),
            size_hint_y=None,
            height=dp(60)
        )

        sis_button = MDRaisedButton(
            text="",  # Remove text since we'll add it with layout
            size_hint=(0.5, 1),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            on_release=lambda x: self.open_url("https://sis.iau.edu.sa"),
            elevation=2,
            _radius=8
        )
        
        # Create layout for SIS button content
        sis_content = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint=(None, None),
            size=(dp(120), dp(40)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        sis_icon = MDIcon(
            icon="school",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_y': 0.5}
        )
        sis_label = MDLabel(
            text="SIS",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="18sp",
            halign='left'
        )
        sis_content.add_widget(sis_icon)
        sis_content.add_widget(sis_label)
        sis_button.add_widget(sis_content)

        blackboard_button = MDRaisedButton(
            text="",
            size_hint=(0.5, 1),
            md_bg_color=get_color_from_hex('#C5D1D2'),
            on_release=lambda x: self.open_url("https://vle.iau.edu.sa"),
            elevation=2,
            _radius=8
        )
        
        bb_content = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint=(None, None),
            size=(dp(120), dp(40)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        bb_icon = MDIcon(
            icon="notebook",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_y': 0.5}
        )
        bb_label = MDLabel(
            text="Blackboard",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="18sp",
            halign='left'
        )
        bb_content.add_widget(bb_icon)
        bb_content.add_widget(bb_label)
        blackboard_button.add_widget(bb_content)

        row1.add_widget(sis_button)
        row1.add_widget(blackboard_button)

        # Second row
        row2 = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(15),
            size_hint_y=None,
            height=dp(60)
        )

        elibrary_button = MDRaisedButton(
            text="",
            size_hint=(0.5, 1),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            on_release=lambda x: self.open_url("https://library.iau.edu.sa"),
            elevation=2,
            _radius=8
        )
        
        lib_content = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint=(None, None),
            size=(dp(120), dp(40)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        lib_icon = MDIcon(
            icon="book",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_y': 0.5}
        )
        lib_label = MDLabel(
            text="E-library",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="18sp",
            halign='left'
        )
        lib_content.add_widget(lib_icon)
        lib_content.add_widget(lib_label)
        elibrary_button.add_widget(lib_content)

        iau_button = MDRaisedButton(
            text="",
            size_hint=(0.5, 1),
            md_bg_color=get_color_from_hex('#C5D1D2'),
            on_release=lambda x: self.open_url("https://www.iau.edu.sa"),
            elevation=2,
            _radius=8
        )
        
        iau_content = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint=(None, None),
            size=(dp(120), dp(40)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        iau_icon = MDIcon(
            icon="web",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_y': 0.5}
        )
        iau_label = MDLabel(
            text="IAU\nwebsite",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="18sp",
            halign='left'
        )
        iau_content.add_widget(iau_icon)
        iau_content.add_widget(iau_label)
        iau_button.add_widget(iau_content)

        row2.add_widget(elibrary_button)
        row2.add_widget(iau_button)

        buttons_grid.add_widget(row1)
        buttons_grid.add_widget(row2)
        content.add_widget(buttons_grid)

        # Spacer to push buttons up
        content.add_widget(MDBoxLayout(size_hint_y=0.3))

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

        # Add everything to foreground
        foreground.add_widget(top_bar)
        foreground.add_widget(content)
        foreground.add_widget(BottomNav())

        self.content_layout.add_widget(foreground)

    def go_back(self, instance):
        self.manager.current = 'home'

    def open_url(self, url):
        webbrowser.open(url)

    def update_bg(self, *args):
        self.bg_rect.pos = self.layout.pos
        self.bg_rect.size = self.layout.size

    def update_time(self, dt):
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')
        self.clock_label.text = current_time 