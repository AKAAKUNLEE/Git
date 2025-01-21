import tkinter as tk
from tkinter import messagebox
import re
import pyperclip

def check_link_and_extract_code():
    input_text = text_entry.get("1.0", tk.END).strip()
    link_pattern = r"https?://pan\.baidu\.com/s/[a-zA-Z0-9]+"
    code_pattern = r"提取码:\s*([a-zA-Z0-9]+)"

    link_match = re.search(link_pattern, input_text)
    code_match = re.search(code_pattern, input_text)

    if link_match and code_match:
        link = link_match.group(0)
        code = code_match.group(1)
        complete_link = f"{link}?pwd={code}"
        result_label.config(text="这是百度网盘链接")
        pyperclip.copy(complete_link)
        messagebox.showinfo("提示", "完整链接已复制到剪切板")
    elif link_match:
        link = link_match.group(0)
        result_label.config(text="这是百度网盘链接，但未找到提取码")
        pyperclip.copy(link)
        messagebox.showinfo("提示", "仅复制了链接")
    else:
        result_label.config(text="这不是百度网盘链接")
        messagebox.showwarning("提示", "未找到有效的百度网盘链接")

# 创建主窗口
root = tk.Tk()
root.title("百度网盘链接检查器")

# 创建和放置控件
text_label = tk.Label(root, text="输入文本:")
text_label.grid(row=0, column=0, padx=10, pady=10)

text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

check_button = tk.Button(root, text="检查链接并合并提取码", command=check_link_and_extract_code)
check_button.grid(row=2, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# 运行主循环
root.mainloop()