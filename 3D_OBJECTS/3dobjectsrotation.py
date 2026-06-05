import tkinter as tk
import math

root = tk.Tk()
root.title("3D OBJECTS") #creates gui

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack() #creates canvas
points = {}

for x in (-1, 1):
    for y in (-1, 1):
        for z in (-1, 1):
            points[(x,y,z)] = canvas.create_oval(295,195,305,205) #creates points 

def update(_=None):
    pitch = math.radians(sliderPITCH.get())
    yaw = math.radians(sliderYAW.get())
    roll = math.radians(sliderROLL.get()) #takes value from sliders

    for (x, y, z), point_id in points.items():

        x_2d = 300 + ((x*math.cos(yaw)+z*math.sin(yaw))*math.cos(roll)-(y*math.cos(pitch)+x*math.sin(yaw)*math.sin(pitch)-z*math.cos(yaw)*math.sin(pitch))*math.sin(roll))*100 # calculates x values of the points
        y_2d = 200 + ((x*math.cos(yaw)+z*math.sin(yaw))*math.sin(roll)+(y*math.cos(pitch)+x*math.sin(yaw)*math.sin(pitch)-z*math.cos(yaw)*math.sin(pitch))*math.cos(roll))*100 # calculates y values of the points

        canvas.coords(
            point_id,
            x_2d - 4,
            y_2d - 4,
            x_2d + 4,
            y_2d + 4
        ) # adjusts the coordinates to the canvas

sliderPITCH = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update)
sliderYAW = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update)
sliderROLL = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update) # creates the sliders

sliderPITCH.pack()
sliderYAW.pack()
sliderROLL.pack()

root.mainloop() #runs the gui or idk
