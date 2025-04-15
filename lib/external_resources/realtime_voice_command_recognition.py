"""
    Realtime Voice Command Recognition
        https://www.youtube.com/watch?v=m-JzldXm9bQ
        https://github.com/AssemblyAI-Community/realtime-voice-command-recognition
    Using Specific Snippets for our Use Case
"""
import pyaudio, importlib
import numpy as np
import tensorflow as tf
from keras import models


# PyAudio Variables
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1 # Mono Channel, same as Training Data
RATE = 16000 # Matches Training Data Length
p = pyaudio.PyAudio()

# TF Variables
seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)
loaded_model = models.load_model("simple_audio.h5")

vr_cmds = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']
"""
    PyAudio Helper Snippets
"""
def record_audio():
    # Setting PyAudio stream settings
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER,
        input_device_index=1
    )
    # MN - Change input_device_index to 0 or remove line, this is set for my mic input

    print("start recording...")

    frames = []
    seconds = 1
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()

    return np.frombuffer(b''.join(frames), dtype=np.int16)

def predict_mic(ld_mod = loaded_model):
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = ld_mod(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = vr_cmds[label_pred[0]]
    print("Predicted label:", command)
    return command


def terminate():
    p.terminate()

"""
    TF Helper Snippets
"""
def get_spectrogram(waveform):
    # Zero-padding for an audio waveform with less than 16,000 samples.
    # (As covered in Module 2: Numpy and Matplot lib)
    input_len = 16000
    waveform = waveform[:input_len]
    zero_padding = tf.zeros(
        [16000] - tf.shape(waveform),
        dtype=tf.float32)
    # Cast the waveform tensors' dtype to float32.
    waveform = tf.cast(waveform, dtype=tf.float32)
    # Concatenate the waveform with `zero_padding`, which ensures all audio
    # clips are of the same length.
    equal_length = tf.concat([waveform, zero_padding], 0)
    # Convert the waveform to a spectrogram via a STFT.
    spectrogram = tf.signal.stft(
        equal_length, frame_length=255, frame_step=128)
    # Obtain the magnitude of the STFT.
    spectrogram = tf.abs(spectrogram)
    # Add a `channels` dimension, so that the spectrogram can be used
    # as image-like input data with convolution layers (which expect
    # shape (`batch_size`, `height`, `width`, `channels`).
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram


def preprocess_audiobuffer(waveform):
    """
    waveform: ndarray of size (16000, )

    output: Spectogram Tensor of size: (1, `height`, `width`, `channels`)
    """
    #  normalize from [-32768, 32767] to [-1, 1]
    waveform = waveform / 32768

    waveform = tf.convert_to_tensor(waveform, dtype=tf.float32)

    spectogram = get_spectrogram(waveform)

    # add one dimension
    spectogram = tf.expand_dims(spectogram, 0)

    return spectogram