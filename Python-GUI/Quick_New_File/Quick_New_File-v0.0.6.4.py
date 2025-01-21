import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os
import json

# 保存和加载自定义扩展名的文件路径
EXTENSIONS_FILE = 'custom_extensions.json'

# 加载自定义扩展名
def load_extensions():
    if os.path.exists(EXTENSIONS_FILE):
        with open(EXTENSIONS_FILE, 'r') as file:
            return json.load(file)
    return []

# 保存自定义扩展名
def save_extensions(extensions):
    with open(EXTENSIONS_FILE, 'w') as file:
        json.dump(extensions, file)

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

# 添加自定义扩展名
def add_extension():
    new_extension = custom_extension_entry.get().strip()
    if new_extension and not new_extension.startswith('.'):
        new_extension = '.' + new_extension
    if new_extension and new_extension not in extensions:
        extensions.append(new_extension)
        extension_var.set(new_extension)
        update_extension_menu()
        save_extensions(extensions)

def update_extension_menu():
    menu = option_menu['menu']
    menu.delete(0, 'end')
    for ext in extensions:
        menu.add_command(label=ext, command=lambda value=ext: extension_var.set(value))

# 创建主窗口
root = tk.Tk()
root.title("文件管理器")

# 设置窗口大小
root.geometry("600x400")

# 加载自定义扩展名
extensions = load_extensions()

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

extension_var = tk.StringVar(page1)
if extensions:
    default_value = extensions[0]
else:
    default_value = "txt"
    extensions.append(default_value)

extension_var.set(default_value)

# 创建 OptionMenu 并初始化
option_menu = tk.OptionMenu(page1, extension_var, default_value, *extensions)
option_menu.pack(pady=10)

create_button = tk.Button(page1, text="创建文件", command=create_file)
create_button.pack(pady=10)

# 自定义扩展名部分
custom_extension_label = tk.Label(page1, text="添加自定义扩展名：")
custom_extension_label.pack(pady=5)

custom_extension_entry = tk.Entry(page1, width=20)
custom_extension_entry.pack(side=tk.LEFT, padx=5)

add_extension_button = tk.Button(page1, text="添加", command=add_extension)
add_extension_button.pack(side=tk.LEFT, padx=5)

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

# 更新 OptionMenu 菜单项
update_extension_menu()

# 运行主循环
root.mainloop()