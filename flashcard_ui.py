from tkinter import *
from tkinter import messagebox

GREEN = "#DDF6D2"
FONT = ("Ariel", 40, "italic")

class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcard App")
        self.window.config(padx=50, pady=50, bg=GREEN)

        self.canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
        try:
            self.flashcard_front = PhotoImage(file="images/card_front.png")
            self.flashcard_back = PhotoImage(file="images/card_back.png")
        except TclError:
            messagebox.showerror(title="Error", message="Image files not found. Please check your image paths.")
            self.window.destroy()
            return

        self.current_side = self.canvas.create_image(400, 263)
        self.card_title = self.canvas.create_text(400, 150, font=FONT)
        self.card_word = self.canvas.create_text(400, 300, font=FONT)
        self.canvas.grid(row=0, columnspan=2, column=0)

        self.right_image = PhotoImage(file="images/right.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(row=1, column=1)

        self.wrong_image = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=1, column=0)

