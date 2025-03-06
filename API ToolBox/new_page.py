import tkinter as tk
from tkinter import ttk  # 显式导入 ttk 模块
from tkinter import messagebox
from api_handler import parse_watermark


class NewPage(tk.ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        """创建新页面控件"""
        # AppID 输入框和标签
        label_appid = tk.ttk.Label(self, text="AppID:")
        label_appid.grid(column=0, row=0, sticky=tk.W)

        self.entry_appid = tk.ttk.Entry(self, width=40)
        self.entry_appid.grid(column=1, row=0, sticky=tk.EW)

        # 视频链接输入框和标签
        label_link = tk.ttk.Label(self, text="视频链接:")
        label_link.grid(column=0, row=1, sticky=tk.W)

        self.entry_link = tk.ttk.Entry(self, width=40)
        self.entry_link.grid(column=1, row=1, sticky=tk.EW)

        # 解析按钮
        button_parse = tk.ttk.Button(self, text="解析视频", command=self.on_parse)
        button_parse.grid(column=0, row=2, columnspan=2, pady=10)

        # 结果显示框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=15)
        self.result_text.grid(column=0, row=3, columnspan=2, sticky=tk.EW)

        # 设置窗口布局
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)

    def on_parse(self):
        """调用API解析视频"""
        appid = self.entry_appid.get()
        link = self.entry_link.get()

        if not appid or not link:
            messagebox.showwarning("提示", "请输入AppID和视频链接！")
            return

        result = parse_watermark(appid, link)
        self.result_text.delete(1.0, tk.END)  # 清空文本框
        self.result_text.insert(tk.END, str(result))  # 显示解析结果
