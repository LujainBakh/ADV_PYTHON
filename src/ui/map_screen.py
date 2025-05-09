from kivy_garden.mapview import MapView, MapMarkerPopup
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from src.ui.bottom_nav import BottomNav
from kivy.uix.label import Label

class MapScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'map'

        # Main layout
        main_layout = MDBoxLayout(orientation='vertical')

        # Top Bar
        top_bar = MDBoxLayout(
            size_hint_y=None,
            height=dp(48),
            md_bg_color=get_color_from_hex('#B0BEC5'),  # Light blue-gray color
            padding=[dp(10), 0, 0, 0]
        )

        back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(0, 0, 0, 0.8),  # Dark gray
            on_release=self.go_back
        )

        title = MDLabel(
            text="Map",
            theme_text_color="Custom",
            text_color=(0, 0, 0, 0.8),  # Dark gray
            font_style="H6"
        )

        top_bar.add_widget(back_button)
        top_bar.add_widget(title)

        # Interactive MapView
        self.map_view = MapView(
            zoom=15,
            lat=26.3927,    # Center on IAU
            lon=50.1927,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # IAU Campus locations
        locations = [
            ("IAU Entrance", 26.3927, 50.1927),
            ("Building 10", 26.3919, 50.1920),
            ("College of Design", 26.3923, 50.1905),
            ("A47", 26.3912, 50.1904),
            ("IELTS Center", 26.3909, 50.1907),
            ("Building 45", 26.3905, 50.1926),
            ("Building 450", 26.3907, 50.1899),
        ]

        # Add markers with popups
        for name, lat, lon in locations:
            marker = MapMarkerPopup(lat=lat, lon=lon)
            marker.add_widget(Label(text=name, color=(0, 0, 0, 1)))
            self.map_view.add_widget(marker)

        # Map container
        map_container = MDBoxLayout(size_hint_y=0.9)
        map_container.add_widget(self.map_view)

        # Bottom navigation
        bottom_nav = MDBoxLayout(
            size_hint_y=None,
            height=dp(56),
            md_bg_color=(1, 1, 1, 0.9),
            spacing="40dp",
            padding=["20dp", "10dp", "20dp", "10dp"]
        )

        # Navigation icons
        nav_icons = [
            {"icon": "home", "text": "Home"},
            {"icon": "account-group", "text": "Community"},
            {"icon": "bank", "text": "University"},
            {"icon": "calendar", "text": "Calendar"}
        ]

        for item in nav_icons:
            button = MDIconButton(
                icon=item["icon"],
                theme_text_color="Custom",
                text_color=get_color_from_hex('#757575'),
                size_hint_x=None,
                width="48dp"
            )
            bottom_nav.add_widget(button)

        # Add all elements to main layout
        main_layout.add_widget(top_bar)
        main_layout.add_widget(map_container)
        main_layout.add_widget(bottom_nav)

        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.current = 'home' 