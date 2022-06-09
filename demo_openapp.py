# -*- coding: utf-8 -*-
from turtle import title

import pyautogui
import win32gui
import win32con
from time import sleep
from pywinauto.application import Application
import os

os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})


# 一、 打开应用
app = Application(backend='uia')
app_path = r"D:\installfile\公路算量\BimHighway\MCTech.CQ.Acad.Launcher.exe"
app.start(app_path)


# 二、连接应用
# 通过进程连接
# app.connect(process=7972)

# 通过窗口句柄进行连接
# app.connect(handle=38145116)

# 通过运行地址进行连接
# app.connect(path=app_path)

print(app)
sleep(5)


# 三、选择指定窗口
# 方式一   app[类名/标题]
# 通过类名来选择窗口
# dlg = app["WindowsForms10.Window.8.app.0.3ddfb6e_r6_ad1ad1"]

# 通过窗口标题来选择窗口
dlg = app["梦诚BIM公路算量"]

# 方式二   app.窗口类名
# dlg = app.WindowsForms10
#
# # app.标题
# dlg = app.title

# 打印窗口中所有的控件
# dlg.print_control_identifiers()


# 四、窗口的操作方法
# 窗口最大化
# dlg.maximize()

# 窗口最小化
# dlg.minimize()

# 窗口恢复正常大小
# dlg.restore()

# 查找窗口显示状态:最大化是：1    正常是：0
# ststus = dlg.get_show_state()
# print(ststus)

# 获取窗口坐标
# cooder = dlg.rectangle()
# print(cooder)

#关闭窗口
# sleep(5)
# dlg.close()


# 五、窗口控件操作
# 查看窗口上所有的控件
# dlg.print_control_identifiers()

# 选中控件
# 方式一
# edit = dlg.Edit4
# print(edit.print_control_identifiers())

# 方式二
edit = dlg["Edit4"]
# print(edit.print_control_identifiers())

# 方式三
exep = edit.child_window(title="打开", control_type="Button")
# exep.print_control_identifiers()


# 六、控件的分类
# 状态栏:StatusBar
# 静态内容:Static
# 按钮:Button
# 复选框:CheckBox
# 单选框:RadioButton
# 组框:GroupBox
# 组合框:ComboBox
# 对话框(窗口): Dialog
# 编辑栏: Edit
# 头部内容:Header
# 列表框:ListBox
# 列表显示控件: ListView
# 弹出菜单:PopupMenu
# 选项卡控件TabControl
# 工具栏:Toolbar
# 工具提示:ToolTips
# 树状视图:Tree View
# 菜单:Menu
# 菜单项:MenuItem
# 窗格:Pane
# 标题栏：TitleBar


# 七、窗口控件基本属性获取方法    https://www.bilibili.com/video/BV1nR4y137sV?p=11&spm_id_from=pageDriver
# 1、获取控件类型：wrapper_object()
print(dlg.wrapper_object())
print(edit.wrapper_object())
print(exep.wrapper_object())

# 2、获取该控件支持的方法：print(dir(a.wrapper_object()))
print(dir(dlg.wrapper_object()))

# 控件的文本内容获取：texts
print(dlg.texts())

# 3、获取控件的子元素：children
print(dlg.children())
print(edit.children())
print(exep.children())

# 4、获取控件类名：class_name
print(dlg.class_name)

# 5、以字典形式返回控件的属性：get_properties
print(dlg.get_properties)


# # 定位到窗口（class_name:窗口类名，title：窗口标题）
# dlg = app.window(class_name='WindowsForms10.Window.8.app.0.3ddfb6e_r6_ad1',title="梦诚BIM公路算量")
# print(dlg)
# dlg = app.window(class_name="WindowsForms10.Window.b.app.0.3ddfb6e_r6_ad1",title="取消")
# print(dlg)
# x,y = pyautogui.position()
# print(x,y)
# pyautogui.moveTo(x=1500,y=645,duration=2,tween=pyautogui.linear)
# pyautogui.doubleClick()
# pyautogui.typewrite(message='15719323447',interval=0.25)
# sleep(1)
# pyautogui.moveTo(x=1500,y=685,duration=2,tween=pyautogui.linear)
# pyautogui.doubleClick()
# pyautogui.typewrite(message='huanglihui',interval=0.25)
# pyautogui.press('Enter')
# pyautogui.moveTo(x=1500,y=760,duration=2,tween=pyautogui.linear)
# pyautogui.click()


# 关闭应用 https://blog.csdn.net/m0_37602827/article/details/108308991
# https://www.bilibili.com/video/BV1nR4y137sV?spm_id_from=333.337.search-card.all.click
sleep(3)
# app.kill()
