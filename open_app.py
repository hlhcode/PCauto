# -*- coding: utf-8 -*-
from pywinauto.application import Application
import os

os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
app = Application(backend='win32')

def openapp(app_path):
    # 打开应用
    app.start(app_path)
    # 连接应用
    app.connect(path=app_path)

def close_app():
    # 关闭应用
    app.kill()

# a= r'D:\installfile\公路算量\BimHighway\MCTech.CQ.Acad.Launcher.exe'
# openapp(a)
# close_app()