import tkinter as tk
import subprocess
import sys
import os

gui = tk.Tk()
gui.geometry('250x250')
gui.title("Choose the app you want to use")

def NumberRecognition():
    base_path = os.path.dirname(__file__)
    script_path = os.path.join(base_path, 'DigitCaligraphicalRecognitionAI', 'GUI.py')
    subprocess.Popen([sys.executable, script_path])

button_ai = tk.Button(text='Number recognition AI', width=20, height=3,command=NumberRecognition)
button_maze = tk.Button(text='Maze solver', width=20, height=3)
button_penalty = tk.Button(text='Penalty Takes Data Analysis', width=20, height=3)

button_ai.pack(pady=10)
button_maze.pack(pady=10)
button_penalty.pack(pady=10)

gui.mainloop()
