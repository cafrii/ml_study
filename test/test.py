

import tensorflow
print(tensorflow)

try:
    import tensorflow.keras as keras
    print('importing tensorflow.keras..')
except Exception:
    import keras
    print('importing keras..')

import keras.models
print(keras.models)

print(keras)
print(keras.__version__)

