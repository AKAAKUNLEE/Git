#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py 
@File    ：WEI-a_to_p.py
@IDE     ：PyCharm 
@Author  ：AKUNLEE
@Date    ：2024/10/7 17:26 
"""
from flask import Flask, request
from winotify import Notification
import urllib.parse
import win32gui
import win32con

app = Flask(__name__)


@app.route('/')  # 获取url信息
def getUrlInfo():
    # 完整url
    url = request.url
    # 主机部分
    hostUrl = request.host_url
    # 访问路径
    fullPath = request.full_path
    # 处理空格转为+的问题
    fullPath = fullPath.replace('+', ' ')
    # 输出
    print('收到推送任务，推送内容是：' +
          str(
              urllib.parse.unquote(
                  fullPath.split("/?")[1]
              )
          ).replace('+', ' ', 1)
          )

    # 接收到的内容
    content = str(
        urllib.parse.unquote(fullPath.split("/?")[1])
    ).replace('+', ' ', 1)

    hwnd = win32gui.FindWindow("WeChatMainWndForPC", u"微信")

    if win32gui.IsWindowVisible(hwnd):
        print('不推送')
        return "not push"
    else:
        print('推送开始')
        titleNameCheck = "$$$" in content

        if titleNameCheck == True:
            nickname = content.split("$$$")[0]
            weixinMsg = content.split("$$$")[1]
        else:
            nickname = '微信消息通知'
            weixinMsg = content

        # 开发Push通知
        # toaster = ToastNotifier()
        # toaster.show_toast(title=nickname, msg=weixinMsg,icon_path="logo.ico", duration=5)
        toast = Notification(
            app_id="微信",
            title=nickname,
            msg=weixinMsg,
            icon="D:/noticeWeChatMsg/weixin.png"
        )
        toast.show()
        print('推送结束')
        return "push ok"


# def notify(hwnd, msg, wparam, lparam):
#     # print("notify", msg)
#     if lparam == win32con.WM_LBUTTONDBLCLK:  # 双击左键
#         print("双击左键", msg)
#         pass
#     elif lparam == win32con.WM_RBUTTONUP:  # 右键弹起
#         print("右键弹起", msg)
#         pass
#     elif lparam == win32con.WM_LBUTTONUP:  # 左键弹起
#         print("左键弹起", msg)
#         pass
#     return True


# wc = win32gui.WNDCLASS()
# wc.hInstance = win32gui.GetModuleHandle(None)
# wc.lpszClassName = "微信新消息通知"
# wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
# wc.lpfnWndProc = notify
# classAtom = win32gui.RegisterClass(wc)
# hwnd = win32gui.CreateWindow(
#     classAtom,
#     "tst2",
#     win32con.WS_OVERLAPPEDWINDOW,
#     win32con.CW_USEDEFAULT,
#     win32con.CW_USEDEFAULT,
#     win32con.CW_USEDEFAULT,
#     win32con.CW_USEDEFAULT,
#     None,
#     None,
#     None,
#     None
# )
# notify_id = (
#     hwnd,
#     0,
#     win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
#     win32con.WM_USER + 20,
#     win32gui.LoadIcon(
#         0,
#         win32con.IDI_APPLICATION
#     ),
#     "微信新消息通知"
# )
# win32gui.Shell_NotifyIcon(0, notify_id)


# win32gui.PumpMessages()
# 在指定IP和端口开启HTTP服务
if __name__ == '__main__':
    app.run(debug=False, host='192.168.1.5', port=9998)