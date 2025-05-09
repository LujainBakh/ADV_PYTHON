from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

PRIMARY_COLOR = '#2196F3'
BACKGROUND_COLOR = '#F5F5F5'
TEXT_PRIMARY = '#333333'
TEXT_SECONDARY = '#666666'

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[0,0,0,0], spacing=0, size_hint=(1,1))
        self.add_widget(self.layout)
        
        # Background
        with self.layout.canvas.before:
            Color(*get_color_from_hex(BACKGROUND_COLOR))
            self.bg_rect = RoundedRectangle(pos=self.layout.pos, size=self.layout.size, radius=[20,])
        self.layout.bind(pos=self.update_bg, size=self.update_bg)
        
        # Scrollable form container
        scroll = ScrollView(size_hint=(1, 1))
        self.form_container = RelativeLayout(size_hint=(None, None), width=500, height=800, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.form = BoxLayout(orientation='vertical', size_hint=(None, None), width=460, height=760, pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=16, padding=[40, 40, 40, 40])
        
        # Form background
        with self.form.canvas.before:
            Color(1, 1, 1, 1)
            self.form_bg = RoundedRectangle(pos=self.form.pos, size=self.form.size, radius=[28,])
        self.form.bind(pos=self.update_form_bg, size=self.update_form_bg)
        
        # Title and subtitle
        self.form.add_widget(Label(text='Create Account', font_size=38, size_hint_y=None, height=60, bold=True, color=get_color_from_hex(TEXT_PRIMARY)))
        self.form.add_widget(Label(text='Please fill in your details', font_size=22, size_hint_y=None, height=38, color=get_color_from_hex(TEXT_SECONDARY)))
        
        # Form fields
        self.email = TextInput(hint_text='Email', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.email)
        
        self.password = TextInput(hint_text='Password', password=True, size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.password)
        
        self.first_name = TextInput(hint_text='First Name', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.first_name)
        
        self.last_name = TextInput(hint_text='Last Name', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.last_name)
        
        self.college_name = TextInput(hint_text='College Name', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.college_name)
        
        self.phone_number = TextInput(hint_text='Phone Number', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.phone_number)
        
        # Register button
        self.register_button = Button(text='Create Account', size_hint_y=None, height=64, background_normal='', background_color=get_color_from_hex(PRIMARY_COLOR), color=(1, 1, 1, 1), font_size=24, bold=True)
        self.register_button.bind(on_press=self.register)
        self.form.add_widget(self.register_button)
        
        # Login link
        self.login_button = Button(text='Already have an account? Sign In', size_hint_y=None, height=40, background_normal='', background_color=(0,0,0,0), color=get_color_from_hex(PRIMARY_COLOR), font_size=18)
        self.login_button.bind(on_press=self.go_to_login)
        self.form.add_widget(self.login_button)
        
        # Status label
        self.status_label = Label(text='', font_size=18, size_hint_y=None, height=38, color=get_color_from_hex('#4CAF50'))
        self.form.add_widget(self.status_label)
        
        self.form_container.add_widget(self.form)
        scroll.add_widget(self.form_container)
        self.layout.add_widget(scroll)
        
        self.on_register_success = None
        self.on_go_to_login = None

    def update_bg(self, *args):
        self.bg_rect.pos = self.layout.pos
        self.bg_rect.size = self.layout.size

    def update_form_bg(self, *args):
        self.form_bg.pos = self.form.pos
        self.form_bg.size = self.form.size

    def register(self, instance):
        # Get all field values
        email = self.email.text.strip()
        password = self.password.text.strip()
        first_name = self.first_name.text.strip()
        last_name = self.last_name.text.strip()
        college_name = self.college_name.text.strip()
        phone_number = self.phone_number.text.strip()
        
        # Validate fields
        if not all([email, password, first_name, last_name, college_name, phone_number]):
            self.status_label.text = 'Please fill in all fields'
            self.status_label.color = get_color_from_hex('#F44336')
            return
        
        # Call the registration callback
        if self.on_register_success:
            success = self.on_register_success(email, password, first_name, last_name, college_name, phone_number)
            if success:
                self.status_label.text = 'Registration successful!'
                self.status_label.color = get_color_from_hex('#4CAF50')
                self.go_to_login(None)
            else:
                self.status_label.text = 'Email already exists'
                self.status_label.color = get_color_from_hex('#F44336')

    def go_to_login(self, instance):
        if self.on_go_to_login:
            self.on_go_to_login() 