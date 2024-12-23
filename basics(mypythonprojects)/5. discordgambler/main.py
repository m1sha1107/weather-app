from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mcontroller
import time
keyboard = Controller()
mouse = mcontroller()
set = ['pls hunt', 'pls fish',  'pls dig', 'pls beg']
#set = ['fr']
click = [False, False, False, False]
pause = 6.5
interpause = 4
time.sleep(8)
count = 0
mouse.position = (412, 930)
while True:
    for i in range(0, len(set)):
        time.sleep(interpause)
        for j in set[i]:
            keyboard.type(j)
            time.sleep(0.05)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        if click[i]:
            mouse.position = (412, 930)
            time.sleep(2)
            mouse.click(Button.left, 1)
            mouse.position = (412, 996)
            time.sleep(0.1)
            mouse.click(Button.left, 1)
    count += 1
    print(count)
    time.sleep(pause)
