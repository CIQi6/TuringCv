
# 对图像进行翻转操作

import cv2

# 读取降噪后的turing图片
img = cv2.imread('after_filter_turing.png')

# 对图像进行上下翻转
new1 = cv2.flip(img, 0)

# 对图像进行左右翻转
new2 = cv2.flip(img, 1)

# 展示原图片
cv2.imshow('img', img)

# 展示上下翻转后的图片
cv2.imshow('up_down', new1)

# 展示左右翻转后的图片
cv2.imshow('left_right', new2)
cv2.waitKey(0)

# 保存翻转后图片
cv2.imwrite('up_down_flip.png', new1)
cv2.imwrite('left_right_flip.png', new2)