from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import webbrowser

class InstructorsScreen(MDScreen):
    search_text = StringProperty("")
    instructors = ListProperty([
        {
            "name": "Ms. Amal AlHajri",
            "title": "PhD in AI, Expert in Data Science and Machine Learning.",
            "location": "Building 650, Second floor no.205-H",
            "hours": "Mon & Wed, 10:00 AM - 12:00 PM",
            "email": "amal.hajri@example.com"
        },
        {
            "name": "Ms. Layan AlNahdi",
            "title": "MSc in Software Engineering, Researcher in Cloud Computing.",
            "location": "Building 650, First floor no.104-B",
            "hours": "Tue & Thu, 1:00 PM - 3:00 PM",
            "email": "layan.nahdi@example.com"
        },
        {
            "name": "Dr. jood Khalid ",
            "title": "CodEd Senior member",
            "location": "IAU, A11, second floor B125",
            "hours": "Mon & Thu, 10:00 AM - 12:00 PM",
            "email": "jood.@example.com"
        },
        {
            "name": "Dr. Amjad ",
            "title": "the best coder ever",
            "location": "IAU, A11, B123",
            "hours": "Mon & Thu, 8:00 AM - 10:00 AM",
            "email": "amjad@example.com"
        }, 
        {
            "name": "Dr. Lujain ",
            "title": "the best Leader ever",
            "location": "IAU, A11, B123",
            "hours": "Mon & Thu, 12:00 PM - 2:00 PM",
            "email": "lujain@example.com"
        }
    ])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.96, 0.98, 0.98, 1)
        self.layout = MDBoxLayout(orientation='vertical', spacing=dp(8))
        # Top App Bar
        toolbar = MDTopAppBar(
            title='Instructors',
            elevation=2,
            left_action_items=[["menu", lambda x: None]],
            md_bg_color=get_color_from_hex('#B0BEC5'),
            specific_text_color=(1,1,1,1),
        )
        self.layout.add_widget(toolbar)
        # Search Bar
        self.search = MDTextField(
            hint_text='Search by Instructor Name',
            size_hint_x=1,
            mode='rectangle',
            pos_hint={'center_x': 0.5},
            text_color_focus=get_color_from_hex('#607D8B'),
            fill_color_normal=(1,1,1,1),
            fill_color_focus=(1,1,1,1),
            icon_right='magnify',
            size_hint_y=None,
            height=dp(48),
            padding=[dp(12), 0, 0, 0],
        )
        self.search.bind(text=self.on_search_text)
        self.layout.add_widget(self.search)
        # Instructors List
        from kivy.uix.scrollview import ScrollView
        self.cards_box = MDBoxLayout(orientation='vertical', spacing=dp(20), padding=[dp(8), dp(8), dp(8), dp(8)], size_hint_y=None)
        self.cards_box.bind(minimum_height=self.cards_box.setter('height'))
        self.scroll = ScrollView(size_hint=(1, 1))
        self.scroll.add_widget(self.cards_box)
        self.layout.add_widget(self.scroll)
        # Floating Bottom Navigation
        nav_bar = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(64),
            padding=[dp(16), dp(8), dp(16), dp(8)],
            spacing=dp(32),
            md_bg_color=get_color_from_hex('#90A4AE'),
        )
        nav_bar.add_widget(MDIconButton(icon='home', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDIconButton(icon='account', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDIconButton(icon='bank', theme_text_color='Custom', text_color=(1,1,1,1)))
        nav_bar.add_widget(MDIconButton(icon='calendar', theme_text_color='Custom', text_color=(1,1,1,1)))
        self.layout.add_widget(nav_bar)
        self.add_widget(self.layout)
        self.update_instructor_cards()

    def update_instructor_cards(self):
        self.cards_box.clear_widgets()
        filter_text = self.search.text.strip().lower()
        for instructor in self.instructors:
            if filter_text in instructor["name"].lower():
                self.cards_box.add_widget(self.create_instructor_card(**instructor))

    def on_search_text(self, instance, value):
        self.update_instructor_cards()

    def on_email_press(self, instance, ref):
        # ref is the email address
        webbrowser.open(f"mailto:{ref}")

    def create_instructor_card(self, name, title, location, hours, email):
        card = MDCard(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(300),
            padding=[dp(16), dp(24), dp(16), dp(24)],
            radius=[dp(20)],
            elevation=8,
            md_bg_color=get_color_from_hex('#F5F5F5'),  # lighter grey
        )
        box = MDBoxLayout(orientation='vertical', spacing=dp(10))
        # Avatar centered inside the card
        avatar_layout = AnchorLayout(anchor_x='center', anchor_y='top', size_hint_y=None, height=dp(90), padding=[0, dp(24), 0, 0])
        avatar = MDIconButton(icon='account-circle', icon_size="72sp", theme_text_color='Custom', text_color=get_color_from_hex('#B0BEC5'), disabled=True)
        avatar_layout.add_widget(avatar)
        box.add_widget(avatar_layout)
        # Name
        box.add_widget(MDLabel(text=f"[b]{name}[/b]", markup=True, halign='center', font_style='H6', theme_text_color='Custom', text_color=get_color_from_hex('#263238'), size_hint_y=None, height=dp(32)))
        # Title
        box.add_widget(MDLabel(text=title, halign='center', font_style='Body2', theme_text_color='Custom', text_color=get_color_from_hex('#263238'), size_hint_y=None, height=dp(28)))
        # Info rows (location, hours, email)
        def info_row(icon, text, color, is_email=False):
            row = MDBoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(28), padding=[0,0,0,0])
            row.add_widget(MDIconButton(icon=icon, theme_text_color='Custom', text_color=color, icon_size="22sp", disabled=True, pos_hint={'center_y': 0.5}))
            if is_email:
                email_label = MDLabel(
                    text=f"[ref={email}][color=#2196F3]{email}[/color][/ref]",
                    markup=True,
                    halign='left',
                    valign='middle',
                    font_style='Caption',
                    theme_text_color='Custom',
                    text_color=color,
                    size_hint_y=None,
                    height=dp(24),
                )
                email_label.bind(on_ref_press=self.on_email_press)
                row.add_widget(email_label)
            else:
                row.add_widget(MDLabel(text=text, halign='left', valign='middle', font_style='Caption', theme_text_color='Custom', text_color=color, size_hint_y=None, height=dp(24)))
            return row
        box.add_widget(info_row('map-marker', location, get_color_from_hex('#263238')))
        box.add_widget(info_row('clock-outline', hours, get_color_from_hex('#263238')))
        box.add_widget(info_row('email-outline', email, get_color_from_hex('#2196F3'), is_email=True))
        card.add_widget(box)
        return card

# For testing
if __name__ == '__main__':
    from kivymd.app import MDApp
    class TestApp(MDApp):
        def build(self):
            return InstructorsScreen()
    TestApp().run() 