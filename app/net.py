from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


class Prediction:

    # using model v7-alt
    model = load_model("app/nn-final.h5")
    d = {0: 'Kawka', 1: 'Sroka', 2: 'Gawron', 3: 'Sójka', 4: 'Wrona', 5: 'Kruk'}

    def __init__(self, file):
        self.shape = self.model.input_shape[::-1][1:3]
        self.img = Image.open(file)
        self.img = self.img.resize(self.shape)
        self.img = np.array(self.img) / 255

    def predict(self):
        prediction = self.model.predict(np.expand_dims(self.img, axis=0))
        return prediction.argmax()
