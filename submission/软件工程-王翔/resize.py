
# 对图片进行缩放操作

import cv2

# 读取降噪后的图片
img = cv2.imread('after_filter_turing.png')

# 对图片进行缩放
resize_img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 展示原图
cv2.imshow('img', img)

# 展示缩放后的图
cv2.imshow('resize_img', resize_img)
cv2.waitKey(0)

# 保存缩放后的图
cv2.imwrite('resize_img.png', resize_img)