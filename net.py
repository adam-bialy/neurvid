from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class Prediction:

    # using model v7-alt
    model = load_model("nn-final.h5")
    d = {0: 'Kawka', 1: 'Sroka', 2: 'Gawron', 3: 'Sójka', 4: 'Wrona', 5: 'Kruk'}

    def __init__(self, path):
        self.shape = self.model.input_shape[1:]
        self.img = image.load_img(path, target_size=self.shape)
        self.img = image.img_to_array(self.img) / 255

    def predict(self):
        prediction = self.model.predict(np.expand_dims(self.img, axis=0))
        return prediction.argmax()
