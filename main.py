import json
from tkinter import *

from botframe import BotFrame


def main():
    with open('keys.json', 'r') as f:
        keys = json.load(f)

    root = Tk()
    root.title('Twitter bot')

    gui = BotFrame(root, keys, padding="3 3 12 12")
    gui.pack()
    gui.mainloop()


if __name__ == '__main__':
    main()
