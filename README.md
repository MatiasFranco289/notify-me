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

## How to run the application

Being in the main path (The same path where the main.py file is) and with all dependencies and packages installed run the following command:

    python main.py

## App configurations

The first time you open the application you will have to configurate the application. You can set the differents parameters using the option menu.

- `Start`: Starts the application with the current configuration.
- `View current settings`: View the current setting of the application.
- `Set pixel coordinates`: Set the position of the pixel that will be observed.
- `Set tolerancy`: Tolerancy is the maximum difference between the alert color and the pixel color between 0 and 900.
- `Set alert color`:  Is the color that the pixel must have to trigger the notification.
- `Set sound path`: Path of the sound file that will be triggered. Must be in a .wav format.
