from tkinter import ttk


class NewPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        """创建新页面控件"""
        label = ttk.Label(self, text="这里是新页面，内容待定")
        label.pack(pady=20)
