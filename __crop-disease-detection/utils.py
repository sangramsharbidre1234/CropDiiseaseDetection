# pip install tensorflow
# python -m pip install --no-cache-dir tensorflow

# pip install Flask


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
tf.enable_eager_execution()

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


image_size = (224, 224)

# /cropmodel/?modelname=tomatomodel
# /cropmodel/?modelname=sugarcanemodel
# /cropmodel/?modelname=cottonmodel
Model_related_data = {
    "tomatomodel" : {
        "dataset" : {
            "total_images" : 14678,
            "total_classes" : 10,
            "classes_names" : [ 
                                "Late_blight",
                                "healthy",
                                "Early_blight",
                                "Septoria_leaf_spot",
                                "Tomato_Yellow_Leaf_Curl_Virus",
                                "Bacterial_spot",
                                "Target_Spot",
                                "Tomato_mosaic_virus",
                                "Leaf_Mold",
                                "Spider_mites Two-spotted_spider_mite",
                            ],
            },

        "training" : {
            "epochs" : 7,
            "batch_size" : 32,
            "img_frame_size" : (224,224),
            "CNN_layers" : 5,
            "CNN_layer_name" : 'relu',   
            "accuracy" : "89.23%",
            },
        "reference" : "https://www.kaggle.com/code/mrappplg/tomato-disease-detection"
        },

    "sugarcanemodel" : {
        "dataset" : {
            "total_images" : 240,
            "total_classes" : 3,
            "classes_names" : [ "Bacterial Blight", "Healthy", "Red Rot" ],
            },

        "training" : {
            "epochs" : 10,
            "batch_size" : 32,
            "img_frame_size" : (224,224),
            "CNN_layers" : 5,
            "CNN_layer_name" : 'relu', 
            "accuracy" : "94.56%",
            },
        "reference" : "https://www.kaggle.com/code/handmadeprojects/sugarcane-disease-detection"
        },
    
    "cottonmodel" : {
        "dataset" : {
            "total_images" : 1951,
            "total_classes" : 4,
            "classes_names" : ["Diseased Cotton Leaf", "Diseased Cotton Plant", "Fresh Cotton Leaf", "Fresh Cotton Plant"],
            },

        "training" : {
            "epochs" : 10,
            "batch_size" : 32,
            "img_frame_size" : (224,224),
            "CNN_layers" : 4,
            "CNN_layer_name" : 'relu', 
            "accuracy" : "83.13%",
            },
        "reference" : "https://www.kaggle.com/code/handmadeprojects/cotton-disease-detection"
        },

    }

def get_model_details():
    return Model_related_data


def tomatomodel(img_path):
    __classNames = [ 
        "Bacterial_spot",
        "Early_blight",
        "Late_blight",
        "Leaf_Mold",
        "Septoria_leaf_spot",
        "Spider_mites Two-spotted_spider_mite",
        "Target_Spot",
        "Tomato_Yellow_Leaf_Curl_Virus",
        "Tomato_mosaic_virus",
        "Healthy",
     ]

    # Load the saved model
    saved_model = load_model('model_folder/tomato_disease_model.h5')

    # Example inference with a test image
    # img_path = 'uysdeh'
    
    img = image.load_img(img_path, target_size=image_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    result = saved_model.predict(img_array)

    # Get the predicted class
    classIndex = np.argmax(result)
    predicted_class = __classNames[classIndex]
    print(f"tomatomodel __ Predicted class - {classIndex} : {predicted_class}")

    # Free memory by deleting variables
    del __classNames
    del saved_model
    del img
    del img_array
    del result

    return predicted_class

    

def sugarcanemodel(img_path):
    __classNames = [ "Bacterial Blight", "Healthy", "Red Rot" ]

    # Load the saved model
    saved_model = load_model("model_folder/sugarcane_disease_model.h5")

    # img_path = "test_img_folder/Red Rot/S_RR (12).JPG"

    img = image.load_img(img_path, target_size=image_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    result = saved_model.predict(img_array)

    # Get the predicted class
    classIndex = np.argmax(result)
    predicted_class = __classNames[classIndex]
    print(f"sugarcanemodel __ Predicted class - {classIndex} : {predicted_class}")

    # Free memory by deleting variables
    del __classNames
    del saved_model
    del img
    del img_array
    del result


    return predicted_class



def cottonmodel(img_path):
    # __classNames = ["Diseased Cotton Leaf", "Diseased Cotton Plant", "Fresh Cotton Leaf", "Fresh Cotton Plant"]
    __classNames = ['fresh cotton plant', 'diseased cotton plant', 'fresh cotton leaf', 'diseased cotton leaf']

    # Load the saved model
    saved_model = load_model('model_folder/cotton_disease_model.h5')

    # img_path = '/kaggle/input/cotton-disease-dataset/Cotton Disease/train/fresh cotton plant/dsd (138)_iaip.jpg'

    img = image.load_img(img_path, target_size=image_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    result = saved_model.predict(img_array)

    # Get the predicted class
    classIndex = np.argmax(result)
    predicted_class = __classNames[classIndex]
    print(f"cottonmodel __ Predicted class - {classIndex} : {predicted_class}")

    # Free memory by deleting variables
    del __classNames
    del saved_model
    del img
    del img_array
    del result


    return predicted_class
