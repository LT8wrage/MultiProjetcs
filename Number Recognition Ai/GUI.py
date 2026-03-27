import tkinter as tk
from PIL import Image, ImageDraw
import io

class DrawingApp:
    def __init__(self, root, on_submit=None):
        self.root = root
        self.root.title("Digit Recognition")
        self.root.geometry("500x600")
        self.on_submit = on_submit
        self.drawn_image = None
        
        # Canvas size (28x28 like MNIST but scaled up for drawing)
        self.canvas_size = 400
        self.draw_color = "white"
        self.bg_color = "black"
        self.brush_width = 5
        
        # Create main frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title label
        title = tk.Label(main_frame, text="Draw a Digit (0-9)", 
                        font=("Arial", 14, "bold"))
        title.pack(pady=5)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(
            main_frame,
            width=self.canvas_size,
            height=self.canvas_size,
            bg=self.bg_color,
            cursor="cross",
            relief=tk.SUNKEN,
            bd=2
        )
        self.canvas.pack(pady=10)
        
        # Bind mouse events for drawing
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        
        self.last_x = None
        self.last_y = None
        
        # Button frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_canvas,
                             width=15, height=2)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Submit button
        submit_btn = tk.Button(button_frame, text="Submit", command=self.submit_drawing,
                              width=15, height=2)
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status = tk.Label(main_frame, text="Ready to draw", 
                              font=("Arial", 9))
        self.status.pack(pady=5)
    
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
    
    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=self.draw_color, width=self.brush_width, capstyle=tk.ROUND, smooth=True
            )
        self.last_x = event.x
        self.last_y = event.y
    
    def end_draw(self, event):
        self.last_x = None
        self.last_y = None
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.status.config(text="Canvas cleared")
        self.drawn_image = None
    
    def get_canvas_image(self):
        """Convert canvas drawing to PIL Image"""
        # Get canvas postscript
        ps = self.canvas.postscript(colormode='color')
        
        # Alternative: Create PIL image directly from canvas coordinates
        img = Image.new('RGB', (self.canvas_size, self.canvas_size), color='black')
        
        # Draw on the PIL image by replicating canvas drawing
        draw = ImageDraw.Draw(img)
        
        # Get all canvas items and redraw them on PIL image
        for item_id in self.canvas.find_all():
            coords = self.canvas.coords(item_id)
            if len(coords) >= 4:
                draw.line(coords, fill='white', width=self.brush_width)
        
        return img
    
    def submit_drawing(self):
        """Submit the drawing and pass it to callback"""
        self.drawn_image = self.get_canvas_image()
        self.status.config(text="Drawing submitted!")
        
        if self.on_submit:
            # Pass the PIL Image to the callback function
            self.on_submit(self.drawn_image)
        
        self.clear_canvas()
    
    def get_image(self):
        """Return the last drawn image"""
        return self.drawn_image


# Example usage
if __name__ == "__main__":
    def handle_submission(image):
        """This function receives the drawn image"""
        # Save example: image.save("drawn_digit.png")
        print("Image received! Size:", image.size)
        print("Image mode:", image.mode)
       
    
    root = tk.Tk()
    app = DrawingApp(root, on_submit=handle_submission)
    root.mainloop()
