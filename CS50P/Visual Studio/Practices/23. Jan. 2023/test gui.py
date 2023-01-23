import pyautogui as jb
import time

limit = input("Text Limit: ")
text = input("What's on your mind?\n").strip()
i = 2

time.sleep(10)
while i <= int(limit) :
        jb.typewrite(text + ' ' + str(i))
        jb.press("Enter")
        i += 2