import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("330x400")

# Entry field (display)
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, ipady = 10)

# Button click function
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# GIF overlay
gif_label = tk.Label(root, bg="white")
gif_label.place(x=65, y=80)  # center position
gif_label.lower()  # hidden initially

# Load GIF
gif = Image.open("funny.gif")

frames = [
    ImageTk.PhotoImage(frame.resize((196, 280)))
    for frame in ImageSequence.Iterator(gif)
]

gif_index = 0
gif_running = False

def show_gif_overlay():
    global gif_index, gif_running

    gif_running = True
    gif_label.lift()

    def animate():
        global gif_index

        if not gif_running:
            return
        
        gif_label.config(image=frames[gif_index])
        gif_index = (gif_index + 1) % len(frames)

        root.after(40, animate)

    animate()

def hide_gif_overlay():
    global gif_running
    gif_running = False
    gif_label.lower()

# Clear function
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)

        show_gif_overlay()
        root.after(2000, hide_gif_overlay)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

        show_gif_overlay()
        root.after(2000, hide_gif_overlay)
    
# Calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)

        show_gif_overlay()
        
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        show_gif_overlay()

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        cmd = clear
    elif text == "=":
        cmd = equal
    else:
        cmd = lambda t=text: click(t)

    tk.Button(root, text=text, width=5, height=4,
              command=cmd).grid(row=row, column=col)

root.mainloop()
