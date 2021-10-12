from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading
import cv2
from image_model.predict import predict


# Create your views here.

def helloworld(request):
    return render(request, 'detectapp/helloworld.html')

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
            # 타임슬립을 하든, delay 1
            print(predict(self.frame))

def gen(camera):
    while True:
        frame = camera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')