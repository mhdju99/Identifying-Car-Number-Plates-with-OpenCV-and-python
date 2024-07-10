import easyocr
import cv2
from numpy import asarray
import cv2
from helper import *
import easyocr
from image_process import *


def crop_object(results, img):
    list_of_object = []
    boxes = results[0].boxes.xyxy.tolist()
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box
        #القص
        cropped_image = img[int(y1) : int(y2), int(x1) : int(x2)]

        gry = processImage(cropped_image)


        list_of_object.append((gry, box))

    return list_of_object


def write_to_file(path, text):
    with open(path, "a") as file:
        file.write(text)


def drow_label(box, imge, text):
    image = imge
    x1, y1, x2, y2 = box
    start_point = (int(x1), int(y2))
    start_point_text = (int(x1), int(y1))
    end_point = (int(x2), int(y1))
    new_end_point = (int(x2), int((y1 - 25)))
    color = (255, 0, 0)
    text_color = (255, 255, 1)
    thickness = 2
    fontFace = cv2.FONT_HERSHEY_DUPLEX
    fontScale = 1
    thickness = 2
    image = cv2.rectangle(image, start_point, end_point, color, thickness)
    image = cv2.rectangle(image, start_point_text, new_end_point, color, -1)
    image = cv2.putText(
        image,
        text,
        start_point_text,
        fontFace,
        fontScale,
        text_color,
        thickness,
        lineType=cv2.LINE_AA,
    )
    return image


def extactText(croped, reader):
    result = reader.readtext(croped)
    text1 = ""
    for bbox, text, prob in result:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        text1 = text1 + " " + text
        print(f"++++++++++++Text: {text}+++++++++++++++, ")

    return text
