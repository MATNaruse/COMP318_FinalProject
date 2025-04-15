# COMP318_FinalProject
Group 5 - Python Voice LED Gadget on Raspberry Pi

## Basic Overview
### A) Using Tensorflow
We were originally going to create a Tensorflow Android App, a Voice Controlled To Do List, but due to lack of Android 
knowledge base and time, we pivoted to making it work on a Raspberry Pi.  
We created a basic Voice Detection model and trained it using sound clips found in a Tensorflow Example.
### B) Using Raspberry Pi
Instead of working with our original intent, we started to look into alternative used for the model with the minimal scope
it had, only  understanding 8 words. We were going to implement an "Eye Test" of a kind, but due to issues with time and
knowledge base, we pivoted again to displaying the detected words with LEDs connected to a breadboard and GPIO pins.

## Code Explanation/Purposes
### External Sources
`simple_audio_create_model.py` is a truncated version of the Tensorflow Simple Audio Example,
found here: https://www.tensorflow.org/tutorials/audio/simple_audio
It basically only generates a model based on the provided data, and does not render or create any visual graphs.

`realtime_voice_command_recognition.py` is a combined version of various classes and files from the AssemblyAI Community
tutorial found here: https://github.com/AssemblyAI-Community/realtime-voice-command-recognition
It handles taking input from the user and processes it into something we can work with on a coding level

`realtime_voice_command_recognition_testing.py` is also from the AssemblyAI Community tutorial, providing an example of 
applying the detected user input into something we can work with. We have modified it to make an LED turn on instead of
drawing with a turtle.

### Internal Sources
`GPIOHarness.py` is used to connect the vocal user input and output the associated blinking LED