import time
import random

import pyautogui
from pynput import mouse, keyboard

# 사용자 활동 감지 변수
is_user_active = False
last_user_activity_time = time.time()

# 사용자 입력 감지 핸들러
def on_move(x, y):
    global is_user_active, last_user_activity_time
    is_user_active = True
    last_user_activity_time = time.time()

def on_click(x, y, button, pressed):
    global is_user_active, last_user_activity_time
    is_user_active = True
    last_user_activity_time = time.time()

def on_scroll(x, y, dx, dy):
    global is_user_active, last_user_activity_time
    is_user_active = True
    last_user_activity_time = time.time()

def on_key_press(key):
    global is_user_active, last_user_activity_time
    is_user_active = True
    last_user_activity_time = time.time()

# 입력 감지 리스너 설정
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_key_press)

mouse_listener.start()
keyboard_listener.start()

try:
    while True:
        current_time = time.time()
        if not is_user_active and current_time - last_user_activity_time > 30:
            old_x, old_y = pyautogui.position().x, pyautogui.position().y
            new_x, new_y = random.randint(0, pyautogui.size().width), random.randint(0, pyautogui.size().height)
            pyautogui.moveTo(new_x, new_y)
            pyautogui.moveTo(old_x, old_y)
            localtime = time.localtime()
            result = time.strftime("%I:%M:%S %p", localtime)
            print(f'Moved at {result} ({new_x}, {new_y}) <-> ({old_x}, {old_y})')
            last_user_activity_time = time.time()
        else:
            # 활동 감지 상태 초기화
            is_user_active = False

        time.sleep(5)
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    mouse_listener.stop()
    keyboard_listener.stop()
