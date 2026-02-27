#Quatisha Poston
#assignment 3

import tkinter as tk
from tkinter import messagebox

#setting up the main window
root = tk.Tk()
root.title("Personal Information Form")
root.geometry("500x300")  # keeping the window size simple and fixed

#label frame to hold all the personal info stuff
lblFrPerson = tk.LabelFrame(root, text="Personal Information")
lblFrPerson.pack(padx=10, pady=10, fill="both", expand=True)

#required fields get an asterisk and some color so they stand out
lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white")
lblFirst.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(row=0, column=1, padx=5, pady=5)

lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white")
lblLast.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entLast = tk.Entry(lblFrPerson)
entLast.grid(row=1, column=1, padx=5, pady=5)

#these ones aren’t required, so no special styling
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entEmail = tk.Entry(lblFrPerson)
entEmail.grid(row=2, column=1, padx=5, pady=5)

lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entPhone = tk.Entry(lblFrPerson)
entPhone.grid(row=3, column=1, padx=5, pady=5)

#runs when the Submit button is clicked
def displayData():
    # grab whatever the user typed in
    first = entFirst.get().strip()
    last = entLast.get().strip()
    email = entEmail.get().strip()
    phone = entPhone.get().strip()

    
    fullName = f"{first} {last}".strip()

    #quick check to make sure required fields aren’t empty
    #(your instructor said this check was optional; keeping it is fine)
    if first == "" or last == "":
        messagebox.showerror(
            "Missing Required Fields",
            "Please enter First Name and Last Name."
        )
        return

    #putting everything together for the message box
    info_message = (
        f"Full Name: {fullName}\n"
        f"Email: {email}\n"
        f"Phone: {phone}"
    )

    messagebox.showinfo("Personal Information", info_message)

#clears all the entry boxes
def Clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

#frame just for the buttons at the bottom
fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)

#buttons are packed side by side
btnS = tk.Button(fraButtons, text="Submit", width=8, command=displayData)
btnS.pack(side=tk.LEFT, padx=5)

btnR = tk.Button(fraButtons, text="Reset", width=8, command=Clear)
btnR.pack(side=tk.LEFT, padx=5)

#quit button just closes the window
btnQ = tk.Button(fraButtons, text="Quit", width=8, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=5)

#keeps the window open and listening for clicks
root.mainloop()
