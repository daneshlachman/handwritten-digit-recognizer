import tkinter as Tkinter
from tkinter import messagebox, Label
from PIL import Image, ImageDraw, ImageTk
import numpy as np

from model import Model


class Application:
    def __init__(self):
        # create root window
        self.root = Tkinter.Tk()
        self.root.resizable(False, False)
        self.root.title('Handwritten digit recognizer')

        # variable definitions
        self.first_image = True
        self.image = None
        self.image_draw = None
        self.application_width_and_height = 400
        self.drawing_line_thickness = 17

        self.model = Model()

        # call define and train model function to get the model ready
        self.model.define_and_train_model()

        # create canvas to display future image on
        self.canvas = Tkinter.Canvas(width=self.application_width_and_height,
                                     height=self.application_width_and_height)
        self.canvas.pack()
        self.create_black_image()

        # use tag_bind to trigger pain_img to draw ellipse using the mouse
        self.canvas.tag_bind(self.canvas._image_id, "<B1-Motion>", lambda e: self.paint_image(e))

        # definition of buttons and their triggered functions
        clear_button = Tkinter.Button(self.root, text="Clear image", command=self.create_black_image)
        clear_button.pack()
        predict_button = Tkinter.Button(self.root, text="Predict", command=self.predict)
        predict_button.pack()

        # define labels for displaying predicted digit and its accuracy
        self.prediction_label = Label(text=("Predicted digit is ")
                                      )
        self.prediction_label.place(x=250, y=400)
        self.accuracy_label = Label(text=("Accuracy is: ")
                                    )
        self.accuracy_label.place(x=250, y=420)
        self.root.mainloop()

    def create_black_image(self):
        # if a black image was already created before, use the current image and make all the pixels black
        if not self.first_image:
            pixels = self.image.load()
            for i in range(self.image.size[0]):
                for j in range(self.image.size[1]):
                    pixels[i, j] = 0
            self.canvas._image_tk = ImageTk.PhotoImage(self.image)
            self.canvas.itemconfigure(self.canvas._image_id, image=self.canvas._image_tk)
        else:
            # create black image within the earlier defined canvas
            self.image = Image.new('L', (self.application_width_and_height,
                                         self.application_width_and_height), color="Black")
            self.image_draw = ImageDraw.Draw(self.image)
            self.canvas._image_tk = ImageTk.PhotoImage(self.image)
            self.canvas._image_id = self.canvas.create_image(0, 0, image=self.canvas._image_tk, anchor='nw')
            self.first_image = False

    def paint_image(self, event):
        # draw ellipses with the movement of the mouse while its left button is clicked
        x, y = event.x, event.y
        self.image_draw.ellipse((x - self.drawing_line_thickness, y - self.drawing_line_thickness,
                                 x + self.drawing_line_thickness, y + self.drawing_line_thickness), fill='white')
        self.canvas._image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvas._image_id, image=self.canvas._image_tk)

    def predict(self):
        # resize the drawn image and then make a prediction, and display the result
        resized_image = self.image.resize((28, 28))
        numpy_conversed_image = np.array(resized_image)
        prediction, prediction_percentage = self.model.make_prediction(numpy_conversed_image)
        self.prediction_label.configure(text="Predicted digit is: " + str(prediction))
        self.accuracy_label.configure(text="Accuracy is: " + str(round(prediction_percentage, 2)))
