#Quatisha Poston
#Assignment 4
#Feb 23rd, 2026


from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


class FoodViewerApp:
    def __init__(self):

        self.root = Tk()
        self.root.title("Food Viewer")

        self.root.geometry("400x380")
        self.root.resizable(False, False)

        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack(side="bottom", pady=8)

        self.img_frame = Frame(self.root)
        self.img_frame.pack(side="top", fill="both", expand=True)

        display_w = 400
        display_h = 300
        
        try:

            self.img1 = Image.open("chicken.jpg").resize((display_w, display_h))
            self.imgOne = ImageTk.PhotoImage(self.img1)

            self.img2 = Image.open("pie.jpg").resize((display_w, display_h))
            self.imgTwo = ImageTk.PhotoImage(self.img2)

            self.img3 = Image.open("pizza.jpg").resize((display_w, display_h))
            self.imgThree = ImageTk.PhotoImage(self.img3)

            self.img4 = Image.open("steak.jpg").resize((display_w, display_h))
            self.imgFour = ImageTk.PhotoImage(self.img4)

        except FileNotFoundError:
            messagebox.showerror(
                "Missing Image Files",
                "I couldn't find one or more image files.\n\n"
                "Make sure these are in the SAME folder as asn4.py:\n"
                "chicken.jpg, pie.jpg, pizza.jpg, steak.jpg"
            )
            self.root.destroy()
            return

        
        self.var = IntVar()
        self.var.set(1)

        
        self.lbl = Label(self.img_frame, image=self.imgOne)
        self.lbl.pack(fill="both", expand=True)

        
        self.radio_a = Radiobutton(
            self.rbdBtn_frame,
            text="Chicken",
            variable=self.var,
            value=1,
            command=self.on_radio_select
        )
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = Radiobutton(
            self.rbdBtn_frame,
            text="Pie",
            variable=self.var,
            value=2,
            command=self.on_radio_select
        )
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = Radiobutton(
            self.rbdBtn_frame,
            text="Pizza",
            variable=self.var,
            value=3,
            command=self.on_radio_select
        )
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = Radiobutton(
            self.rbdBtn_frame,
            text="Steak",
            variable=self.var,
            value=4,
            command=self.on_radio_select
        )
        self.radio_d.pack(side="left", padx=10)

        self.root.mainloop()

    
    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.lbl.config(image=self.imgOne)
            self.lbl.image = self.imgOne
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
            self.lbl.image = self.imgTwo
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
            self.lbl.image = self.imgThree
        elif choice == 4:
            self.lbl.config(image=self.imgFour)
            self.lbl.image = self.imgFour


if __name__ == "__main__":
    FoodViewerApp()
