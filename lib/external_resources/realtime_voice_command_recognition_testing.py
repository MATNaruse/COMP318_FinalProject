"""
    COMP318-002 Group 5
    Realtime Voice Command Recognition
        https://www.youtube.com/watch?v=m-JzldXm9bQ
        https://github.com/AssemblyAI-Community/realtime-voice-command-recognition
    Using Specific Snippets for our Use Case
"""
import numpy as np
from keras import models

from GPIOHarness import blink_led
from realtime_voice_command_recognition import record_audio, terminate, preprocess_audiobuffer

# !! Modify this in the correct order
commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']

loaded_model = models.load_model("simple_audio.h5")

## This is left over from our pivot from an Eye Test
# test_answers = ['up', 'down', 'left', 'right', 'yes', 'no']
# test_input = []

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    # test_input.append(command)
    return command

if __name__ == "__main__":
    while True:
        command = predict_mic()
        blink_led(command)
        if command == "stop":
            terminate()
            break

    ## This is left over from our pivot from an Eye Test
    # x = 0
    # correct = 0
    # for x in range(0, 6):
        # command = predict_mic()
        # blink_led(command)
    # for result in zip(test_input, test_answers):
        # if result[0] == result[1]:
            # correct = correct + 1
        # print(f"[{'O' if result[0] == result[1] else 'X'}] {result[0]} - {result[1]}")
    # print(f"You got {correct} out of {len(test_answers)} correct!")
