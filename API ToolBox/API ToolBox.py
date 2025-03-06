import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pyperclip  # 用于操作剪切板

# API URL
API_URL = "https://api.okcode.vip/api/dev/html_link"


def fetch_data():
    """调用API并显示数据"""
    key = entry_key.get()  # 获取用户输入的网页链接

    if not key:
        messagebox.showwarning("提示", "要提取的网页链接:")
        return

    # 请求参数
    params = {"key": key}

    try:
        # 发送 GET 请求
        response = requests.get(API_URL, params=params)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析 JSON 响应
            data = response.json()
            result_text.delete(1.0, tk.END)  # 清空文本框
            result_text.insert(tk.END, str(data))  # 显示JSON数据
        else:
            messagebox.showerror("错误", f"请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        messagebox.showerror("错误", f"请求异常：{e}")


def paste_from_clipboard():
    """从剪切板粘贴内容到输入框"""
    try:
        clipboard_text = pyperclip.paste()  # 获取剪切板内容
        entry_key.delete(0, tk.END)  # 清空输入框
        entry_key.insert(0, clipboard_text)  # 粘贴内容
    except Exception as e:
        messagebox.showerror("错误", f"读取剪切板失败：{e}")


def clear_input():
    """清空输入框"""
    entry_key.delete(0, tk.END)


# 创建主窗口
root = tk.Tk()
root.title("API工具箱")
root.geometry("500x400")

# 设置主题 (需要安装 ttkthemes)
try:
    from ttkthemes import ThemedTk

    root = ThemedTk(theme="arc")  # 使用 'arc' 主题，可以根据需要更换
    root.title("API工具箱 (支持主题)")
    root.geometry("500x400")
except ImportError:
    print("ttkthemes 未安装，使用默认主题")

# 创建控件
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

label_key = ttk.Label(frame, text="要提取的网页链接:")
label_key.grid(column=0, row=0, sticky=tk.W)

entry_key = ttk.Entry(frame, width=40)
entry_key.grid(column=1, row=0, sticky=tk.EW)

# 将所有按钮放在同一行
button_frame = ttk.Frame(frame)
button_frame.grid(column=0, row=1, columnspan=4, pady=10)

button_paste = ttk.Button(button_frame, text="读取剪切板", command=paste_from_clipboard)
button_paste.pack(side=tk.LEFT, padx=5)

button_clear = ttk.Button(button_frame, text="清空输入", command=clear_input)
button_clear.pack(side=tk.LEFT, padx=5)

button_fetch = ttk.Button(button_frame, text="获取数据", command=fetch_data)
button_fetch.pack(side=tk.LEFT, padx=5)

result_text = tk.Text(frame, wrap=tk.WORD, height=15)
result_text.grid(column=0, row=2, columnspan=4, sticky=tk.EW)

# 设置窗口布局
frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# 运行主循环
root.mainloop()
