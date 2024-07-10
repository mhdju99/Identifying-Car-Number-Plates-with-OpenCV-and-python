from tkinter import Tk, filedialog
import cv2

def choose_file():
    root = Tk()
    root.withdraw()  # يخفي النافذة الرئيسية
    file_path = filedialog.askopenfilename(title="اختر ملف")  # يعرض نافذة اختيار الملفات
    return file_path


def resize_img(image, value):
    down_width = image.shape[0] - (image.shape[0] * value)
    down_height = image.shape[1] - (image.shape[1] * value)
    down_points = ( int(down_height),int(down_width))
    resized_down = cv2.resize(image, down_points)
    return resized_down


def processImage(cropimage):
    license_plate_crop_gray = cv2.cvtColor(cropimage, cv2.COLOR_BGR2GRAY)
    return license_plate_crop_gray


