## Required packages
You must run the following commands in the terminal in order to install required packages for the app to run correctly. If you try to install some dependencies before this step you will be getting errors.

    sudo apt-get install python3-tk python3-dev

    sudo apt-get install libasound2-dev

## Installing dependencies

Being in the same path where the main.py file is use the following command:

    pip install -r requirements.txt

## Disable screenshot sound

To screenshot sound can be very annoying if it is triggered every second. In order to disable it yo need to rename or move the file in the following path:

    /usr/share/sounds/freedesktop/stereo/camera-shutter.oga

