import numpy as np
import tensorflow as tf

model = tf.keras.application.MobileNetV2(
        weight='imagenet', input_shape=(224, 224, 3))
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

tflite_result = interpreter.get_tensor(output_details[0]['index'])
tf_results = model(tf.constant(input_data))

for tf_results, tflite_result in zip(tf_results, tflite_result):
  np.testing.assert_almost_equal(tflite_result, tflite_result, decimal=5)
