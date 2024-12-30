# hemorrhage_detection.py

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Function to load the trained model
def load_trained_model(model_path):
    model = load_model(model_path)
    return model

# Function to preprocess the image
def preprocess_image(image_path, target_size=(256, 256)):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(grayscale_image, target_size)
    resized_image = resized_image.astype('float32') / 255.0
    resized_image = resized_image[..., None]  # Add channel axis
    return np.expand_dims(resized_image, axis=0)



def predict_hemorrhage(model, image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    if predictions[0][0] > predictions[0][1]:
        return"Hemorrhage Detected"
    else:
        return"No Hemorrhage Detected"

