import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import cv2  # 修改这里
import os
import concurrent.futures

def auto_crop_image(input_path, output_path):
    # 读取输入图片
    original_image = cv2.imread(input_path)
    if original_image is None:
        raise ValueError("无法读取输入图片")

    # 转换为灰度图像
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # 应用高斯模糊
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 边缘检测
    edges = cv2.Canny(blurred_image, 50, 150)

    # 查找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的轮廓
    largest_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    if largest_contour is None:
        raise ValueError("未找到有效的边缘轮廓")

    # 获取最小外接矩形
    bounding_rect = cv2.boundingRect(largest_contour)

    # 裁剪图片
    cropped_image = original_image[bounding_rect[1]:bounding_rect[1] + bounding_rect[3],
                                    bounding_rect[0]:bounding_rect[0] + bounding_rect[2]]

    # 保存裁剪后的图片
    cv2.imwrite(output_path, cropped_image)

def select_input_folder():
    input_folder = filedialog.askdirectory()
    if input_folder:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

def process_images():
    input_folder = input_entry.get()
    output_folder = output_entry.get()

    if not input_folder or not output_folder:
        messagebox.showerror("错误", "请选择输入和输出文件夹路径")
        return

    # 获取输入文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    if not image_files:
        messagebox.showerror("错误", "输入文件夹中没有图片文件")
        return

    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 多线程处理图片
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for image_file in image_files:
            input_path = os.path.join(input_folder, image_file)
            output_path = os.path.join(output_folder, image_file)
            futures.append(executor.submit(auto_crop_image, input_path, output_path))

        # 等待所有任务完成
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                messagebox.showerror("错误", f"处理图片时发生错误: {e}")

    messagebox.showinfo("成功", "图片裁剪成功！")

# 创建主窗口
root = tk.Tk()
root.title("自动裁剪图片")

# 创建输入文件夹选择框
input_label = tk.Label(root, text="输入文件夹路径:")
input_label.grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
input_button = tk.Button(root, text="选择", command=select_input_folder)
input_button.grid(row=0, column=2, padx=10, pady=5)

# 创建输出文件夹选择框
output_label = tk.Label(root, text="输出文件夹路径:")
output_label.grid(row=1, column=0, padx=10, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)
output_button = tk.Button(root, text="选择", command=select_output_folder)
output_button.grid(row=1, column=2, padx=10, pady=5)

# 创建处理按钮
process_button = tk.Button(root, text="批量裁剪图片", command=process_images)
process_button.grid(row=2, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()