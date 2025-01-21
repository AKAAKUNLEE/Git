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
    content = file_content.get("1.0", tk.END).strip()
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            messagebox.showinfo("成功", f"文件 {file_path} 创建成功")
    except Exception as e:
        messagebox.showerror("错误", f"创建文件失败: {e}")

def select_directory(entry_widget):
    directory = filedialog.askdirectory()
    if directory:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, directory)

# 查看文件列表页面
def list_files():
    directory = directory_entry.get()
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
        menu.add_command(label=ext, command=lambda value=ext: set_extension(value))

# 设置后缀名并更新文件内容
def set_extension(extension):
    extension_var.set(extension)
    update_file_content(extension)

# 更新文件内容
def update_file_content(extension):
    if extension in content_templates:
        file_content.delete("1.0", tk.END)
        file_content.insert(tk.END, content_templates[extension])

# 创建主窗口
root = tk.Tk()
root.title("文件管理器")
root.configure(bg="#f0f0f0")

# 设置窗口大小
root.geometry("600x400")

# 创建 Notebook 组件
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both", padx=10, pady=10)

# 加载自定义扩展名
extensions = load_extensions()

# 初始化内容模板
content_templates = {
    ".txt": "这是默认的文本文件内容。",
    ".py": "print('Hello, World!')",
    ".json": "{\"key\": \"value\"}",
    # 可以根据需要添加更多模板
}

# 创建第一个页面（创建文件）
page1 = ttk.Frame(notebook, padding=10)
notebook.add(page1, text="创建文件")

# 页面1的内容
label = ttk.Label(page1, text="请输入文件路径（不包括扩展名）：", wraplength=110)
label.grid(row=0, column=0, sticky="w")

entry = ttk.Entry(page1, width=20)
entry.grid(row=0, column=1, sticky="w")

select_directory_button = ttk.Button(page1, text="选择目录", width=7, command=lambda: select_directory(entry))
select_directory_button.grid(row=0, column=2, sticky="w")

extension_var = tk.StringVar(page1)
if extensions:
    default_value = extensions[0]
else:
    default_value = "txt"
    extensions.append(default_value)

extension_var.set(default_value)

label1 = ttk.Label(page1, text="请输入文件名：", wraplength=110)
label1.grid(row=1, column=0, sticky="w")

file_entry = ttk.Entry(page1, width=20)
file_entry.grid(row=1, column=1, sticky="w")

# 创建 OptionMenu 并初始化
option_menu = ttk.OptionMenu(page1, extension_var, default_value, *extensions, command=set_extension)
option_menu.grid(row=1, column=2, sticky="w")

create_button = ttk.Button(page1, text="创建文件", width=7, command=create_file)
create_button.grid(row=1, column=3, sticky="w")

# 自定义扩展名部分
custom_extension_label = ttk.Label(page1, text="添加自定义扩展名：", wraplength=110)
custom_extension_label.grid(row=2, column=0, sticky="w")

custom_extension_entry = ttk.Entry(page1, width=20)
custom_extension_entry.grid(row=2, column=1, padx=5, sticky="w")

add_extension_button = ttk.Button(page1, text="添加", width=7, command=add_extension)
add_extension_button.grid(row=2, column=2, padx=5, sticky="w")

# 创建第二个页面（查看文件列表）
page2 = ttk.Frame(notebook, padding=10)
notebook.add(page2, text="快速新建文件夹")

# 页面2的内容
# 自定义新建文件夹部分
create_folder_label = ttk.Label(page2, text="新建文件夹名称：")
create_folder_label.grid(row=1, column=0, sticky="w")

create_folder_entry = ttk.Entry(page2, width=20)
create_folder_entry.grid(row=1, column=1, sticky="w")  # 去掉 padx 参数

create_folder_button = ttk.Button(page2, text="新建文件夹", command=lambda: create_folder(directory_entry, create_folder_entry))
create_folder_button.grid(row=1, column=2, sticky="w")

# 新建文件夹的函数
def create_folder(base_entry, folder_name_entry):
    base_path = base_entry.get()
    folder_name = folder_name_entry.get()
    if not base_path or not folder_name:
        return  # 如果路径或文件夹名称为空，不执行任何操作
    folder_path = os.path.join(base_path, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        messagebox.showinfo("成功", f"文件夹 {folder_path} 已创建")
    except Exception as e:
        messagebox.showerror("错误", f"创建文件夹失败: {e}")

# 创建第三个页面（自定义文件内容）
page3 = ttk.Frame(notebook, padding=10)
notebook.add(page3, text="自定义文件内容")

# 页面3的内容
content_label = ttk.Label(page3, text="请输入文件内容：")
content_label.grid(row=0, column=0, sticky="w")

file_content = tk.Text(page3, width=40, height=10)
file_content.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")

# 初始化文件内容
update_file_content(extension_var.get())

# 更新 OptionMenu 菜单项
update_extension_menu()

# 运行主循环
root.mainloop()