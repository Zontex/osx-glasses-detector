# osx-glasses-detector

Detect if you wear glasses during OSX system startup / wake up from sleep and notify you to wear it if you don't.

## Overview

I experience debilitating headaches when I neglect to wear my reading glasses while using my laptop. Unfortunately, I often forget or simply don't feel like putting them on. To overcome this challenge, I've created a Python script that serves as a reminder each time I start up my laptop.

The script, which has been pieced together from various sources, uses the openCV object detection model to detect if I'm wearing my glasses. If I'm not, the script will issue a notification, reminding me to put them on for a more comfortable and headache-free experience.

## Expected results

When your laptop wake up or powered on, the script will automatically execute, take a screenshot from your camera and figure out if you wear glasses or not.

## Requirements

1. Get ~~[Sleep Watcher 2.2.1 or above](https://www.bernhard-baehr.de/) which supports Mac OS X >= 10.5.~~ This doesn't seem to work, instead, get [hammerspoon](https://github.com/Hammerspoon/hammerspoon/) and load the lua script inside the repo. Don't forget to change the username accordingly.
2. Download the detection model from [italojs facial-landmarks-recognition repository](https://github.com/italojs/facial-landmarks-recognition)
3. Install the following libraries: pygame,numpy,dlib,cv2,matplot,pillow,statistics. to install dlib you'll need to install cmake first.
4. Itegrate TTS service or get a free sample file, I used [TTSMp3](https://ttsmp3.com/) to download the TTS mp3 file.
5. Make sure to chmod +x script.sh to ensure it's executed.
6. Permit OSX permissions when asked through security center.

## Deamon installation

~~Inside sleep watcher readme file there are detailed instructions on executing the deamon.~~

## Credits

* [siddh30](https://github.com/siddh30/Glasses-Detection/blob/main/Glasses_detection.ipynb) for the glasses detection code
* [italojs](https://github.com/italojs/) for the object detection model

## License

Previous repositories don't have license so I put this one as MIT.
