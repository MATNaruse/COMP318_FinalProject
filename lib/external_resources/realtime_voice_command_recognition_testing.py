import numpy as np
import importlib
from keras import models

# from lib.classes.GPIOHarness import blink_led
from realtime_voice_command_recognition import record_audio, terminate, preprocess_audiobuffer

# from lib.static_data import static_data

# !! Modify this in the correct order
# commands = static_data.vr_cmds
commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']

loaded_model = models.load_model("simple_audio.h5")

test_answers = ['up', 'down', 'left', 'right', 'yes', 'no']

test_input = []

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    test_input.append(command)
    return command

if __name__ == "__main__":
    x = 0
    correct = 0
    for x in range(0, 6):
        command = predict_mic()
        # blink_led(command)
    for result in zip(test_input, test_answers):
        if result[0] == result[1]:
            correct = correct + 1
        print(f"[{'O' if result[0] == result[1] else 'X'}] {result[0]} - {result[1]}")
    print(f"You got {correct} out of {len(test_answers)} correct!")
