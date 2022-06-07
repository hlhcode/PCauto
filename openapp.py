# -*- coding: utf-8 -*-
from pywinauto import Application

# 打开应用
app= Application(backend='win32')

# 连接应用
app.start('notepad.exe')


app.connect(path='notepad.exe')

# 关闭应用 https://blog.csdn.net/m0_37602827/article/details/108308991
app.kill()