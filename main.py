import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, BOTH, X, Label, Entry, Frame, Button, messagebox
from traffic import Traffic

width = 300
height = 200
userId = "admin"
password = "1234"

class Application:
    def __init__(self, master):
        self.master = master
        self.topFrame = Frame(master, height=200, bg="white")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(master, height=600, bg="#f0eec5")
        self.bottomFrame.pack(fill=X)

        self.label1 = Label(self.topFrame, text="TRAFFIC MANAGEMENT SYSTEM", font="BodoniMTBlack 40 bold", bg="white", fg="blue")
        self.label1.place(x=350, y=70)

        self.name = Label(self.bottomFrame, text="NAME: ", font="arial 11 bold", bg="#f0eec5", fg="black")
        self.name.place(x=550, y=210)
        self.password = Label(self.bottomFrame, text="PASSWORD:", font="arial 11 bold", bg="#f0eec5", fg="black")
        self.password.place(x=550, y=240)

        # Load and display image
        try:
            image = Image.open('picture.png')
            image = image.resize((150, 150), Image.LANCZOS)
            img_pro = ImageTk.PhotoImage(image)
            self.label_pic = Label(self.bottomFrame, image=img_pro, background="#f0eec5")
            self.label_pic.image = img_pro
            self.label_pic.place(x=630, y=10)
        except Exception as e:
            print(f"Error loading image: {e}")

        # Entry fields
        self.name1 = tk.StringVar()
        self.pwd1 = tk.StringVar()
        self.entry_name = Entry(self.bottomFrame, textvariable=self.name1)
        self.entry_name.place(x=650, y=210, width=120, height=20)

        self.entry_pwd = Entry(self.bottomFrame, show="*", textvariable=self.pwd1)
        self.entry_pwd.place(x=650, y=240, width=120, height=20)

        # Login button
        self.button_register = Button(self.bottomFrame, text="ENTER", font="arial 16 bold", fg="red", command=self.getThere)
        self.button_register.place(x=660, y=300)

    def getThere(self):
        if self.name1.get() != userId or self.pwd1.get() != password:
            messagebox.showinfo("Login Error", "Wrong Username or Password Entered. Can't Proceed Further")
        else:
            Traffic()


def main():
    root = tk.Tk()
    app = Application(root)
    root.title("LOGIN PAGE")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()


if __name__ == "__main__":
    main()
