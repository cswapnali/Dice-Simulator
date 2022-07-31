import tkinter as tk
import random
import tkinter.font as font

def roll_dice():
    #Unicode values for the face of dice
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result = random.choice(value)
    label1.configure(text = result)
    label1.pack()
    
    if (result == '\u2680'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)
    elif (result == '\u2681'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)
    elif (result == '\u2682'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)
    elif (result == '\u2683'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)
    elif (result == '\u2684'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)
    elif (result == '\u2685'):
        label2 = tk.Label(canvas)
        label2.place(x=100,y=250)

canvas = tk.Tk()
canvas.geometry('400x400')
canvas.maxsize(400, 400)
canvas.title('Rolling Dice')

#label to print result
label1 = tk.Label(canvas, text='', font = ('Arial', 300))

myfont = font.Font(family = ('Arial', 15))
button = tk.Button(canvas, text='Roll Dice', height=2, width=10, bg='blue', fg='#ffffff', command = roll_dice)
button['font'] = myfont
button.place(x=150, y=20)

canvas.mainloop()

