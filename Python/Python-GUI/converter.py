import tkinter as tk
from tkinter import messagebox
from opencc import OpenCC

# 初始化转换器
cc = OpenCC('t2s')  # 繁体到简体

# 创建主窗口
root = tk.Tk()
root.title("繁体中文转简体中文")

# 创建输入框
input_label = tk.Label(root, text="输入繁体中文:")
input_label.pack()

input_text = tk.Entry(root, width=50)
input_text.pack()

# 创建输出框
output_label = tk.Label(root, text="转换后的简体中文:")
output_label.pack()

output_text = tk.Entry(root, width=50, state='readonly')
output_text.pack()

# 转换函数
def convert_text():
    try:
        traditional_text = input_text.get()
        simplified_text = cc.convert(traditional_text)
        output_text.config(state='normal')
        output_text.delete(0, tk.END)
        output_text.insert(0, simplified_text)
        output_text.config(state='readonly')
    except Exception as e:
        messagebox.showerror("错误", str(e))

# 创建转换按钮
convert_button = tk.Button(root, text="转换", command=convert_text)
convert_button.pack()

# 运行主循环
root.mainloop()