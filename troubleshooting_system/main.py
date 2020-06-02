import troubleshooting_system.ui_layer.start_window as ww
from tkinter import *
from PIL import ImageTk, Image


def call_window(window):
    app = ww.WelcomeWindow(window)
    app.pack()


if __name__ == "__main__":
    root = Tk()
    call_window(root)
    canvas = Canvas(root, width=650, height=450)
    img = ImageTk.PhotoImage(Image.open('E:\\Project\\Automated-troubleshooting-system\\troubleshooting_system'
                                        '\\images_layer\\background.jpg'))
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.pack()
    root.mainloop()
