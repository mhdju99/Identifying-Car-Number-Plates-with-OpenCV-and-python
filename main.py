from image_process import *
from object_dedact import *
from helper import *
import datetime
import cv2


from ultralytics import YOLO


def main():
    model = YOLO("license_plate_detector.pt")
    reader = easyocr.Reader(["en"])
    while True:
        print("ready")
        image_path = choose_file()
        orignal = cv2.imread(image_path)
        results = prdict(model, image_path)
        crops: list = crop_object(results, orignal)

        for crop in crops:
            #استخراج النص
            text = extactText(crop[0], reader)
            #كتابة في ملف
            write_to_file(
                "aa.text",
                f"\n plate number is :{text}   .... catch in : {datetime.datetime.now()}\n",
            )
            
            image = drow_label(crop[1], orignal, text)

        cv2.imshow("Image", crop[0])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        res = resize_img(image, 0.3)
        cv2.imshow("Image", res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
