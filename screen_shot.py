import os
import pyautogui


print('''

''')
path = os.path.join(os.path.expanduser('~'), 'pictures')

def screen_shot():


    mm = pyautogui.screenshot()
    mm.save(f'{path}\\new_screenshot.png')
    print("Screenshot saved...")
if __name__ == "__main__":
    screen_shot()
