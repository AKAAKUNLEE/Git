import cv2 as cv
import numpy as np
import os
import pyperclip

class HsvSelector(object):

    def __init__(self, input_source, cap_index=None, img_path=None, video_path=None):
        """
        input_source: 0 代表摄像头，1代表图片, 2代表视频
        """
        self.input_source = input_source
        self.display_type = "img" if input_source == 1 else "video"

        if input_source == 0:
            assert cap_index is not None, "请指定摄像头标号"
            self.cap = cv.VideoCapture(cap_index)
            assert self.cap.isOpened(), "摄像头未打开"

        elif input_source == 1:
            assert img_path is not None, "请指定图片路径"
            assert os.path.exists(img_path), f"{img_path}路径下没有图片"
            self.image = cv.imread(img_path)

        elif input_source == 2:
            assert video_path is not None, "请指定视频路径"
            assert os.path.exists(video_path), f"{video_path}路径下没有视频"
            self.cap = cv.VideoCapture(video_path)
            assert self.cap.isOpened(), "视频文件未成功加载"

        else:
            raise ValueError("不支持此输入类型")

    def nothing(self, x):
        pass