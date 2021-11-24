import os, shutil
from keras import models
import numpy as np
import cv2

from settings.project_path import *

# preprocess images
def get_inputs(images=[]):
    pre_x = []

    for img in images:
        x = cv2.imread(img)
        x = cv2.resize(x, (150, 150))
        x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        pre_x.append(x) 
    pre_x = np.array(pre_x) / 255.0
    
    return pre_x

# copy images
if os.path.isdir(PREDICTED_DIR):
    shutil.rmtree(PREDICTED_DIR)
    os.mkdir(PREDICTED_DIR)
    os.mkdir(CATS_DIR)
    os.mkdir(DOGS_DIR)
else:
    os.mkdir(PREDICTED_DIR)
    os.mkdir(CATS_DIR)
    os.mkdir(DOGS_DIR)

# show image name    
print('-' * 70, '\n\n', os.listdir(PREDICT_DIR), '\n\n', '-' * 70)

# put image_path into list
images = [os.path.join(PREDICT_DIR, img) 
    for img in os.listdir(PREDICT_DIR)]

# get preprocessed image tensor
pre_x = get_inputs(images)


# load trained convnet
model = models.load_model(MODEL_PATH)
# use convnet to predict
pre_y = model.predict_classes(pre_x)

# categorical saparate images into different folders
print('-' * 60 + '\n')
for i in range(len(pre_y)):
    print('Image=%s, Predicted=%s' % (os.listdir(PREDICT_DIR)[i], ['cat', 'dog'][pre_y[i][0]]))

    if pre_y[i][0] == 0:
        dst = os.path.join(CATS_DIR, os.listdir(PREDICT_DIR)[i])
        shutil.copyfile(images[i], dst)
    else:
        dst = os.path.join(DOGS_DIR, os.listdir(PREDICT_DIR)[i])
        shutil.copyfile(images[i], dst)
print('\n' + '-' * 60)