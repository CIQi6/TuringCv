
import cv2 
from matplotlib import pyplot as plt
import numpy as np

turing=cv2.imread("D://noisy_turing.png")
gray=cv2.imread("D://noisy_turing.png",cv2.IMREAD_GRAYSCALE)
cat=cv2.imread("D://cat.jpg")
dog=cv2.imread("D://dog.jpg")
def cv_show(img):
    cv2.imshow("1",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
turing.shape#获取目标图片大小
guide=cv2.imread("D://turing_true.jpg")#使用从图灵微信公众号翻出来的logo作为引导图像guide
guide=cv2.resize(guide,(640, 640),interpolation=cv2.INTER_LINEAR)#调整引导图象大小与目标图片一致
turing=cv2.medianBlur(turing,3) #对原图进行中值滤波
Filter=cv2.ximgproc.createGuidedFilter(guide=guide,radius=15,eps=200)#radius滤波器大小与eps滤波器精度越大，图像越平滑越好，

result=Filter.filter(turing)#对目标图像应用导向滤波器
cv_show(turing)
cv_show(result)

rows,cols,channels=result.shape

Rotating = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)#向左旋转90°
res1 = cv2.warpAffine(result, Rotating, (cols, rows))
cv_show(res1)
Shifting = np.float32([[1, 0, 200], [0, 1, 100]])#x方向平移200 y方向平移100
res2 = cv2.warpAffine(result, Shifting, (cols, rows))      
 
cv_show(res2)


pts1 = np.float32([[0, 0], [cols , 0], [0, rows]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.1], [cols * 0.2, rows * 0.8]])#更改参数任意变换
 
Any = cv2.getAffineTransform(pts1, pts2)
res3 = cv2.warpAffine(result, Any, (cols, rows))
cv_show(res3)