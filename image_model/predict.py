from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from .main import preprocessing

# # Load the model
# model = load_model('keras_model.h5')
#
# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1.
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# # Replace this with the path to your image
# image = Image.open('test.png')
# #resize the image to a 224x224 with the same strategy as in TM2:
# #resizing the image to be at least 224x224 and then cropping from the center
# size = (224, 224)
# image = ImageOps.fit(image, size, Image.ANTIALIAS)
#
# #turn the image into a numpy array
# image_array = np.asarray(image)
# # Normalize the image
# normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# # Load the image into the array
# data[0] = normalized_image_array
#
# # run the inference
# prediction = model.predict(data)
# print(np.round(prediction))
# 1. 배경 2. 헬멧 쓴거 3. 헬멧 안쓴거 4. 두명태운거

def predict(image):
    # Load the model
    model = load_model('image_model/keras_model.h5')

    # 이미지 전처리
    nomalize_image = preprocessing(image)

    return model.predict(nomalize_image)
