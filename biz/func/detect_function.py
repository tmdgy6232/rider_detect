from detectapp.models import Detect
import cv2
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'riderDetection.settings')
application = get_wsgi_application()
def save_image(img, classfication_type):
    new_detect = Detect()
    new_detect.image = img
    new_detect.classification_type = classfication_type
    new_detect.save()
    print('저장완료')
