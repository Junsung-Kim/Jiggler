import time
import random
import logging
from pynput import mouse, keyboard
import pyautogui

INACTIVITY_THRESHOLD = 30

last_user_activity_time = time.time()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def update_activity(*args):
    global last_user_activity_time
    last_user_activity_time = time.time()

mouse_listener = mouse.Listener(
    on_move=update_activity,
    on_click=update_activity,
    on_scroll=update_activity,
)
keyboard_listener = keyboard.Listener(on_press=update_activity)

mouse_listener.start()
keyboard_listener.start()

try:
    while True:
        current_time = time.time()
        if current_time - last_user_activity_time > INACTIVITY_THRESHOLD:
            old_x, old_y = pyautogui.position()
            screen_width, screen_height = pyautogui.size()
            new_x = random.randint(0, screen_width - 1)
            new_y = random.randint(0, screen_height - 1)

            pyautogui.moveTo(new_x, new_y)
            pyautogui.moveTo(old_x, old_y)

            logging.info(f"Mouse moved: ({old_x}, {old_y}) -> ({new_x}, {new_y})")

            last_user_activity_time = current_time

        time.sleep(5)
except KeyboardInterrupt:
    logging.info("Program terminated by user.")
finally:
    mouse_listener.stop()
    keyboard_listener.stop()
    logging.info("Listeners stopped. Exiting program.")
