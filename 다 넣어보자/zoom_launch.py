#줌 실행
import pyautogui
import subprocess
from time import sleep
#pyautogui.mouseInfo()
sleep(15)
subprocess.Popen([r"C:\Users\701\AppData\Roaming\Zoom\bin\Zoom.exe"])
sleep(4)
pyautogui.hotkey('Alt','space','x')
pyautogui.click(811,447,duration=1)
sleep(3)
pyautogui.click(851,486,duration=1)
pyautogui.write("4540269850")
pyautogui.click(987,652,duration=1)
sleep(3)
pyautogui.click(907,478,duration=1)
pyautogui.write("asiae5")
pyautogui.click(975,648,duration=1)