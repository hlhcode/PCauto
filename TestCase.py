# -*- coding: utf-8 -*-
import open_app
from login_app import login_app


def test_case(app_path, class_name, title):
    open_app(app_path)
    login_app(class_name, title)


app_path = r'D:\installfile\公路算量\BimHighway\MCTech.CQ.Acad.Launcher.exe'
class_name = 'WindowsForms10.Window.8.app.0.3ddfb6e_r6_ad1'
title = "梦诚BIM公路算量"
test_case(app_path, class_name, title)
