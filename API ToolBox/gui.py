import tkinter as tk
from tkinter import ttk, messagebox
from api_handler import fetch_data
from clipboard_handler import paste_from_clipboard


class APIToolboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("API工具箱")
        self.root.geometry("500x400")

        # 设置主题 (需要安装 ttkthemes)
        try:
            from ttkthemes import ThemedTk

            self.root = ThemedTk(theme="arc")  # 使用 'arc' 主题，可以根据需要更换
            self.root.title("API工具箱 (支持主题)")
            self.root.geometry("500x400")
        except ImportError:
            print("ttkthemes 未安装，使用默认主题")

        # 创建多页面的Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # 第一页：API工具箱
        self.page_api = ttk.Frame(self.notebook)
        self.notebook.add(self.page_api, text="API工具箱")
        self.create_api_toolbox_page(self.page_api)

        # 第二页：新页面（内容待定）
        self.page_new = ttk.Frame(self.notebook)
        self.notebook.add(self.page_new, text="新页面")
        self.create_new_page(self.page_new)

    def create_api_toolbox_page(self, parent):
        """创建API工具箱页面"""
        frame = ttk.Frame(parent, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # 输入框和标签
        label_key = ttk.Label(frame, text="要提取的网页链接:")
        label_key.grid(column=0, row=0, sticky=tk.W)

        self.entry_key = ttk.Entry(frame, width=40)
        self.entry_key.grid(column=1, row=0, sticky=tk.EW)

        # 按钮在同一行
        button_frame = ttk.Frame(frame)
        button_frame.grid(column=0, row=1, columnspan=4, pady=10)

        button_paste = ttk.Button(button_frame, text="读取剪切板", command=self.on_paste)
        button_paste.pack(side=tk.LEFT, padx=5)

        button_clear = ttk.Button(button_frame, text="清空输入", command=self.on_clear)
        button_clear.pack(side=tk.LEFT, padx=5)

        button_fetch = ttk.Button(button_frame, text="获取数据", command=self.on_fetch)
        button_fetch.pack(side=tk.LEFT, padx=5)

        # 结果显示框
        self.result_text = tk.Text(frame, wrap=tk.WORD, height=15)
        self.result_text.grid(column=0, row=2, columnspan=4, sticky=tk.EW)

        # 设置窗口布局
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

    def create_new_page(self, parent):
        """创建新页面（内容待定）"""
        frame = ttk.Frame(parent, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(frame, text="这里是新页面，内容待定")
        label.pack(pady=20)

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
