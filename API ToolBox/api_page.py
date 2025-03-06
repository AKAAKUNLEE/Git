import tkinter as tk
from tkinter import ttk  # 显式导入 ttk 模块
from tkinter import messagebox
from api_handler import fetch_data
from clipboard_handler import paste_from_clipboard


class APIPage(tk.ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        """创建提取网页链接页面控件"""
        # 输入框和标签
        label_key = tk.ttk.Label(self, text="要提取的网页链接:")
        label_key.grid(column=0, row=0, sticky=tk.W)

        self.entry_key = tk.ttk.Entry(self, width=40)
        self.entry_key.grid(column=1, row=0, sticky=tk.EW)

        # 按钮在同一行
        button_frame = tk.ttk.Frame(self)
        button_frame.grid(column=0, row=1, columnspan=4, pady=10)

        button_paste = tk.ttk.Button(button_frame, text="读取剪切板", command=self.on_paste)
        button_paste.pack(side=tk.LEFT, padx=5)

        button_clear = tk.ttk.Button(button_frame, text="清空输入", command=self.on_clear)
        button_clear.pack(side=tk.LEFT, padx=5)

        button_fetch = tk.ttk.Button(button_frame, text="获取数据", command=self.on_fetch)
        button_fetch.pack(side=tk.LEFT, padx=5)

        # 结果显示框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=15)
        self.result_text.grid(column=0, row=2, columnspan=4, sticky=tk.EW)

        # 设置窗口布局
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def on_paste(self):
        """读取剪切板内容到输入框"""
        clipboard_text = paste_from_clipboard()
        if clipboard_text:
            self.entry_key.delete(0, tk.END)
            self.entry_key.insert(0, clipboard_text)

    def on_clear(self):
        """清空输入框"""
        self.entry_key.delete(0, tk.END)

    def on_fetch(self):
        """调用API并显示结果"""
        key = self.entry_key.get()
        if not key:
            messagebox.showwarning("提示", "要提取的网页链接:")
            return

        result = fetch_data(key)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))
