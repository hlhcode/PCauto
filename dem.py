# -*- coding: utf-8 -*-
from time import sleep

from pywinauto import Application
from pywinauto.keyboard import send_keys
from pywinauto.timings import wait_until,Timings
# app = Application().start("notepad.exe")
# # 选择主窗口
# dlg = app["无标题 - 记事本"]
#
# # dlg.print_control_identifiers()
# menu = dlg["DesktopWindowXamlSource5"]
# menu.print_control_identifiers()

# file = menu.child_window()
# file.print_control_identifiers()
#
#
# sleep(3)
# print(menu.items())


# i = 0
#
#
# def work():
#     global i
#     i += 1
#     print("当前i的值为", i)
#     return i
#
#
# # 等待work返回的结果为5，继续往下执行
# wait_until(10, 1, work, 5)
# print("等待通过")

# app = Application().start("notepad.exe")
# # 选择主窗口
# dlg = app["无标题 - 记事本"]
# dlg.print_control_identifiers()
#
# # 选择编辑框
# dlg["Edit"].type_keys("pyrhon自动化,666")
#
# # 替换操作
# # 通过菜单选择替换
# dlg.menu_select("编辑->替换")
#
# app["替换"].print_control_identifiers()
# # 选择查找编辑框
# app["替换"]["Edit1"].type_keys("666")
# # 选择替换为编辑框
# app["替换"]["Edit2"].type_keys("999")
# # 选择全部替换按钮，进行点击
# app["替换"]["Butten3"].type_keys("999").click()

# 按F1
# send_keys("{F1}")
# send_keys("{VK_F1}")


# 通过按键打开 cmd ，进入python
# send_keys("{VK_LWIN}")
#
# send_keys("cmd")
#
# send_keys("{VK_RETURN}")

send_keys("{VK_LWIN}cmd{VK_RETURN}")