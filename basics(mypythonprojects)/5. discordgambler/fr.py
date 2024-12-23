from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(0)
i = 1
while True:
    time.sleep(6.5)
    keyboard.type('fr')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print(i)
    i += 1