from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from src.ui.bottom_nav import BottomNav
from kivy.utils import get_color_from_hex

class GPACalculatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.courses = []
        
        # Main layout
        main_box = MDBoxLayout(orientation='vertical')
        
        # Top bar with menu and title
        top_bar = MDBoxLayout(
            size_hint_y=None,
            height=dp(60),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            padding=[dp(10), 0, 0, 0]
        )
        menu_button = MDIconButton(
            icon="menu",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        title = MDLabel(
            text="GPA Calculator",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        top_bar.add_widget(menu_button)
        top_bar.add_widget(title)
        
        # Content layout
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(16),
            spacing=dp(10)
        )
        
        # Input fields
        self.course_name = MDTextField(
            hint_text="Course Name",
            mode="rectangle",
            size_hint_y=None,
            height=dp(48)
        )
        
        self.grade = MDTextField(
            hint_text="Select Grade",
            mode="rectangle",
            readonly=True,
            size_hint_y=None,
            height=dp(48)
        )
        
        grade_items = [
            {
                "text": grade,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=grade: self.set_grade(x),
            } for grade in ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
        ]
        
        self.grade_menu = MDDropdownMenu(
            caller=self.grade,
            items=grade_items,
            width_mult=4,
        )
        
        self.grade.bind(focus=self.open_grade_menu)
        
        self.credits = MDTextField(
            hint_text="Credits (e.g., 3)",
            mode="rectangle",
            size_hint_y=None,
            height=dp(48)
        )
        
        # Buttons
        add_button = MDRaisedButton(
            text="Add Course",
            size_hint=(1, None),
            height=dp(50),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            on_release=self.add_course
        )
        
        calculate_button = MDRaisedButton(
            text="Calculate GPA",
            size_hint=(1, None),
            height=dp(50),
            md_bg_color=get_color_from_hex('#A9BCBD'),
            on_release=self.calculate_gpa
        )
        
        self.courses_list = MDLabel(
            text="",
            size_hint_y=None,
            height=dp(100)
        )
        
        self.gpa_result = MDLabel(
            text="Your GPA: --",
            size_hint_y=None,
            height=dp(50)
        )
        
        # Add all elements to layouts
        content.add_widget(self.course_name)
        content.add_widget(self.grade)
        content.add_widget(self.credits)
        content.add_widget(add_button)
        content.add_widget(calculate_button)
        content.add_widget(self.courses_list)
        content.add_widget(self.gpa_result)
        
        main_box.add_widget(top_bar)
        main_box.add_widget(content)
        main_box.add_widget(BottomNav())  # Add the reusable bottom navigation
        
        self.add_widget(main_box)

    def open_grade_menu(self, instance, value):
        if value:
            self.grade_menu.open()

    def set_grade(self, grade):
        self.grade.text = grade
        self.grade_menu.dismiss()
        
    def add_course(self, instance):
        try:
            if not self.course_name.text or not self.grade.text or not self.credits.text:
                self.gpa_result.text = "Please fill all fields"
                return

            course = {
                'name': self.course_name.text,
                'grade': self.grade.text,
                'credits': float(self.credits.text)
            }
            self.courses.append(course)
            
            # Update courses list display
            current_text = self.courses_list.text
            new_course = f"{course['name']} - Grade: {course['grade']}, Credits: {course['credits']}\n"
            self.courses_list.text = current_text + new_course
            
            # Clear input fields
            self.course_name.text = ""
            self.grade.text = ""
            self.credits.text = ""
            
        except ValueError:
            self.gpa_result.text = "Please enter valid values"
    
    def calculate_gpa(self, instance):
        if not self.courses:
            self.gpa_result.text = "Please add courses first"
            return
            
        grade_points = {
            'A+': 5.0, 'A': 4.7, 
            'B+': 4.3, 'B': 4.0,
            'C+': 3.3, 'C': 3.0,
            'D+': 2.3, 'D': 2.0,
            'F': 0.0
        }
        
        total_points = 0
        total_credits = 0
        
        for course in self.courses:
            if course['grade'] in grade_points:
                points = grade_points[course['grade']] * course['credits']
                total_points += points
                total_credits += course['credits']
            
        if total_credits > 0:
            gpa = total_points / total_credits
            self.gpa_result.text = f"Your GPA: {gpa:.2f}"
        else:
            self.gpa_result.text = "Error calculating GPA"