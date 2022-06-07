# -*- coding: utf-8 -*-
from pywinauto import application

app = application.Application().start('notepad.exe')
# app = application.Application().start('calc.exe')
# app = application.Application().start('clock.exe')

chuangkou = '无标题-记事本'
# print(app[chuangkou].print_control_identifiers())

app[chuangkou].Edit.type_keys('hahah\n',with_spaces=True,with_newlines=True)
app[chuangkou].Edit.type_keys('nihao\n',with_spaces=True,with_newlines=True)

app[chuangkou].menu_select
    # ('文件->退出')