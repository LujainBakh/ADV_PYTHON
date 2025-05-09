from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.core.window import Window
from datetime import datetime
from kivy.uix.popup import Popup
from kivy_garden.calendar import CalendarWidget

# Instructor names from instructors_screen.py
INSTRUCTORS = [
    "Ms. Amal AlHajri",
    "Ms. Layan AlNahdi",
    "Dr. jood Khalid",
    "Dr. Amjad",
    "Dr. Lujain"
]
TIMES = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM"]

class OfficeHourScreen(MDScreen):
    selected_instructor = StringProperty(INSTRUCTORS[0])
    selected_time = StringProperty(TIMES[0])
    selected_date = StringProperty(datetime(2024, 12, 8).strftime('%a, %b %d'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.layout = MDBoxLayout(orientation='vertical', spacing=dp(8))
        # AppBar
        toolbar = MDTopAppBar(
            title='Office Hours',
            elevation=2,
            left_action_items=[["menu", lambda x: None]],
            md_bg_color=get_color_from_hex('#B0BEC5'),
            specific_text_color=(1,1,1,1),
        )
        self.layout.add_widget(toolbar)
        # Main content
        content = MDBoxLayout(orientation='vertical', padding=[dp(16), dp(8), dp(16), 0], spacing=dp(16))
        # Instructor dropdown
        content.add_widget(MDLabel(text='Search for Instructor', font_style='Subtitle1', bold=True, theme_text_color='Primary'))
        self.instructor_menu = MDDropdownMenu(
            caller=None,
            items=[{"text": name, "on_release": lambda x=name: self.set_instructor(x)} for name in INSTRUCTORS],
            width_mult=4,
        )
        self.instructor_field = MDTextField(
            text=self.selected_instructor,
            hint_text='Select Instructor',
            readonly=True,
            on_focus=self.open_instructor_menu,
            font_size=18,
        )
        content.add_widget(self.instructor_field)
        # Date picker
        content.add_widget(MDLabel(text='Choose a Date', font_style='Subtitle1', bold=True, theme_text_color='Primary'))
        self.date_btn = MDButton(
            text=self.selected_date,
            style="filled",
            md_bg_color=get_color_from_hex('#6E6B7B'),
            text_color=(1,1,1,1),
            font_size=24,
            pos_hint={"center_x": 0.5},
            on_release=self.show_date_picker,
        )
        content.add_widget(self.date_btn)
        # Time dropdown
        time_row = MDBoxLayout(orientation='horizontal', spacing=dp(8), size_hint_y=None, height=dp(48))
        time_row.add_widget(MDLabel(text='Choose a Time', font_style='Subtitle1', bold=True, theme_text_color='Primary'))
        self.time_menu = MDDropdownMenu(
            caller=None,
            items=[{"text": t, "on_release": lambda x=t: self.set_time(x)} for t in TIMES],
            width_mult=3,
        )
        self.time_field = MDTextField(
            text=self.selected_time,
            hint_text='Select Time',
            readonly=True,
            on_focus=self.open_time_menu,
            font_size=18,
        )
        time_row.add_widget(self.time_field)
        content.add_widget(time_row)
        # Confirm button
        self.confirm_btn = MDButton(
            text='Confirm',
            style="filled",
            md_bg_color=get_color_from_hex('#B0BEC5'),
            text_color=(0,0,0,1),
            font_size=18,
            pos_hint={"center_x": 0.9},
            on_release=self.confirm,
        )
        content.add_widget(self.confirm_btn)
        self.layout.add_widget(content)
        # Bottom navigation bar
        nav_bar = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(64),
            padding=[dp(16), dp(8), dp(16), dp(8)],
            spacing=dp(32),
            md_bg_color=get_color_from_hex('#90A4AE'),
        )
        nav_bar.add_widget(MDButton(icon='home', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDButton(icon='account', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDButton(icon='bank', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDButton(icon='calendar', theme_text_color='Custom', text_color=(1,1,1,1)))
        self.layout.add_widget(nav_bar)
        self.add_widget(self.layout)

    def open_instructor_menu(self, instance, value):
        if value:
            self.instructor_menu.caller = self.instructor_field
            self.instructor_menu.open()

    def set_instructor(self, name):
        self.selected_instructor = name
        self.instructor_field.text = name
        self.instructor_menu.dismiss()

    def show_date_picker(self, instance):
        self.calendar_popup = Popup(
            title="Pick a date",
            content=CalendarWidget(on_select=self.on_date_selected),
            size_hint=(0.9, 0.7)
        )
        self.calendar_popup.open()

    def on_date_selected(self, calendar, date):
        # date is a datetime.date object
        self.selected_date = date.strftime('%a, %b %d')
        self.date_btn.text = self.selected_date
        self.calendar_popup.dismiss()

    def open_time_menu(self, instance, value):
        if value:
            self.time_menu.caller = self.time_field
            self.time_menu.open()

    def set_time(self, t):
        self.selected_time = t
        self.time_field.text = t
        self.time_menu.dismiss()

    def confirm(self, instance):
        from kivymd.toast import toast
        toast(f"Confirmed: {self.selected_instructor}, {self.selected_date}, {self.selected_time}")

# For testing
if __name__ == '__main__':
    class TestApp(MDApp):
        def build(self):
            return OfficeHourScreen()
    TestApp().run() 