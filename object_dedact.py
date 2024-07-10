from ultralytics import YOLO
import cv2
from numpy import asarray
import cv2
import numpy as np
from matplotlib import pyplot as plt
from image_process import choose_file, resize_img
import easyocr


def prdict(model, img_recized):
    # pretrained YOLOv8n model
    results = model.predict(
        source=img_recized,
        conf=0.7,
        imgsz=640,
    )
    print(results[0].boxes.xyxy.tolist())
    return results
