'''import cv2

# 读取彩色图像
image = cv2.imread('icon_star_s.png')

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 分离通道
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# 显示原始图像和通道分离后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

# 等待按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
import cv2
import os


# 定义函数，用于保存图像
def save_image(image, path):
    cv2.imwrite(path, image)


# 读取图像
image = cv2.imread('icon_star_s.png')
# 分离三个通道
b, g, r = cv2.split(image)
# 创建保存路径
if not os.path.exists('output'):
    os.makedirs('output')
# 保存三个通道到文件夹
save_image(b, 'output/blue.png')
save_image(g, 'output/green.png')
save_image(r, 'output/red.png')
