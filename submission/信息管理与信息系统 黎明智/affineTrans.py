
import cv2 
from matplotlib import pyplot as plt
import numpy as np

turing=cv2.imread("./noisy_turing.png")
gray=cv2.imread("./noisy_turing.png",cv2.IMREAD_GRAYSCALE)

def cv_show(img):
    cv2.imshow("1",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
turing.shape
guide=cv2.imread("./turing_true.jpg")
guide=cv2.resize(guide,(640, 640),interpolation=cv2.INTER_LINEAR)
turing=cv2.medianBlur(turing,3) 
Filter=cv2.ximgproc.createGuidedFilter(guide=guide,radius=15,eps=200)

result=Filter.filter(turing)
cv_show(turing)
cv_show(result)

rows,cols,channels=result.shape

Rotating = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
res1 = cv2.warpAffine(result, Rotating, (cols, rows))
cv_show(res1)
Shifting = np.float32([[1, 0, 200], [0, 1, 100]])
res2 = cv2.warpAffine(result, Shifting, (cols, rows))      
 
cv_show(res2)


pts1 = np.float32([[0, 0], [cols , 0], [0, rows]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.1], [cols * 0.2, rows * 0.8]])
 
Any = cv2.getAffineTransform(pts1, pts2)
res3 = cv2.warpAffine(result, Any, (cols, rows))
cv_show(res3)