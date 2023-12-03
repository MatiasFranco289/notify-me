from dotenv import load_dotenv
import os
import global_vars
import ast

def prepare_app() -> None:
    print("Preparing app...")
    print("")

    if not os.path.exists(".env"):
        print("No .env file found")
        create_env_file()

    load_dotenv() 
    load_environment_variables()

def load_environment_variables() -> None:
    all_vars_loaded : bool = False
    environment_vars : dict = {
        "SOUND_PATH" : global_vars.sound_path, 
        "TOLERANCY": global_vars.tolerancy,
        "ALERT_COLOR": global_vars.alert_color, 
        "PIXEL_COORDINATES": global_vars.pixel_coordinates
        }

    while not all_vars_loaded:
        all_vars_loaded = True

        for key in environment_vars:
            environment_vars[key] = os.getenv(key)

            if(environment_vars[key] == None):
                print("Malformed .env file detected. Creating new one...")
                delete_env_file()
                create_env_file()
                load_dotenv()
                all_vars_loaded = False
                break
    
    global_vars.sound_path = environment_vars["SOUND_PATH"]
    global_vars.tolerancy = int(environment_vars["TOLERANCY"])
    global_vars.alert_color = ast.literal_eval(environment_vars["ALERT_COLOR"])
    global_vars.pixel_coordinates = ast.literal_eval(environment_vars["PIXEL_COORDINATES"])

    print("Environment variables loaded correctly")

def delete_env_file() -> None:
    print("Deleting .env file...")
    print("")

    try:
        os.remove(".env")
        print(".env file deleted correctly")
    except:
        print("Error while deleting .env file")
        exit(1)

def create_env_file() -> None:
    print("Creating .env file...")
    print("")

    try:
        with open(".env", "w") as file:
            file.write('SOUND_PATH = "alarm_sound.wav"\n')
            file.write('TOLERANCY = 0\n')
            file.write('ALERT_COLOR = (0, 0, 0, 0)\n')
            file.write("PIXEL_COORDINATES = {'x': 0, 'y': 0}\n")
        print("File created correctly")
    except:
        print("Error while creating .env file")
        exit(1)