import pyautogui
import datetime
from time import sleep
from pywinauto import Desktop
import subprocess
#pyautogui.mouseInfo()
subprocess.Popen([r"C:\Users\701\AppData\Roaming\Zoom\bin\Zoom.exe"])
sleep(2)
#pyautogui.hotkey('F6')
pyautogui.hotkey('Alt','space','x')
pyautogui.click(665,446,duration=1)
sleep(1)
pyautogui.hotkey('Alt','space','x')
sleep(2)
pyautogui.hotkey('Alt','F2')
sleep(3)
now = datetime.datetime.now()
#pyautogui.mouseInfo()
filename = now.strftime('%Y-%m-%d %H-%M-%S')
print(filename)
pyautogui.screenshot(str(filename)+'.png')