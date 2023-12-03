from prepare import prepare_app
from options import view_current_settings
from options import set_tolerancy
from options import set_alert_color
from options import set_sound_path
from options import set_pixel_coordinates
from watcher import main_loop

def main_menu() -> None:
    options : dict = {
        "1" : main_loop,
        "2" : view_current_settings,
        "3" : set_pixel_coordinates,
        "4" : set_tolerancy,
        "5" : set_alert_color,
        "6" : set_sound_path,
        "7" : exit
    }

    while True:
        print("")
        print("1 - Start")
        print("2 - View current settings")
        print("3 - Set pixel coordinates")
        print("4 - Set tolerancy")
        print("5 - Set alert color")
        print("6 - Set sound path")
        print("7 - Exit")
        print("")
        
        user_input = input("Enter your choice: ")
        options[user_input]()

print("Welcome to notify me!")
prepare_app()
main_menu()