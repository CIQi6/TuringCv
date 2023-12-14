import cv2 
from matplotlib import pyplot as plt
import numpy as np

target=cv2.imread("D://zombies.png")
template=cv2.imread("D://head.png")
def cv_show(img):
    cv2.imshow("1",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
theight, twidth = template.shape[:2]
result = cv2.matchTemplate(target,template,cv2.TM_CCORR_NORMED)

index=np.where(result>0.94)
draw=target.copy()
for i in zip(*index[::-1]):
    result=cv2.rectangle(draw,i,(i[0]+twidth, i[1]+theight*2), (0, 0, 255), 1)
cv_show(target)
cv_show(result)
