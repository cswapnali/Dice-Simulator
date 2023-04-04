import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry('300x300')
window.title('Dice Simulator')

dice = [r'Images\1.png', r'Images\2.png', r'Images\3.png', r'Images\4.png', r'Images\5.png', r'Images\6.png']
image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label = tk.Label(window, image=image)

label.image = image

label.place(x=90, y=75)
def dice_roll():
    image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label.configure(image=image)
    label.image= image
    
button = tk.Button(window, text='ROLL', bg='blue', fg='white', font='Times 15 bold', command=dice_roll)
button.place(x=110, y=230)
window.mainloop()