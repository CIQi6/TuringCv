
# 对图像进行平移操作

import cv2
import numpy as np

# 读取降噪后的turing图片
img = cv2.imread('after_filter_turing.png')

# 高, 宽, 通道数
h, w, ch = img.shape

# 变换矩阵      向上平移
M_up = np.float32([[1, 0, 0], [0, 1, -100]])

# 变换矩阵      向右平移
M_right = np.float32([[1, 0, 100], [0, 1, 0]])

# 平移图片
translation_up_img = cv2.warpAffine(img, M_up, (w, h))
translation_right_img = cv2.warpAffine(img, M_right, (w, h))

# 展示原图片
cv2.imshow('img', img)

# 展示平移后的图片
cv2.imshow('translation_up_img', translation_up_img)
cv2.imshow('translation_right_img', translation_right_img)

cv2.waitKey(0)

# 保存平移后的图片
cv2.imwrite('translation_up_img.png', translation_up_img)
cv2.imwrite('translation_right_img.png', translation_right_img)