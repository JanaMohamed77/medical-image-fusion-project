import cv2
import numpy as np

def load_and_preprocess(path, size=(256, 256)):
    """
    Reads an MRI image, converts to grayscale, resizes, 
    and normalizes pixel values.
    """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image not found at {path}")
    
    img_resized = cv2.resize(img, size)
    img_normalized = img_resized / 255.0  # Normalize to [0,1]
    return img_normalized
