from tkinter import *
from tkinter import ttk

from twitterbot import PersonalBot


class BotFrame(ttk.Frame, PersonalBot):
    def __init__(self, master: Tk, keys: dict, **kw):
        super().__init__(master, **kw)
        PersonalBot.__init__(self, keys)

        self.labels = {}
        self.entries = {}

        self.show_widgets()

    def show_widgets(self):
        for key in self.label_texts[:3]:
            self.labels[key] = ttk.Label(self, text=key)
            self.entries[key] = ttk.Entry(self, width=20)
            self.labels[key].pack(padx=10, anchor='w')
            self.entries[key].pack(padx=10, pady=2)
        for key in self.label_texts[3:]:
            self.entries[key] = IntVar()
            check_button = ttk.Checkbutton(self, text=key, variable=self.entries[key])
            check_button.pack(padx=30, pady=3, anchor='w')

        button = ttk.Button(self, text="Submit", command=self.main_function)
        button.pack(padx=5, pady=5)

    def retrieve_answers(self):
        for key in self.label_texts:
            self.answers[key] = self.entries[key].get()
        print(self.answers)
