from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from src.ui.bottom_nav import BottomNav
from src.ui.widgets import RoundedTextInput, RoundedButton
from src.database.db_manager import DatabaseManager
import sqlite3

PROFILE_BG = '#A9BCBD'
FIELD_LABEL_COLOR = '#000000'
FIELD_HINT_COLOR = '#B0B0B0'

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.user_id = None
        print("ProfileScreen initialized")
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.build_ui()

    def on_enter(self):
        print("Entering ProfileScreen")
        app = App.get_running_app()
        if hasattr(app, 'current_user') and app.current_user:
            print(f"Current user found: {app.current_user}")
            self.user_id = app.current_user[0]  # Get user ID from current_user tuple
            self.load_user_data()
        else:
            print("No current user found")
            # Show error message to user
            self.show_error("Please log in to view your profile")

    def build_ui(self):
        # Top bar (like ResourcesScreen)
        self.top_bar = MDBoxLayout(
            size_hint_y=None,
            height=dp(48),
            md_bg_color=get_color_from_hex(PROFILE_BG),
            padding=[dp(10), 0, 0, 0]
        )
        back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            on_release=self.go_back
        )
        title = MDLabel(
            text="Profile",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        self.top_bar.add_widget(back_button)
        self.top_bar.add_widget(title)
        self.layout.add_widget(self.top_bar)

        # Add back button at the top left
        self.back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            pos_hint={'x': 0, 'top': 1},
            on_release=self.go_back
        )
        self.layout.add_widget(self.back_button)

        # Decorative lines (SVG-like)
        with self.layout.canvas:
            Color(0,0,0,1)
            Line(circle=(dp(120), dp(700), dp(180)), width=1)
            Line(circle=(dp(120), dp(700), dp(120)), width=1)
            Line(points=[dp(400), dp(100), dp(600), dp(300), dp(500), dp(500)], width=1)

        # Profile fields
        self.fields_box = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.9, None), height=420, pos_hint={'center_x':0.5, 'top':0.7})
        self.layout.add_widget(self.fields_box)

        # Create text inputs
        self.first_name = MDTextField(hint_text='First Name', font_size=22, size_hint_y=None, height=48)
        self.last_name = MDTextField(hint_text='Last Name', font_size=22, size_hint_y=None, height=48)
        self.email = MDTextField(hint_text='Email', font_size=22, size_hint_y=None, height=48, readonly=True)
        self.university = MDTextField(hint_text='University', font_size=22, size_hint_y=None, height=48, readonly=True)
        self.phone = MDTextField(hint_text='Phone Number', font_size=22, size_hint_y=None, height=48)
        self.college = MDTextField(hint_text='College', font_size=18, size_hint_y=None, height=48, readonly=True)

        self.fields_box.add_widget(self.first_name)
        self.fields_box.add_widget(self.last_name)
        self.fields_box.add_widget(self.email)
        self.fields_box.add_widget(self.university)
        self.fields_box.add_widget(self.phone)
        self.fields_box.add_widget(self.college)

        # Update button
        self.update_btn = RoundedButton(text='Update Profile', size_hint=(1, None), height=48, font_size=20, color=(1,1,1,1))
        self.update_btn.background_color = get_color_from_hex(PROFILE_BG)
        self.update_btn.bind(on_press=self.update_profile)
        self.layout.add_widget(self.update_btn)
        self.update_btn.pos_hint = {'center_x':0.5}
        self.update_btn.y = dp(120)

        # Bottom nav
        self.bottom_nav = BottomNav()
        self.bottom_nav.pos_hint = {'center_x':0.5, 'y':0}
        self.layout.add_widget(self.bottom_nav)

    def load_user_data(self):
        print(f"Loading data for user ID: {self.user_id}")
        if self.user_id:
            user_info = self.db.get_user_info(self.user_id)
            print(f"Retrieved user info: {user_info}")
            if user_info:
                email, first_name, last_name, college_name, phone_number = user_info
                print(f"Setting fields: {first_name}, {last_name}, {email}, {college_name}, {phone_number}")
                # Update the TextInput fields
                self.first_name.text = first_name
                print("First name field now contains:", self.first_name.text)
                self.last_name.text = last_name
                self.email.text = email
                self.phone.text = phone_number
                self.college.text = college_name
                self.university.text = 'Imam Abdulrahman Bin Faisal University'
                # Disable read-only fields
                self.email.disabled = True
                self.college.disabled = True
                self.university.disabled = True
                print("Profile data loaded successfully")
            else:
                print("Failed to get user info from database")
                self.show_error("Failed to load user data")
        else:
            print("No user_id set!")

    def show_error(self, message):
        self.fields_box.clear_widgets()
        self.fields_box.add_widget(Label(text=message, color=(1,0,0,1), font_size=22))
        self.update_btn.disabled = True

    def update_profile(self, instance):
        if not self.user_id:
            return
            
        # Only allow editing of first_name, last_name, phone
        updated = self.db.update_user_info(
            self.user_id,
            self.email.text,
            self.first_name.text,
            self.last_name.text,
            self.college.text,
            self.phone.text
        )
        if updated:
            self.update_btn.text = 'Profile Updated!'
        else:
            self.update_btn.text = 'Update Failed!'

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'home'
