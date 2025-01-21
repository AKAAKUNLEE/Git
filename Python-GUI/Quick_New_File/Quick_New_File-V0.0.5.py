#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py 
@File    ：Quick_New_File-V0.0.5.py
@IDE     ：PyCharm 
@Author  ：AKUNLEE
@Date    ：2024/10/3 11:51 
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import os

def create_file():
    file_path = entry.get() + "." + extension_var.get()
    try:
        with open(file_path, 'w') as file:
            file.write("")
            messagebox.showinfo("成功", f"文件 {file_path} 创建成功")
    except Exception as e:
        messagebox.showerror("错误", f"创建文件失败: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry.delete(0, tk.END)
        entry.insert(0, directory)

# 创建主窗口
root = tk.Tk()
root.title("文件创建器")

# 设置窗口大小
root.geometry("400x250")

# 创建标签
label = tk.Label(root, text="请输入文件路径（不包括扩展名）：")
label.pack(pady=10)

# 创建输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 创建选择目录按钮
select_button = tk.Button(root, text="选择目录", command=select_directory)
select_button.pack(pady=5)

# 创建下拉菜单
extensions = ["txt", "csv", "json", "xml", "pdf"]
extension_var = tk.StringVar(root)
extension_var.set(extensions[0])  # 默认值

option_menu = tk.OptionMenu(root, extension_var, *extensions)
option_menu.pack(pady=10)

# 创建创建文件按钮
create_button = tk.Button(root, text="创建文件", command=create_file)
create_button.pack(pady=10)

# 运行主循环
root.mainloop()
