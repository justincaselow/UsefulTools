import pyautogui
from PIL import ImageGrab
from pyzbar import pyzbar
import webbrowser as wb

pyautogui.hotkey('printscreen')
img = ImageGrab.grabclipboard()
output = pyzbar.decode(img)
if not output:
    raise Exception("No QR code found on screen")
zoomUrl = output[0].data.decode('utf-8')
wb.open("http://" + zoomUrl)
