import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

# Placeholder data
INSTRUCTORS = ['Dr. Jood', 'Dr. Smith', 'Dr. Lee']
TIMES = ['10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM']

class OfficeHourApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Office Hours')
        self.geometry('400x700')
        self.configure(bg='white')
        self.resizable(False, False)

        # AppBar
        self.appbar = tk.Frame(self, bg='#AAB0BE', height=60)
        self.appbar.pack(fill='x', side='top')
        self.menu_icon = tk.Label(self.appbar, text='≡', bg='#AAB0BE', fg='white', font=('Arial', 24))
        self.menu_icon.place(x=10, y=10)
        self.title_label = tk.Label(self.appbar, text='Office Hours', bg='#AAB0BE', fg='white', font=('Arial', 24, 'normal'))
        self.title_label.pack(pady=10)

        # Main content
        self.content = tk.Frame(self, bg='white')
        self.content.pack(fill='both', expand=True, padx=16, pady=(8, 0))

        # Instructor dropdown
        tk.Label(self.content, text='Search for Instructor', bg='white', font=('Arial', 14, 'bold')).pack(anchor='w', pady=(16, 0))
        self.instructor_var = tk.StringVar(value=INSTRUCTORS[0])
        self.instructor_menu = ttk.Combobox(self.content, textvariable=self.instructor_var, values=INSTRUCTORS, state='readonly', font=('Arial', 13))
        self.instructor_menu.pack(fill='x', pady=4)

        # Date picker
        tk.Label(self.content, text='Choose a Date', bg='white', font=('Arial', 14, 'bold')).pack(anchor='w', pady=(24, 0))
        self.selected_date = tk.StringVar(value='2024-12-08')
        self.date_frame = tk.Frame(self.content, bg='#6E6B7B', bd=0)
        self.date_frame.pack(fill='x', pady=8)
        self.year_label = tk.Label(self.date_frame, text='2024', bg='#6E6B7B', fg='white', font=('Arial', 14))
        self.year_label.pack(anchor='w')
        self.day_label = tk.Label(self.date_frame, text='Sun, Dec 8', bg='#6E6B7B', fg='white', font=('Arial', 28, 'bold'))
        self.day_label.pack(anchor='w')

        self.calendar = Calendar(self.content, selectmode='day', year=2024, month=12, day=8,
                                mindate=datetime(2024, 12, 1), maxdate=datetime(2024, 12, 31),
                                date_pattern='yyyy-mm-dd')
        self.calendar.pack(pady=4)
        self.calendar.bind('<<CalendarSelected>>', self.update_date)

        # Time dropdown
        time_row = tk.Frame(self.content, bg='white')
        time_row.pack(fill='x', pady=(24, 0))
        tk.Label(time_row, text='Choose a Time', bg='white', font=('Arial', 14, 'bold')).pack(side='left')
        self.time_var = tk.StringVar(value=TIMES[0])
        self.time_menu = ttk.Combobox(time_row, textvariable=self.time_var, values=TIMES, state='readonly', font=('Arial', 13))
        self.time_menu.pack(side='right')

        # Confirm button
        self.confirm_btn = tk.Button(self.content, text='Confirm', font=('Arial', 14), bg='#FFC0CB', fg='black',
                                     relief='flat', bd=0, padx=32, pady=8, command=self.confirm)
        self.confirm_btn.pack(anchor='e', pady=(16, 0))

        # Spacer
        tk.Label(self.content, bg='white').pack(pady=40)

        # Bottom navigation bar
        self.navbar = tk.Frame(self, bg='#FFC0CB', height=80)
        self.navbar.pack(fill='x', side='bottom')
        self.navbar.grid_propagate(False)
        self.add_navbar_buttons()

    def update_date(self, event):
        date_str = self.calendar.get_date()
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        self.year_label.config(text=str(date_obj.year))
        self.day_label.config(text=date_obj.strftime('%a, %b %-d'))

    def confirm(self):
        tk.messagebox.showinfo('Confirmed', f'Instructor: {self.instructor_var.get()}\nDate: {self.calendar.get_date()}\nTime: {self.time_var.get()}')

    def add_navbar_buttons(self):
        icons = ['🏠', '🧑‍💼', '🏛️', '📅']
        for i, icon in enumerate(icons):
            btn = tk.Button(self.navbar, text=icon, font=('Arial', 24), bg='#FFC0CB', fg='white', relief='flat', bd=0)
            btn.grid(row=0, column=i, sticky='nsew', padx=10, pady=10)
        for i in range(4):
            self.navbar.grid_columnconfigure(i, weight=1)

if __name__ == '__main__':
    try:
        import tkcalendar
    except ImportError:
        import sys
        print('tkcalendar not found. Please install it with: pip install tkcalendar')
        sys.exit(1)
    app = OfficeHourApp()
    app.mainloop() 