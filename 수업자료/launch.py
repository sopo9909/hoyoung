<<<<<<< HEAD
import pyautogui
import datetime

datetime.datetime.today()
now=datetime.datetime.now()

pyautogui.click(23,1060,duration=1)
pyautogui.click(373,705,duration=1)
pyautogui.sleep(12)
pyautogui.hotkey('Alt','space','x')

#pyautogui.mouseInfo()
pyautogui.click(84,96,button='right')
pyautogui.sleep(1)
pyautogui.moveTo(138,109,duration=1)
pyautogui.click(386,189,duration=1)
pyautogui.write(now.strftime('%m-%d'))
pyautogui.sleep(2)
pyautogui.press('enter')
=======
import pyautogui
import datetime

datetime.datetime.today()
now=datetime.datetime.now()

pyautogui.click(23,1060,duration=1)
pyautogui.click(373,705,duration=1)
pyautogui.sleep(12)
pyautogui.hotkey('Alt','space','x')

#pyautogui.mouseInfo()
pyautogui.click(84,96,button='right')
pyautogui.sleep(1)
pyautogui.moveTo(138,109,duration=1)
pyautogui.click(386,189,duration=1)
pyautogui.write(now.strftime('%m-%d'))
pyautogui.sleep(2)
pyautogui.press('enter')
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
