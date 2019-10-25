import os
import tensorflow as tf

from tensorflow.contrib.lite.python import lite
from tensorflow.keras import Input, Model

from darknet import darknet_base
from definitions import ROOT_DIR

inputs = Input(shape=(None, None, 3))
outputs, config = darknet_base(inputs, include_yolo_head=False)

model = Model(inputs, outputs)
model_path = os.path.join(ROOT_DIR, 'model', 'yolov3.h5')

tf.keras.models.save_model(model, model_path, overwrite=True)

model = tf.keras.model.load_model(model_path,
        custom_objects={'tf': tf}
        )
converter = lite.TocoConverter.from_keras_model_file(model_path,
        input_shapes={'input_1': [1, config['width'], config['height'], 3]}
            )
converter.post_training_quantize = True
tflite_model = convert.convert()
open('model/yolov3.tflite', 'wb').write(tflite_model)
