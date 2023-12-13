
# 对图片进行降噪处理

import cv2

# 读取图片
img = cv2.imread('noisy_turing.png')

# 对图片进行三次高斯滤波处理
result = cv2.GaussianBlur(img, (5, 5), 0)
resul1 = cv2.GaussianBlur(result, (5, 5), 0)
result2 = cv2.GaussianBlur(resul1, (5, 5), 0)

# 对被高斯滤波降噪三次的图片进行三次均值滤波处理
p1 = cv2.blur(result2, (5, 5))
p2 = cv2.blur(p1, (5, 5))
p3 = cv2.blur(p2, (5, 5))

# 对降噪过的图片进行三次双边滤波处理
f1 = cv2.bilateralFilter(p3, 7, 10, 20)
f2 = cv2.bilateralFilter(f1, 7, 10, 20)
f3 = cv2.bilateralFilter(f2, 7, 10, 20)

# 保存降噪后的图片
cv2.imwrite('after_filter_turing.png', f3)

# 展示原图片
cv2.imshow('img', img)

# 展示降噪后的图片
cv2.imshow('final_result', f3)
cv2.waitKey(0)