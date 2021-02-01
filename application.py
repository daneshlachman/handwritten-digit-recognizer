import tkinter as Tkinter
from PIL import Image, ImageDraw, ImageTk
import pdb
import numpy as np
import matplotlib.pyplot as plt


class Application():
    def __init__(self):
        # create root window
        self.root = Tkinter.Tk()
        self.first_image = True
        self.image = None
        self.image_draw = None

        # create canvas to display future image on
        self.canvas = Tkinter.Canvas(width=512, height=512)
        self.canvas.pack()

        # call function to create black image on the canvas
        self.create_new_black_image()

        # use tag_bind to trigger pain_img to draw ellipse using the mouse
        self.canvas.tag_bind(self.canvas._image_id, "<B1-Motion>", lambda e: self.paint_img(e))

        # definition of buttons and their triggered functions
        clear_button = Tkinter.Button(self.root, text="Clear image", command=self.create_new_black_image)
        predict_button = Tkinter.Button(self.root, text="Predict", command=self.predict)
        clear_button.pack()
        predict_button.pack()

        self.root.mainloop()

    def create_new_black_image(self):
        if not self.first_image:
            pixels = self.image.load()
            for i in range(self.image.size[0]):
                for j in range(self.image.size[1]):
                    pixels[i, j] = 0
        else:
            # create black image within the earlier defined canvas
            self.image = Image.new('L', (512, 512), color="Black")
            self.image_draw = ImageDraw.Draw(self.image)
            self.canvas._image_tk = ImageTk.PhotoImage(self.image)
            self.canvas._image_id = self.canvas.create_image(0, 0, image=self.canvas._image_tk, anchor='nw')
            self.first_image = False

    def paint_img(self, event):
        x, y = event.x, event.y
        self.image_draw.ellipse((x-10, y-10, x+10, y+10), fill='white')
        self.canvas._image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvas._image_id, image=self.canvas._image_tk)

    def predict(self):
        resized_image = self.image.resize((28, 28))
        # resized_image.show()
        numpy_array = np.array(resized_image)
        plt.figure()
        plt.imshow(numpy_array)
        plt.colorbar()
        plt.grid(False)
        plt.show()


Application()

