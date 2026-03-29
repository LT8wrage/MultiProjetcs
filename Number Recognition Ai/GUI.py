import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import keras

model = keras.saving.load_model('my_model.keras')

pil_image = Image.new("RGB", (400, 400), "BLACK")
pil_draw = ImageDraw.Draw(pil_image)

gui = tk.Tk()
gui.title("Digit Recognition")
gui.geometry("500x600")

title = tk.Label(gui, text='Draw a number')

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="white", outline="white")
    pil_draw.ellipse([x - 8, y - 8, x + 8, y + 8], fill="white", outline="white")

def clear():
    canvas.delete("all")
    pil_draw.rectangle([0, 0, 400, 400], fill="black") 
    title.config(text="Draw a number")

def submit():
    small_image = pil_image.resize((28, 28))
    small_image.save('28x28.png')
    final_input = (np.array(small_image.convert('L')).astype('float32') / 255.0).reshape(1, 28, 28, 1)
    
    prediction = model.predict(final_input)
    digit = np.argmax(prediction)
    title.config(text=f"Your digit is a : {digit}")



canvas = tk.Canvas(gui, width=400, height=400, bg="black")
Submit_btn = tk.Button(gui, text="Submit", width=10, height=2, command=submit)
Clear_btn = tk.Button(gui, text="Clear", width=10, height=2, command=clear)





canvas.bind("<B1-Motion>", draw)

title.pack(pady=30)
canvas.pack(pady=10)
Submit_btn.pack(ipadx=100)
Clear_btn.pack()
gui.mainloop()

