# -*- coding: utf-8 -*-
from pywinauto.application import Application

app = Application(backend='win32')

def openapp(app_path):
    # 打开应用
    app.start(app_path)
    # 连接应用
    app.connect(path=app_path)

def close_app():
    # 关闭应用
    app.kill()


# openapp('notepad.exe')
# close_app()