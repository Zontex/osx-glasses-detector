# osx-glasses-detector

Detect if you wear glasses during OSX system startup and notify you to wear it if you don't.

## Overview

I'm suffering from extreme headaches when I don't put on my reading glasses when I use my laptop, often I either forget or I can't bother putting them on. I've decided to make a script that notifies me of each laptop startup to put on my glasses if I don't put them already.

The script is combined from multiple sources into a single code for convenient use, using the openCV object detection model.

## Expected results

When your laptop wake up or powered on, the script will automatically execute, take a screenshot from your camera and figure out if you wear glasses or not.

## Requirements

1. You'll need To get ~~[Sleep Watcher 2.2.1 or above](https://www.bernhard-baehr.de/) which supports Mac OS X >= 10.5.~~ This doesn't seem to work, instead, get [hammerspoon](https://github.com/Hammerspoon/hammerspoon/) and load the lua script inside the repo. Don't forget to change the username accordingly.
2. You'll need to download the detection model from [italojs facial-landmarks-recognition repository](https://github.com/italojs/facial-landmarks-recognition)
3. You'll need to install the following libraries: pygame,numpy,dlib,cv2,matplot,pillow,statistics. to install dlib you'll need to install cmake first.
4. You'll need to either integrate TTS service or get a free sample file, I used [TTSMp3](https://ttsmp3.com/) to download the TTS mp3 file.
5. Make sure to chmod +x script.sh to ensure it's executed.
6. Permit OSX permissions when asked through security center.

## Deamon installation

Inside sleep watcher readme file there are detailed instructions on executing the deamon.

## Credits

* [siddh30](https://github.com/siddh30/Glasses-Detection/blob/main/Glasses_detection.ipynb) for the glasses detection code
* [italojs](https://github.com/italojs/) for the object detection model

## License

Previous repositories don't have license so I put this one as MIT.