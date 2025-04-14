"""
    Simple Audio Recognition Example from TensorFlow
        https://www.tensorflow.org/tutorials/audio/simple_audio
    Using Specific Snippets for our use case
"""

# TODO: Will Implement Graphs later for demo/presentation purposes (?)
# MN - I just wanted them out of the way for now while I troubleshooted the model creation

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import models
from IPython import display

from lib.external_resources.simple_audio_create_model import test_spectrogram_ds, train_ds

model = models.load_model("simple_audio.h5")

y_pred = model.predict(test_spectrogram_ds)
y_pred = tf.argmax(y_pred, axis=1)
y_true = tf.concat(list(test_spectrogram_ds.map(lambda s,lab: lab)), axis=0)

label_names = np.array(train_ds.class_names)

confusion_mtx = tf.math.confusion_matrix(y_true, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_mtx,
            xticklabels=label_names,
            yticklabels=label_names,
            annot=True, fmt='g')
plt.xlabel('Prediction')
plt.ylabel('Label')
plt.show()