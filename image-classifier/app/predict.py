from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the model once
model = MobileNetV2(weights="imagenet") #load the MobileNetV2 model pre-trained on ImageNet

def predict_image(img_path, top_k=5):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224)) #prepare the input image to be compatible with MobileNetV2.
    x = image.img_to_array(img) # TensorFlow models work with arrays, not image objects
    x = np.expand_dims(x, axis=0) #convert it into a batch of one image
    x = preprocess_input(x)  # ensure that the input matches what the model was trained on

    # Predict
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=top_k)[0] # translates the raw predictions into human-readable labels
# create a clean list of dictionaries for each of the top predicted classes.
    results = []
    for class_id, label, confidence in decoded:
        results.append({
            "class_id": class_id,
            "label": label,
            "confidence": round(float(confidence), 4)
        })

    best = results[0]
    if best["confidence"] < 0.5:
        best["warning"] = "Low confidence  prediction might be incorrect."

    return {
        "top_prediction": best,
        "top_k_predictions": results
    }

# Local test
if __name__ == "__main__":
    result = predict_image("test_images/banana.jpg")
    from pprint import pprint
    pprint(result)
