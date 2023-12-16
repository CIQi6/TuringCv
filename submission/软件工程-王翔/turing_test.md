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
cv2.imshow('up_down', new1)

# 展示左右翻转后的图片
cv2.imshow('left_right', new2)
cv2.waitKey(0)

# 保存翻转后图片
cv2.imwrite('up_down_flip.png', new1)
cv2.imwrite('left_right_flip.png', new2)
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




# 模板匹配

## 相关代码如下

```python
import cv2

# 读取输入图像，并将其灰度化
ASL_img = cv2.imread("ASL.png")
ASL_gray_img = cv2.cvtColor(ASL_img, cv2.COLOR_BGR2GRAY)

# 读取模板图像，并将其灰度化
temple = cv2.imread("temple.png", 0)

# 获取结果        使用TM_SQDIFF匹配方法，结果越小，匹配度越高
result = cv2.matchTemplate(ASL_gray_img, temple, 0)
# print(result)

# 解析结果
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
print(minVal)
print(maxVal)
print(minLoc)
print(maxLoc)

# 获取矩形顶点
h, w = temple.shape

# 在彩色的原图中绘制结果
cv2.rectangle(ASL_img, minLoc, (minLoc[0]+w, minLoc[1]+h), (0, 0, 255), 3)

# 展示绘制结果和模板图像
cv2.imshow('ASL_img', ASL_img)
cv2.imshow('temple', temple)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
cv2.imwrite('ASL_img.png', ASL_im
```
