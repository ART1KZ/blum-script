import pyautogui
import cv2
import numpy as np
import concurrent.futures
import time
import keyboard
from pynput.mouse import Button, Controller
import pygetwindow as gw
import tkinter as tk
from tkinter import simpledialog
import base64
from colorama import Fore
import random

mouse = Controller()

WIND = 0.2  # Сдвиг окна

star_templates_10s = [
    ('6', cv2.imread('6.png', cv2.IMREAD_COLOR)),
    ('7', cv2.imread('7.png', cv2.IMREAD_COLOR)),
    ('9', cv2.imread('9.png', cv2.IMREAD_COLOR)),
    ('16', cv2.imread('16.png', cv2.IMREAD_COLOR)),
]

star_templates_p = [
    ('8', cv2.imread('8.png', cv2.IMREAD_COLOR)),
    ('10', cv2.imread('10.png', cv2.IMREAD_COLOR)),
    ('11', cv2.imread('11.png', cv2.IMREAD_COLOR)),
    ('12', cv2.imread('12.png', cv2.IMREAD_COLOR)),
    ('16', cv2.imread('16.png', cv2.IMREAD_COLOR)),
    ('18', cv2.imread('18.png', cv2.IMREAD_COLOR)),
    ('19', cv2.imread('19.png', cv2.IMREAD_COLOR))
]

def click(xs, ys):
    mouse.position = (xs, ys)
    mouse.press(Button.left)
    mouse.release(Button.left)

def choose_window_gui():
    root = tk.Tk()
    root.withdraw()
    windows = gw.getAllTitles()
    if not windows:
        return None
    choice = simpledialog.askstring(f"{Fore.LIGHTWHITE_EX}Выбор окна Telegram", "Введите номер окна:\n" + "\n".join(
        f"{i}: {window}" for i, window in enumerate(windows)))
    if choice is None or not choice.isdigit():
        return None
    choice = int(choice)
    if 0 <= choice < len(windows):
        return windows[choice]
    else:
        return None

def grab_screen(region, scale_factor=0.5):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    new_width = int(screenshot.shape[1] * scale_factor)
    new_height = int(screenshot.shape[0] * scale_factor)
    resized_screenshot = cv2.resize(screenshot, (new_width, new_height))
    return resized_screenshot

def find_template_on_screen(template, screenshot, step=0.7, scale_factor=0.5):
    new_width = int(template.shape[1] * scale_factor)
    new_height = int(template.shape[0] * scale_factor)
    resized_template = cv2.resize(template, (new_width, new_height))
    result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= step:
        return (int(max_loc[0] / scale_factor), int(max_loc[1] / scale_factor))
    return None

def click_on_screen(position, template_width, template_height, region_left, region_top):
    center_x = position[0] + template_width // 2
    center_y = position[1] + template_height // 2
    click(center_x + region_left, center_y + region_top + 4)

def process_template(template_data, screenshot, scale_factor, region_left, region_top, click_counts):
    template_name, template = template_data
    if template is None:
        print(f"{Fore.LIGHTRED_EX}Ошибка загрузки {template_name}")
        return template_name, None
    position = find_template_on_screen(template, screenshot, scale_factor=scale_factor)
    if position:
        template_height, template_width, _ = template.shape
        if template_name == '6' and click_counts['6'] > 1:
            click_on_screen(position, template_width, template_height, region_left, region_top)
            click_counts['6'] -= 1

        elif template_name == '7' and click_counts['6'] > 1:
            center_x = (telegram_window.left+int(telegram_window.width*0.05)) + (telegram_window.width-int(telegram_window.width*0.12)) // 2
            center_y = (telegram_window.top+int(telegram_window.height*WIND)) + (int(telegram_window.height*(0.92-WIND))) // 2
            mouse.position = (center_x, center_y)
            time.sleep(0.3)
            mouse.scroll(0, 2)
            mouse.scroll(0, -200)
            time.sleep(0.3)

            position_8 = find_template_on_screen(star_templates_p[-1][1], screenshot, scale_factor=scale_factor)
            if position_8:
                click_on_screen(position_8, template_width, template_height, region_left, region_top)
                click_counts['6'] -= 1

        elif template_name == '9':
            click_on_screen(position, template_width, template_height, region_left, region_top)

        return template_name, position
    return template_name, None

def color_range(r, g, b):
    return ((r in range(90, 110) and g in range(125, 150) and b in range(85, 95)) or
            (r in range(200, 255) and g in range(35, 65) and b in range(180, 205)) or
            (r in range(50, 105) and g in range(110, 175) and b in range(5, 40)) or
            (r in range(185, 255) and g in range(0, 2) and b in range(155, 200)) or
            (r in range(90, 130) and g in range(165, 210) and b in range(20, 85)) or
            (r in range(130, 180) and g in range(55, 75) and b in range(5, 20)) or
            (r in range(190, 240) and g in range(10, 35) and b in range(100, 175)) or
            (r in range(235, 255) and g in range(150, 185) and b in range(0, 15)) or
            (r in range(85, 105) and g in range(135, 175) and b in range(15, 55)))

window_name = "TelegramDesktop"
check = gw.getWindowsWithTitle(window_name)
encoded = b'0JDQstGC0L7RgCDRgdC60YDQuNC/0YLQsCBhcnR5azE4MDcgKGh0dHBzOi8vZnVucGF5LmNvbS91c2Vycy8zMzA1MzUzLykuINCf0LXRgNC10L/RgNC+0LTQsNC20LAg0YHQutGA0LjQv9GC0LAg0LfQsNC/0YDQtdGJ0LXQvdCwLg=='
print(f"{Fore.LIGHTYELLOW_EX}{base64.b64decode(encoded).decode('utf-8')}")

if not check:
    print(f"{Fore.LIGHTRED_EX}\nОкно {window_name} не найдено!\nПожалуйста, выберите другое окно.")
    window_name = choose_window_gui()

if not window_name or not gw.getWindowsWithTitle(window_name):
    print(f"{Fore.LIGHTRED_EX}\nНе удалось найти указанное окно!\nЗапустите Telegram, после чего перезапустите бота!")
else:
    print(f"{Fore.LIGHTBLUE_EX}\nОкно {window_name} найдено\n")
    num = input(f"{Fore.LIGHTYELLOW_EX}Укажите количество игр, что нужно отыграть:\n")
    click_counts = {'6': int(num)}
    print(f"{Fore.LIGHTBLUE_EX}Нажмите 'S' для старта.")

telegram_window = gw.getWindowsWithTitle(window_name)[0]
paused = True
last_check_time = time.time()
last_blue_check_time = time.time()
last_pause_time = time.time()
last_check_time_10s = time.time()
last_check_time_5s = time.time()
end_time = None

while True:
    if keyboard.is_pressed('S') and time.time() - last_pause_time > 0.1:
        paused = not paused
        last_pause_time = time.time()
        if paused:
            print(f'{Fore.LIGHTBLUE_EX}Пауза')
        else:
            print(f'{Fore.LIGHTBLUE_EX}Работаю')
            print(f"{Fore.LIGHTBLUE_EX}Для паузы нажми 'S'")
        time.sleep(0.2)

    window_rect = (
        telegram_window.left+int(telegram_window.width*0.05),
        telegram_window.top+int(telegram_window.height*WIND),
        telegram_window.width-int(telegram_window.width*0.12),
        int(telegram_window.height*(0.92-WIND))
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    if not paused and click_counts['6'] > 0:
        screenshot = grab_screen(window_rect)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            current_time = time.time()

            if current_time - last_check_time_10s >= 5:
                futures += [executor.submit(process_template, template_data, screenshot, 0.5, (telegram_window.left+int(telegram_window.width*0.05)), (telegram_window.top+int(telegram_window.height*WIND)), click_counts) for template_data in star_templates_10s]
                last_check_time_10s = current_time

            for future in concurrent.futures.as_completed(futures):
                template_name, position = future.result()

        screenshot_pix = pyautogui.screenshot(region=window_rect)
        width, height = screenshot_pix.size
        for x in range(0, width, 20):
            for y in range(0, height, 20):
                r, g, b = screenshot_pix.getpixel((x, y))
                if color_range(r, g, b):
                    click(x + random.uniform(1, 2)+window_rect[0], y + random.uniform(1, 2)+window_rect[1])
                    time.sleep(0.01)
                    break

    if click_counts['6'] == 1:
        if not end_time:
            end_time = time.time() + 50
            print(f'{Fore.LIGHTWHITE_EX}Достигнуто заданное количество игр')

    if end_time and time.time() >= end_time:
        break

print(f'{Fore.LIGHTRED_EX}Стоп')
