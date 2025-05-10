from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from src.ui.bottom_nav import BottomNav
from kivy.uix.scrollview import ScrollView
from kivymd.toast import toast

class OfficeHoursScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDFloatLayout()
        self.add_widget(self.layout)
        self.build_ui()

    def build_ui(self):
        # Soft background color
        with self.layout.canvas.before:
            Color(0.97, 0.98, 1, 1)
            self.bg_rect = Rectangle(pos=self.layout.pos, size=self.layout.size)
        self.layout.bind(pos=self.update_bg, size=self.update_bg)

        # Top bar
        self.top_bar = MDBoxLayout(
            size_hint_y=None,
            height=dp(56),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            padding=[dp(8), 0, 0, 0],
            pos_hint={'top': 1}
        )
        self.menu_btn = MDIconButton(
            icon="menu",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            pos_hint={'center_y': 0.5}
        )
        self.top_bar.add_widget(self.menu_btn)
        self.top_bar.add_widget(MDLabel(
            text="Office Hours",
            font_style="H5",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            halign="left",
            valign="middle"
        ))
        self.layout.add_widget(self.top_bar)

        # Card with all fields and button
        self.card = MDCard(
            orientation='vertical',
            size_hint=(0.95, None),
            width=min(dp(400), self.width * 0.95) if self.width else dp(400),
            height=dp(420),  # Use a fixed height
            pos_hint={'center_x': 0.5, 'center_y': 0.53},
            padding=[dp(16), dp(16), dp(16), dp(16)],
            elevation=0,
            radius=[20],
            md_bg_color=(1, 1, 1, 1),
        )
        
        # Use a ScrollView to wrap the card content for overflow
        scroll = ScrollView(size_hint=(1, 1))
        card_box = MDBoxLayout(orientation='vertical', spacing=dp(12), size_hint_y=None)
        card_box.bind(minimum_height=card_box.setter('height'))

        # Section title
        card_box.add_widget(MDLabel(
            text="Book an Office Hour",
            font_style="H6",
            theme_text_color="Primary",
            halign="center",
            size_hint_y=None,
            height=dp(28),
            bold=True
        ))
        card_box.add_widget(MDLabel(size_hint_y=None, height=dp(4)))  # Spacer

        # Instructor field
        card_box.add_widget(MDLabel(
            text="Instructor",
            font_style="Subtitle2",
            theme_text_color="Secondary",
            halign="center",
            size_hint_y=None,
            height=dp(18),
        ))
        self.instructor_input = MDTextField(
            hint_text="e.g. Dr. Jood",
            mode="rectangle",
            size_hint_x=1,
            size_hint_y=None,
            height=dp(38),
            font_size=dp(16),
            padding=[dp(6), 0, dp(6), 0],
        )
        card_box.add_widget(self.instructor_input)
        card_box.add_widget(MDLabel(size_hint_y=None, height=dp(6)))  # Spacer

        # Date field
        card_box.add_widget(MDLabel(
            text="Date",
            font_style="Subtitle2",
            theme_text_color="Secondary",
            halign="center",
            size_hint_y=None,
            height=dp(18),
        ))
        self.date_input = MDTextField(
            hint_text="e.g. 2024-12-08",
            mode="rectangle",
            size_hint_x=1,
            size_hint_y=None,
            height=dp(38),
            font_size=dp(16),
            padding=[dp(6), 0, dp(6), 0],
        )
        card_box.add_widget(self.date_input)
        card_box.add_widget(MDLabel(size_hint_y=None, height=dp(6)))  # Spacer

        # Time field
        card_box.add_widget(MDLabel(
            text="Time",
            font_style="Subtitle2",
            theme_text_color="Secondary",
            halign="center",
            size_hint_y=None,
            height=dp(18),
        ))
        self.time_input = MDTextField(
            hint_text="e.g. 10:00 AM",
            mode="rectangle",
            size_hint_x=1,
            size_hint_y=None,
            height=dp(38),
            font_size=dp(16),
            padding=[dp(6), 0, dp(6), 0],
        )
        card_box.add_widget(self.time_input)
        card_box.add_widget(MDLabel(size_hint_y=None, height=dp(10)))  # Spacer

        # Confirm button
        self.confirm_btn = MDRaisedButton(
            text="Confirm",
            md_bg_color=get_color_from_hex('#A9BCBD'),
            text_color=(0,0,0,1),
            size_hint=(1, None),
            height=dp(42),
            font_size=dp(16),
            pos_hint={"center_x": 0.5},
            elevation=2,
            on_release=self.confirm_appointment
        )
        card_box.add_widget(self.confirm_btn)

        scroll.add_widget(card_box)
        self.card.clear_widgets()
        self.card.add_widget(scroll)
        self.layout.add_widget(self.card)

        # Bottom navigation (always at the bottom)
        self.bottom_nav = BottomNav()
        self.bottom_nav.size_hint = (1, None)
        self.bottom_nav.height = dp(70)
        self.bottom_nav.pos_hint = {'center_x':0.5, 'y':0}
        self.layout.add_widget(self.bottom_nav)

    def update_bg(self, *args):
        self.bg_rect.pos = self.layout.pos
        self.bg_rect.size = self.layout.size

    def confirm_appointment(self, instance):
        print(f"Confirmed: {self.instructor_input.text}, {self.date_input.text}, {self.time_input.text}")
        toast("Appointment booked!")
