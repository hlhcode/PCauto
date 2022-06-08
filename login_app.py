# -*- coding: utf-8 -*-
import pyautogui
from time import sleep
from open_app import app


def login_app(class_name, title):
    dlg = app.window(class_name=class_name, title=title)
    x, y = pyautogui.position()
    pyautogui.moveTo(x=1500, y=645, duration=2, tween=pyautogui.linear)
    pyautogui.doubleClick()
    pyautogui.typewrite(message='15719323447', interval=0.25)
    sleep(1)
    pyautogui.moveTo(x=1500, y=685, duration=2, tween=pyautogui.linear)
    pyautogui.doubleClick()
    pyautogui.typewrite(message='huanglihui', interval=0.25)
    pyautogui.press('Enter')
    pyautogui.moveTo(x=1500, y=760, duration=2, tween=pyautogui.linear)
    pyautogui.click()
