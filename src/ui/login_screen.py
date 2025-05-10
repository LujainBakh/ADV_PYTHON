from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.screenmanager import Screen

PRIMARY_COLOR = '#2196F3'
BACKGROUND_COLOR = '#F5F5F5'
TEXT_PRIMARY = '#333333'
TEXT_SECONDARY = '#666666'

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Move all BoxLayout code into a child widget
        self.layout = BoxLayout(orientation='vertical', padding=[0,0,0,0], spacing=0, size_hint=(1,1))
        self.add_widget(self.layout)
        self.layout.canvas.before.clear()
        with self.layout.canvas.before:
            Color(*get_color_from_hex(BACKGROUND_COLOR))
            self.bg_rect = RoundedRectangle(pos=self.layout.pos, size=self.layout.size, radius=[20,])
        self.layout.bind(pos=self.update_bg, size=self.update_bg)
        # Centered form container (bigger and centered)
        self.form_container = RelativeLayout(size_hint=(None, None), width=500, height=540, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.form = BoxLayout(orientation='vertical', size_hint=(None, None), width=460, height=500, pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=32, padding=[40, 40, 40, 40])
        with self.form.canvas.before:
            Color(1, 1, 1, 1)
            self.form_bg = RoundedRectangle(pos=self.form.pos, size=self.form.size, radius=[28,])
        self.form.bind(pos=self.update_form_bg, size=self.update_form_bg)
        self.form.add_widget(Label(text='Welcome Back', font_size=38, size_hint_y=None, height=60, bold=True, color=get_color_from_hex(TEXT_PRIMARY)))
        self.form.add_widget(Label(text='Please sign in to continue', font_size=22, size_hint_y=None, height=38, color=get_color_from_hex(TEXT_SECONDARY)))
        self.email = TextInput(hint_text='Email', size_hint_y=None, height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 24, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        self.form.add_widget(self.email)
        # Password row with show/hide toggle
        pw_row = RelativeLayout(size_hint_y=None, height=64)
        self.password = TextInput(hint_text='Password', password=True, size_hint=(1, None), height=64, multiline=False, background_normal='', background_active='', background_color=(0.96, 0.96, 0.96, 1), foreground_color=get_color_from_hex(TEXT_PRIMARY), padding=[24, 20, 56, 20], cursor_color=get_color_from_hex(PRIMARY_COLOR), font_size=22)
        pw_row.add_widget(self.password)
        self.show_pw_btn = ToggleButton(text='👁', size_hint=(None, None), width=40, height=40, pos_hint={'right': 1, 'center_y': 0.5}, background_normal='', background_color=(0,0,0,0), font_size=24)
        self.show_pw_btn.bind(on_press=self.toggle_password)
        pw_row.add_widget(self.show_pw_btn)
        self.form.add_widget(pw_row)
        self.login_button = Button(text='Sign In', size_hint_y=None, height=64, background_normal='', background_color=get_color_from_hex('#A9BCBD'), color=(1, 1, 1, 1), font_size=24, bold=True)
        self.login_button.bind(on_press=self.login)
        self.form.add_widget(self.login_button)
        
        self.status_label = Label(text='', font_size=18, size_hint_y=None, height=38, color=get_color_from_hex('#4CAF50'))
        self.form.add_widget(self.status_label)
        self.form_container.add_widget(self.form)
        # Use BoxLayout with center alignment for vertical centering
        self.layout.add_widget(BoxLayout(size_hint_y=1))
        self.layout.add_widget(self.form_container)
        self.layout.add_widget(BoxLayout(size_hint_y=1))
        self.on_login_success = None  # Callback for successful login

    def update_bg(self, *args):
        self.bg_rect.pos = self.layout.pos
        self.bg_rect.size = self.layout.size

    def update_form_bg(self, *args):
        self.form_bg.pos = self.form.pos
        self.form_bg.size = self.form.size

    def toggle_password(self, instance):
        self.password.password = not self.show_pw_btn.state == 'down'
        self.show_pw_btn.text = '🙈' if self.show_pw_btn.state == 'down' else '👁'

    def login(self, instance):
        email = self.email.text.strip()
        password = self.password.text.strip()
        
        if not email or not password:
            self.status_label.text = 'Please fill in all fields'
            self.status_label.color = get_color_from_hex('#F44336')
            return
            
        if self.on_login_success:
            success = self.on_login_success(email, password)
            if success:
                self.status_label.text = 'Login successful!'
                self.status_label.color = get_color_from_hex('#4CAF50')
                # Switch to home screen after successful login
                app = App.get_running_app()
                app.root.current = 'home'
            else:
                self.status_label.text = 'Invalid email or password'
                self.status_label.color = get_color_from_hex('#F44336')

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()