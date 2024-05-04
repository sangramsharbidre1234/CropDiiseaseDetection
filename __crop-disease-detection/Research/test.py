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
            }
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
            }
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
            }
        },

    }

print(Model_related_data['tomatomodel'])
print(Model_related_data['tomatomodel']['dataset']['classes_names'])
print(Model_related_data['tomatomodel']['training'])