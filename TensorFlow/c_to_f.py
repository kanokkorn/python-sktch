import tensorflow as tf
import numpy as np 
from matplotlib import pyplot as plt

cel = np.array([0, 1, 2, 3, 4, 5, 6], dtype = float)
fah = np.array([1, 3, 5, 7, 9, 11, 13], dtype = float)

for i, c in enumerate(cel):
    print("{} degree Celsius = {} degrees Fahenheit".format(c, fah[i]))

L0 = tf.keras.layers.Dense( units = 1, input_shape = [1] )
model = tf.keras.Sequential([L0])
model.compile( loss = 'mean_squared_error', optimizer = tf.keras.optimizers.Adam(0.1)) 
history = model.fit(cel, fah, epochs=3500, verbose=False)
print("Finish !")

import matplotlib.pyplot as plt

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(history.history['loss'])

print(model.predict([84501, 10000]))