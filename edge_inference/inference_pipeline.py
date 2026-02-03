# inference_pipeline.py
import cv2
import numpy as np

def preprocess(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img

def dummy_inference(img):
    # Placeholder for CNN inference
    disease_score = np.mean(img)
    if disease_score > 0.55:
        return "Disease Detected"
    else:
        return "Healthy Crop"

if __name__ == "__main__":
    image = preprocess("leaf.jpg")
    result = dummy_inference(image)
    print("Inference Result:", result)
