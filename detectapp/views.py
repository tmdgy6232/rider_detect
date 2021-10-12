from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
import cv2
import numpy as np
import time
import csv
from image_model.predict import predict


# Create your views here.

def helloworld(request):
    return render(request, 'detectapp/helloworld.html')

def ready(request):
    return render(request, 'detectapp/ready.html')

def detail(request):
    return render(request, 'detectapp/detail.html')

@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("Error")
        pass

class VideoCamera(object):
    delay = 0
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        threading.Thread(target=self.predict, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        self.delay += 1
        # print(predict(image))
        if self.delay / 1000 == 0:
            self.delay = 0
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

    def predict(self):
        while True:

            result = predict(self.frame)
            result_max = np.argmax(result)

            now = time.localtime()

            if result_max == 0:
                ans = 'backgroud'
                time.sleep(1)
                f = open('example_db.csv', 'a', newline='')
                wr = csv.writer(f)
                wr.writerow(["%04d/%02d/%02d %02d:%02d:%02d" % (
                now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), ans])
                f.close()
            elif result_max == 1:
                ans = 'headgear'
                time.sleep(1)
                f = open('example_db.csv', 'a', newline='')
                wr = csv.writer(f)
                wr.writerow(["%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), ans])
                f.close()
            elif result_max == 2:
                ans = 'no headgear'
                time.sleep(1)
                f = open('example_db.csv', 'a', newline='')
                wr = csv.writer(f)
                wr.writerow(["%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), ans])
                f.close()
            elif result_max == 3:
                ans = 'overcrowding'
                time.sleep(1)
                f = open('example_db.csv', 'a', newline='')
                wr = csv.writer(f)
                wr.writerow(["%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), ans])
                f.close()

def gen(camera):
    while True:
        frame = camera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')