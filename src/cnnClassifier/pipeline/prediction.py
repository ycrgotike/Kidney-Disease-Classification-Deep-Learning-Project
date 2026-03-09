import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:

    def __init__(self):
        self.model = load_model("artifacts/training/model.h5")

    def predict(self, filename):

        test_image = image.load_img(filename, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        result = self.model.predict(test_image)

        class_labels = ['Cyst','Normal','Stone','Tumor']

        prediction = class_labels[np.argmax(result)]

        return prediction