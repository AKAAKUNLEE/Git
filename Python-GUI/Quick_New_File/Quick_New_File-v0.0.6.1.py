#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py 
@File    ：Quick_New_File-v0.0.6.py
@IDE     ：PyCharm 
@Author  ：AKUNLEE
@Date    ：2024/10/3 11:58 
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import os

def create_file():
    file_path =entry_fpn.get() +"/" + entry_fn.get() + "." + extension_var.get()
    try:
        with open(file_path, 'w') as file:
            file.write("")
            messagebox.showinfo("成功", f"文件 {file_path} 创建成功")
    except Exception as e:
        messagebox.showerror("错误", f"创建文件失败: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_fpn.delete(0, tk.END)
        entry_fpn.insert(0, directory)

# 创建主窗口
root = tk.Tk()
root.title("文件创建器")

# 设置窗口大小
root.geometry("450x300")

# 创建标签
tk.Label(root, text='文件名:', font=('华文新魏', 14)).place(x=10, y=170)
tk.Label(root, text='文件地址:', font=('华文新魏', 14)).place(x=10, y=210)
# 创建输入框-新建文本文件
var_file_name = tk.StringVar()
# var_file_name.set('新建文本文件')
entry_fn = tk.Entry(root, textvariable=var_file_name, font=('华文新魏', 14))
entry_fn.place(x=120,y=175)

# 创建输入框-文件地址
var_filepath_name = tk.StringVar()
# var_filepath_name.set('D:\Git\Python\Python-GUI\Quick_New_File')
entry_fpn = tk.Entry(root, textvariable=var_filepath_name, font=('华文新魏', 14))
entry_fpn.place(x=120,y=215)

# 创建选择目录按钮
select_directory_button = tk.Button(root, text="选择目录", command=select_directory).place(x=360,y=215)

# 创建下拉菜单
extensions = ["txt", "csv", "json", "xml", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]
extension_var = tk.StringVar(root)
extension_var.set(extensions[1])  # 默认值

option_menu = tk.OptionMenu(root, extension_var, *extensions)
option_menu.place(x=360,y=175)

# 创建创建文件按钮
create_button = tk.Button(root, text="创建文件", command=create_file)
create_button.place(x=150,y=250)

# 运行主循环
root.mainloop()

