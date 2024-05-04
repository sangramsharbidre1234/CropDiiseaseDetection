# pip install tensorflow

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
tf.enable_eager_execution()

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

image_size = (224, 224)
__classNames = [ "Bacterial Blight", "Healthy", "Red Rot" ]


# Load the saved model
saved_model = load_model("model_folder\sugarcane_disease_model.h5")

# Load an example image for inference

# Bacterial Blight
Bacterial_Blight_img_path = ['test_img_folder\Bacterial Blight\S_BLB (10).JPG', 'test_img_folder\Bacterial Blight\S_BLB (12).JPG', 'test_img_folder\Bacterial Blight\S_BLB (17).JPG', 'test_img_folder\Bacterial Blight\S_BLB (20).JPG']

# Healthy
Healthy_img_path = ['test_img_folder\Healthy\S_H (12).jpg', 'test_img_folder\Healthy\S_H (14).jpg', 'test_img_folder\Healthy\S_H (19).jpg', 'test_img_folder\Healthy\S_H (100).JPG']    

# Red Rot
Red_Rot_img_path = ['test_img_folder\Red Rot\S_RR (12).JPG', 'test_img_folder\Red Rot\S_RR (16).JPG', 'test_img_folder\Red Rot\S_RR (21).JPG', 'test_img_folder\Red Rot\S_RR (100).JPG']


# select img_path

# img_path = Bacterial_Blight_img_path[0]
# img_path = Healthy_img_path[0]
img_path = Red_Rot_img_path[0]


img = image.load_img(img_path, target_size=image_size)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Make predictions
predictions = saved_model.predict(img_array)

# Get the predicted class
predicted_class = np.argmax(predictions)
print("predicted_class : ", predicted_class)
print(f"Predicted Class: {__classNames[predicted_class]}")
