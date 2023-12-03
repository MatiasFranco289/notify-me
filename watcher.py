import pyautogui
import global_vars
import time
from utils import get_tuple_difference
import simpleaudio as sa
import wave

def get_pixel_color(x, y) -> tuple:
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    return pixel_color

def play_sound(file_path):
    wave_obj = wave.open(file_path, 'rb')
    global_vars.play_obj = sa.play_buffer(wave_obj.readframes(wave_obj.getnframes()), wave_obj.getnchannels(), wave_obj.getsampwidth(), wave_obj.getframerate())
    
def main_loop() -> None:
    global_vars.running = True
    
    if global_vars.play_obj != None:
        global_vars.play_obj.stop()


    while global_vars.running:
        print("Running...")
        
        pixel_color = get_pixel_color(global_vars.pixel_coordinates['x'], global_vars.pixel_coordinates['y'])


        if get_tuple_difference(pixel_color, global_vars.alert_color) <= global_vars.tolerancy:
            print("Notification detected!")
            global_vars.running = False
            play_sound(global_vars.sound_path)

        time.sleep(1)