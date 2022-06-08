# -*- coding: utf-8 -*-
from turtle import title

import pyautogui
import win32gui
import win32con
from time import sleep
from pywinauto.application import Application
import os
os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
# 打开应用
app= Application(backend='win32')

# 连接应用
aap_path=r'D:\installfile\公路算量\BimHighway\MCTech.CQ.Acad.Launcher.exe'
app.start(aap_path)

app.connect(path=aap_path)
sleep(5)

# 定位到窗口（class_name:窗口类名，title：窗口标题）
dlg = app.window(class_name='WindowsForms10.Window.8.app.0.3ddfb6e_r6_ad1',title="梦诚BIM公路算量")
print(dlg)
dlg = app.window(class_name="WindowsForms10.Window.b.app.0.3ddfb6e_r6_ad1",title="取消")
print(dlg)
x,y = pyautogui.position()
print(x,y)
pyautogui.moveTo(x=1500,y=645,duration=2,tween=pyautogui.linear)
pyautogui.doubleClick()
pyautogui.typewrite(message='15719323447',interval=0.25)
sleep(1)
pyautogui.moveTo(x=1500,y=685,duration=2,tween=pyautogui.linear)
pyautogui.doubleClick()
pyautogui.typewrite(message='huanglihui',interval=0.25)
pyautogui.press('Enter')
pyautogui.moveTo(x=1500,y=760,duration=2,tween=pyautogui.linear)
pyautogui.click()





# 关闭应用 https://blog.csdn.net/m0_37602827/article/details/108308991
sleep(3)
# app.kill()