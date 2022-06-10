# -*- coding: utf-8 -*-
from turtle import title

import pyautogui
import win32gui
import win32con
from time import sleep
from pywinauto.application import Application
import os
from pywinauto.keyboard import send_keys
from pywinauto.timings import wait_until,Timings

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
# print(dlg.wrapper_object())
# print(edit.wrapper_object())
# print(exep.wrapper_object())

# 2、获取该控件支持的方法：print(dir(a.wrapper_object()))
# print(dir(dlg.wrapper_object()))

# 控件的文本内容获取：texts
print(dlg.texts())

# 3、获取控件的子元素：children
# print(dlg.children())
# print(edit.children())
# print(exep.children())

# 4、获取控件类名：class_name
print(dlg.class_name)

# 5、以字典形式返回控件的属性：get_properties
print(dlg.get_properties)


# 八、控件及窗口的截图操作
# 截图处理方法:capture_as_image
# Pic = dlg.capture_as_image()
# print(Pic)
# Pic.save("0001.png")

# pic1 = edit.capture_as_image().save("002.png")

# pic2 = exep.capture_as_image().save("003.png")


# 九、菜单控件的操作方法
# items：获取所有的子菜单
# print(edit.items())

# item_by_index：根据索引、下标选定指定的菜单项
# m = edit.item_by_index(1)
# print(m)

# item_by_path：根据路径指定菜单项
# m = edit.item_by_path("文件->新建")
# print(m)

# 菜单项的操作方法：
# items：获取所有子选项
# print(exep.items())        存在问题，待解决

# click_input：点击菜单
# exep.click_input()
# edit.item_by_path("文件->新建").click_input()


# 十、pywinauto中的等待机制1
# 1、wait方法：
# 作用：等待窗口处于某个状态
# 参数：
# wait_for：等待的状态（状态有一下几种）
#     exists：表示该窗口是有效的句柄
#     visible:表示该窗口未隐藏
#     enabled:表示未禁用窗口
#     ready:表示该窗口可见并启用
#     active:表示该窗口处于活动状态
# timeout :超时时间
# retry_interval :重试时间间隔

# 等待窗口处于可见状态
# dlg.wait(wait_for="ready",timeout=10,retry_interval=1)
# print("kejian ")

# 2、Wait_not方法:
# 作用:等待窗口不处于某个特定状态参数:
#     wait_for :等待的状态(状态有以下几种)
#     exists:表示该窗口是有效的句柄
#     visible:表示该窗口未隐藏
#     enabled:表示未禁用窗口
#     ready:表示该窗口可见并启用
#     active:表示该窗口处于活动状态
# timeout :超时时间
# retry_interval :重试时间间隔

# 等待窗口处于不可见状态
# dlg.wait_not(wait_for_not="ready",timeout=10,retry_interval=1)
# print("不可见 ")

# 3、wait_cpu_usage_lower方法
# 等待该进程的cup的使用率低于某个阀值
# 注意:此方法仅适用于整个应用程序进程，不适用于窗口/元素。
#
# 参数:
# threshold :该进程cup占用率
# timeout :超时时间
# retry_interval :重试时间间隔

# app = Application().connect(process=33564)
# app.wait_cpu_usage_lower(threshold=5,timeout=5,usage_interval=1)
# print("当前进程CPU占用率低于%5")


# 十一、pywinauto中的等待机制2
# timings模块
# wait_until方法:
# 参数:
# Timeout:超时时间
# retry_interval 重试时间
# func 执行的函数
# value 比较的值
# Op 比较方式函数（默认为相等)
# args 给执行函数传位置参数
# kwargs 给执行函数传关键字参数

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


# 在执行许多动作需要在之前，之后和之间如果我们需要暂停。
# 那么模块timings中有几个方法库帮我们实现这种暂停操作。
# 通过在对象timings .Timings中设置全局静态变量（等待时间)，它可以单独根据您的需要进行调整。

# 全局计时变量值的设置方法
# Timings.defaults() :将全局计时设为默认值
# Timings.slow():将所有时间加倍（使脚本执行速度降低约2倍)
# Timings.fast():#将所有计时除以2（快2倍)


# 十二、编辑类型的控件操作
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


# 十三、模拟键盘的基本操作
# 键盘操作模块:pywinauto.keyboard
# Send_keys方法:
#     使用方式: send_keys(按键)
# 例如:
#     按F5: send_keys({VK_F5})
#     按F12: send_keys({VK_F12})
#     按回车键:send_keys({VK_RETURN})
#     按普通字母键: send_keys('A’)
#                 send_keys('A’)

# 常用按键
# ESC键:VK_ESCAPE (27)
# 回车键:VK_RETURN (13)
# TAB键: VK_TAB (9)
# Caps Lock键:VK_CAPITAL (20)
# Shift键: VK_SHIFT (16)
# Ctrl键:VK_CONTROL (17)
# Alt键:VK_MENU (18)
# 空格键: VK_SPACE(32)
# 退格键:VK_BACK(8)
# 左win键:VK_LWIN(91)
# 右win键:VK_RWIN(92)

# 按F1
# send_keys("{F1}")
# send_keys("{VK_F1}")

# 进入cmd
# send_keys("{VK_LWIN}")
#
# send_keys("cmd")
#
# send_keys("{VK_RETURN}")
send_keys("{VK_LWIN}cmd{VK_RETURN}")


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
