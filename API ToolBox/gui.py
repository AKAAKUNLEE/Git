import tkinter as tk
from api_page import APIPage
from new_page import NewPage


class APIToolboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("提取网页链接")
        self.root.geometry("500x400")

        # 设置主题 (需要安装 ttkthemes)
        try:
            from ttkthemes import ThemedTk

            self.root = ThemedTk(theme="arc")  # 使用 'arc' 主题，可以根据需要更换
            self.root.title("提取网页链接 (支持主题)")
            self.root.geometry("500x400")
        except ImportError:
            print("ttkthemes 未安装，使用默认主题")

        # 创建多页面的Notebook
        self.notebook = tk.ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # 第一页：提取网页链接
        self.api_page = APIPage(self.notebook)
        self.notebook.add(self.api_page, text="提取网页链接")

        # 第二页：新页面（内容待定）
        self.new_page = NewPage(self.notebook)
        self.notebook.add(self.new_page, text="新页面")
