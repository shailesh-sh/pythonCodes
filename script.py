from pynput.keyboard import Key,Controller
import subprocess
import time

print("Begin")
filename = input("Enter the file Name from which you want to copy\n")
input1 = input("Enter the start to initiate\n")

if input1 == "start":
    subprocess.Popen(['C:\\Program Files (x86)\\ogs\\Notepadapp.exe'])
    keyboard = Controller()
    time.sleep(2)
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of file")
                break
            if c == '\n':
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            keyboard.press(c)
            keyboard.release(c)

