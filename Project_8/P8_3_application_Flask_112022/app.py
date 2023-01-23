from flask import Flask, request, redirect, url_for, send_from_directory, render_template, send_file

import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import stat
from skimage.color import rgb2gray

# tensorflow
import tensorflow as tf #2.4.0
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img

# segmentation_models
import segmentation_models as sm
sm.set_framework('tf.keras')
from segmentation_models import FPN

#NGROK
from flask_ngrok import run_with_ngrok

# define a Flask app
app = Flask(__name__)
run_with_ngrok(app)

#model = None
IMAGE_PATH_IN = 'static/input/'
IMAGE_PATH_OUT = 'static/output/'
MODEL_PATH = "model/Base-Dice.keras"

#model = sm.FPN('resnet152', classes=8, activation='softmax', encoder_weights='imagenet')
model = load_model(MODEL_PATH,
                    custom_objects={
                            'iou_score': sm.metrics.iou_score,
                            'f1-score': sm.metrics.f1_score,
                            'dice_loss': sm.losses.DiceLoss()})
model.load_weights(MODEL_PATH)

# function for preparing the input image before prediction
def prepare_image(image):
    image = image/255.0
    image = np.asarray(image).astype(np.float32)
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/', methods=['GET'])
def index():
    # main page
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if request.files.get("file"):
            image_filename = request.files["file"].filename
            files_list = os.listdir('static/input')
            for file in files_list:
                name = file.split('.')[0]
                if name.endswith('_gt'):
                    name = name.split('_')
                    name = name[:-1]
                    name = "_".join(name)
                    if name == image_filename.split('.')[0]:
                        true_mask = name + '_gt' + '.png'
                        true_mask = load_img((f'{IMAGE_PATH_IN}/{true_mask}'), color_mode="grayscale")
                        true_mask = np.asarray(true_mask)
                        plt.imsave(os.path.join(IMAGE_PATH_OUT, 'output_gt.jpg'), true_mask)

            # read the image in PIL format
            image = request.files["file"].read()
            image = Image.open(io.BytesIO(image))
            image = image.resize((256, 128), Image.ANTIALIAS)
            image = np.asarray(image)
            image = prepare_image(image)

            # model prediction
            predicted_mask = model.predict(image)
            predicted_mask = np.argmax(predicted_mask, axis=3)[0]


            plt.imsave(os.path.join(IMAGE_PATH_OUT, 'output_pred.jpg'), predicted_mask)

            return render_template('predict.html')

    return render_template('submit.html')

if __name__ == '__main__':
    app.run()
