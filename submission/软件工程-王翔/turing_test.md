# 对图像进行降噪处理

## 相关代码如下

```python
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
```



# 对图片进行平移处理

## 相关代码如下

```python
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
pingyi_up_img = cv2.warpAffine(img, M_up, (w, h))
pingyi_right_img = cv2.warpAffine(img, M_right, (w, h))

# 展示原图片
cv2.imshow('img', img)

# 展示平移后的图片
cv2.imshow('pingyi_up_img', pingyi_up_img)
cv2.imshow('pingyi_right_img', pingyi_right_img)

cv2.waitKey(0)

# 保存平移后的图片
cv2.imwrite('pingyi.up_img.png', pingyi_up_img)
cv2.imwrite('pingyi_right_img.png', pingyi_right_img)
```



# 对图像进行翻转处理

## 相关代码如下

```python
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
cv2.imshow('shangxia', new1)

# 展示左右翻转后的图片
cv2.imshow('zuoyou', new2)
cv2.waitKey(0)

# 保存翻转后图片
cv2.imwrite('shangxia_flip.png', new1)
cv2.imwrite('zuoyou_flip.png', new2)
```



# 对图像进行缩放处理

## 相关代码如下

```python
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
```

