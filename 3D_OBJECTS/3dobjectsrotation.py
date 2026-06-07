import tkinter as tk
import math

root = tk.Tk()
root.title("3D OBJECTS") #creates gui

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack() #creates canvas


phi = (1 + math.sqrt(5))/2
inv = 1/phi

points = {}
lines = []
current_shape = "" 


objects = {
    "cube": {
        "points": [(1, 1, 1),(1, 1, -1),(1, -1, 1),(1, -1, -1),(-1, 1, 1),(-1, 1, -1),(-1, -1, 1),(-1, -1, -1),],
        "edges": [((-1,-1,-1),(1,-1,-1)),((-1,-1,-1),(-1,1,-1)),((-1,-1,-1),(-1,-1,1)),
                  ((1,1,1),(-1,1,1)),((1,1,1),(1,-1,1)),((1,1,1),(1,1,-1)),
                  ((-1,1,1),(-1,-1,1)),((-1,1,1),(-1,1,-1)),((1,-1,-1),(1,-1,1)),
                  ((1,-1,1),(-1,-1,1)),((1,1,-1),(1,-1,-1)),((1,1,-1),(-1,1,-1)),]
    },
    "octaheron": {"points": [(1, 0, 0),(-1, 0, 0),(0, 1, 0),(0, -1, 0),(0, 0, 1),(0, 0, -1),],
        "edges": [((1, 0, 0), (0, 1, 0)), ((1, 0, 0), (0, -1, 0)), ((1, 0, 0), (0, 0, 1)), ((1, 0, 0), (0, 0, -1)),
    ((-1, 0, 0), (0, 1, 0)), ((-1, 0, 0), (0, -1, 0)), ((-1, 0, 0), (0, 0, 1)), ((-1, 0, 0), (0, 0, -1)),
    ((0, 1, 0), (0, 0, 1)), ((0, 1, 0), (0, 0, -1)), ((0, -1, 0), (0, 0, 1)), ((0, -1, 0), (0, 0, -1))]
    },
    "dodecahedron": {"points": [(0, inv, phi),(0, -inv, phi),(0, inv, -phi),(0, -inv, -phi),
                          (inv, phi, 0),(-inv, phi, 0),(inv, -phi, 0),(-inv, -phi, 0),
                          (phi, 0, inv),(-phi, 0, inv),(phi, 0, -inv),(-phi, 0, -inv)],
        "edges": [((0, inv, phi), (0, -inv, phi)), ((0, inv, -phi), (0, -inv, -phi)),
    ((inv, phi, 0), (-inv, phi, 0)), ((inv, -phi, 0), (-inv, -phi, 0)),
    ((phi, 0, inv), (phi, 0, -inv)), ((-phi, 0, inv), (-phi, 0, -inv)),
    ((0, inv, phi), (inv, phi, 0)), ((0, inv, phi), (-inv, phi, 0)),
    ((0, inv, phi), (phi, 0, inv)), ((0, inv, phi), (-phi, 0, inv)),
    ((0, -inv, phi), (inv, -phi, 0)), ((0, -inv, phi), (-inv, -phi, 0)),
    ((0, -inv, phi), (phi, 0, inv)), ((0, -inv, phi), (-phi, 0, inv)),
    ((0, inv, -phi), (inv, phi, 0)), ((0, inv, -phi), (-inv, phi, 0)),
    ((0, inv, -phi), (phi, 0, -inv)), ((0, inv, -phi), (-phi, 0, -inv)),
    ((0, -inv, -phi), (inv, -phi, 0)), ((0, -inv, -phi), (-inv, -phi, 0)),
    ((0, -inv, -phi), (phi, 0, -inv)), ((0, -inv, -phi), (-phi, 0, -inv)),
    ((inv, phi, 0), (phi, 0, inv)), ((inv, phi, 0), (phi, 0, -inv)),
    ((-inv, phi, 0), (-phi, 0, inv)), ((-inv, phi, 0), (-phi, 0, -inv)),
    ((inv, -phi, 0), (phi, 0, inv)), ((inv, -phi, 0), (phi, 0, -inv)),
    ((-inv, -phi, 0), (-phi, 0, inv)), ((-inv, -phi, 0), (-phi, 0, -inv))]} # uhh
}

def change_shape(shape_name):
    global current_shape
    current_shape = shape_name
    
    # Réinitialisation complète (Interface + Listes Python)
    sliderPITCH.set(0)
    sliderYAW.set(0)
    sliderROLL.set(0)
    canvas.delete("all")
    points.clear()
    lines.clear()
    
    # Création des points graphiques
    for p in objects[current_shape]["points"]:
        points[p] = canvas.create_oval(0, 0, 0, 0)
        
    # Création des lignes graphiques
    for edge in objects[current_shape]["edges"]:
        lines.append(canvas.create_line(0, 0, 0, 0))
        
    update()

def update(_=None):

    pitch = math.radians(sliderPITCH.get())
    yaw = math.radians(sliderYAW.get())
    roll = math.radians(sliderROLL.get())#takes value from sliders

    transformed = {}

    for (x, y, z), point_id in points.items():

        x_2d = 300 + ((x*math.cos(yaw)+z*math.sin(yaw))*math.cos(roll)-(y*math.cos(pitch)+x*math.sin(yaw)*math.sin(pitch)-z*math.cos(yaw)*math.sin(pitch))*math.sin(roll))*100 # calculates x values of the points
        y_2d = 200 + ((x*math.cos(yaw)+z*math.sin(yaw))*math.sin(roll)+(y*math.cos(pitch)+x*math.sin(yaw)*math.sin(pitch)-z*math.cos(yaw)*math.sin(pitch))*math.cos(roll))*100 # calculates y values of the points

        canvas.coords(
            point_id,
            x_2d - 4,
            y_2d - 4,
            x_2d + 4,
            y_2d + 4
        )   # adjusts the coordinates to the canvas
        transformed[(x,y,z)] = (x_2d, y_2d)

    for i, (a, b) in enumerate(objects[current_shape]["edges"]):
        x1, y1 = transformed[a]
        x2, y2 = transformed[b]

        canvas.coords(lines[i], x1, y1, x2, y2)
    
button_cube = tk.Button(root, text="cube", command=lambda: change_shape("cube"))
button_octahedron = tk.Button(root, text="octahedron",command=lambda: change_shape("octaheron"))
button_dodecahedron = tk.Button(root, text="dodecahedron",command=lambda: change_shape("dodecahedron")) #buttons to show geometrical shapes

button_cube.pack()
button_octahedron.pack()
button_dodecahedron.pack()

sliderPITCH = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update)
sliderYAW = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update)
sliderROLL = tk.Scale(root,from_=0,to=360,orient="horizontal",command=update) # creates the sliders

sliderPITCH.pack()
sliderYAW.pack()
sliderROLL.pack()

root.mainloop() #runs the gui or idk
#this all started from geometry dash...
