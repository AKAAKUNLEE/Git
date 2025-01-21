#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py 
@File    ：Quick_New_File-v0.0.6.2.py
@IDE     ：PyCharm 
@Author  ：AKUNLEE
@Date    ：2024/10/7 09:24 
"""
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os

# 创建文件页面
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

# 查看文件列表页面
def list_files():
    directory = filedialog.askdirectory()
    if directory:
        files = os.listdir(directory)
        listbox.delete(0, tk.END)  # 清空列表
        for file in files:
            listbox.insert(tk.END, file)

# 创建主窗口
root = tk.Tk()
root.title("文件管理器")

# 设置窗口大小
root.geometry("600x400")

# 创建 Notebook 组件
notebook = ttk.Notebook(root)

# 创建第一个页面（创建文件）
page1 = ttk.Frame(notebook)
notebook.add(page1, text="创建文件")

# 页面1的内容
label = tk.Label(page1, text="请输入文件路径（不包括扩展名）：")
label.pack(pady=10)

entry = tk.Entry(page1, width=50)
entry.pack(pady=10)

select_directory_button = tk.Button(page1, text="选择目录", command=select_directory)
select_directory_button.pack(pady=5)

extensions = ["txt", "csv", "json", "xml", "pdf"]
extension_var = tk.StringVar(page1)
extension_var.set(extensions[0])  # 默认值

option_menu = tk.OptionMenu(page1, extension_var, *extensions)
option_menu.pack(pady=10)

create_button = tk.Button(page1, text="创建文件", command=create_file)
create_button.pack(pady=10)

# 创建第二个页面（查看文件列表）
page2 = ttk.Frame(notebook)
notebook.add(page2, text="查看文件列表")

# 页面2的内容
list_label = tk.Label(page2, text="选择目录查看文件列表：")
list_label.pack(pady=10)

list_button = tk.Button(page2, text="选择目录", command=list_files)
list_button.pack(pady=5)

listbox = tk.Listbox(page2, width=50, height=10)
listbox.pack(pady=10)

# 显示 Notebook
notebook.pack(expand=1, fill="both")

# 运行主循环
root.mainloop()
