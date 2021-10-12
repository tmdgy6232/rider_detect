import numpy as np
import os

np.random.seed(3)

from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

data_datagen = ImageDataGenerator(rescale=1. / 255,
                                  rotation_range=30,
                                  shear_range=5.5,
                                  width_shift_range=0.1,
                                  height_shift_range=0.1,
                                  zoom_range=0.,
                                  horizontal_flip=False,
                                  vertical_flip=True,
                                  fill_mode='nearest')

filename_in_dir = []

for root, dirs, files in os.walk('./dataset/two_person'):
    for fname in files:
        full_fname = os.path.join(root, fname)
        filename_in_dir.append(full_fname)

for file_image in filename_in_dir:
    print(file_image)
    img = load_img(file_image)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0

    for batch in data_datagen.flow(x, save_to_dir='./dataset/two_person_gen', save_prefix='no_headgear', save_format='png'):
        i += 1
        if i > 20:
            break