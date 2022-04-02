from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


class Prediction:

    # using model v7-alt
    model = load_model("app/nn-final.h5")
    d = {0: 'Kawka', 1: 'Sroka', 2: 'Gawron', 3: 'Sójka', 4: 'Wrona', 5: 'Kruk'}

    def __init__(self, file):
        # find the shape expected by the model
        self.shape = self.model.input_shape[::-1][1:3]
        # open and resize the file
        self.img = Image.open(file)
        self.img = self.img.resize(self.shape)
        self.img = np.array(self.img) / 255
        # find the filetype
        filetype = file.filename.split(".")[-1].lower()
        if filetype == "png" and self.img.shape[-1] == 4:
            self.img = self.img[:,:,:-1]

    def predict(self):
        prediction = self.model.predict(np.expand_dims(self.img, axis=0))
        return prediction.argmax()

    def predict_top2(self):
        prediction = self.model.predict(np.expand_dims(self.img, axis=0))
        return prediction.argsort()[:,-2:].flatten()[::-1]
