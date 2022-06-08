# -*- coding: utf-8 -*-
from pywinauto.application import Application

# 打开应用
app= Application(backend='win32')

# 连接应用
app.start('notepad.exe')

app.connect(path='notepad.exe')


dlg =app.window(class_name,title)
# dlg = app.class_name
# dlg = app[title]
app.Notepad.print_control_identifiers()
# 关闭应用 https://blog.csdn.net/m0_37602827/article/details/108308991
app.kill()