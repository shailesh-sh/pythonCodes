import time
import pyautogui
import os

count = 0
workspace = input("Enter the Workspace\n")
directory = input("Enter the folder Name\n")
if not os.path.exists(workspace+"\\"+directory):
    os.mkdir(workspace+"\\"+directory)


while True:
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    screenshot.save(workspace+"\\"+directory+"\\"+str(count)+".png")
    count += 1
    time.sleep(3600)

