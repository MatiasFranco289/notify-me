from pynput import mouse
import global_vars
import os

def view_current_settings() -> None:
    print("")
    print("Current settings:")
    print("")
    print("Pixel coordinates: ", global_vars.pixel_coordinates)
    print("Tolerancy: ", global_vars.tolerancy)
    print("Alert color: ", global_vars.alert_color)
    print("Sound path: ", global_vars.sound_path)
    print("")

def set_tolerancy() -> None:
    tolerancy_setted : bool = False
    print("Tolerancy is the maximum difference between the alert color and the pixel color between 0 and 900")
    
    while not tolerancy_setted:
        try:
            n : int = int(input("Enter the tolerancy: "))

            if n < 0 or n > 900:
                print("Invalid input please enter an integer between 0 and 900")
                continue
            
            global_vars.tolerancy = n
            write_env("TOLERANCY", str(n))
            tolerancy_setted = True

            print("")
            print("Tolerancy setted correctly in ", n)
        except ValueError:
            print("Invalid input please enter an integer")

def write_env(var_name, var_value) -> None:

    try:
        with open(".env", "r") as file:
            lines = file.readlines()
    except:
        print("Error while opening .env file")
        exit(1)
    
    try:
        with open(".env", "w") as file:
            for line in lines:
                if var_name in line:
                    file.write(var_name + " = " + var_value + "\n")
                else:
                    file.write(line)
    except:
        print("Error while writing .env file")
        exit(1)

def set_alert_color() -> None:
    alert_color_setted : bool = False
    color = {
            "red" : None,
            "green" : None,
            "blue" : None,
            "alpha" : None
        }
    
    print("Alert color is the color that will trigger the notification")
    
    while not alert_color_setted:
        alert_color_setted = color["red"] != None and color["green"] != None and color["blue"] != None and color["alpha"] != None

        try:
            for key in color:
                if color[key] != None: continue

                n : int = int(input("Enter the " + key + " value: "))

                if n < 0 or n > 255:
                    print("Invalid input please enter an integer between 0 and 255")
                    break

                color[key] = n
            
            global_vars.alert_color = (color["red"], color["green"], color["blue"], color["alpha"])
            write_env("ALERT_COLOR", str(global_vars.alert_color))
            print("")
            print("Alert color setted correctly in ", color)

        except ValueError:
            print("Invalid input please enter an integer")

def set_sound_path() -> None:
    sound_path_setted : bool = False
    print("Sound path is the path to the sound that will be played when the notification is triggered")
    
    while not sound_path_setted:
        try:
            path : str = input("Enter the sound path: ")

            if not os.path.exists(path):
                print("Invalid path")
                continue
            
            global_vars.sound_path = path
            write_env("SOUND_PATH", path)
            sound_path_setted = True

            print("")
            print("Sound path setted correctly in ", path)
        except ValueError:
            print("Invalid input please enter an integer")

def set_pixel_coordinates(pixel_position = None) -> None:
    if pixel_position == None:
        print("Click on the pixel that will be checked periodically")
        print("Waiting for click...")
        
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    else:
        global_vars.pixel_coordinates = pixel_position
        write_env("PIXEL_COORDINATES", str(pixel_position))
        print("")
        print("Pixel coordinates setted correctly in ", pixel_position)


def on_click(x, y, button, pressed):
    if button != mouse.Button.left or not pressed: return

    mouse_x : float = x
    mouse_y : float = y

    set_pixel_coordinates({"x": mouse_x, "y": mouse_y})
    return False
