# -*- coding: utf-8 -*-
from pywinauto import Application

app= Application(backend='win32')

app.start('notepad.exe')

app.connect(path='notepad.exe')

app.kill()