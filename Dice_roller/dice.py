import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["./assets/dice.png", "./assets/dice (1).png", "./assets/dice (2).png", "./assets/dice (3).png", "./assets/dice (4).png", "./assets/dice (5).png", "./assets/dice (6).png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x=30, y=100)
label2.place(x=300, y=100)

def dice_roll():
    new_image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=new_image1)
    label1.image = new_image1

    new_image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=new_image2)
    label2.image = new_image2

button = tk.Button(window, text="ROLL", bg="green", fg="white", font="Times 20 bold", command=dice_roll)
button.place(x=200, y=0)

window.mainloop()
