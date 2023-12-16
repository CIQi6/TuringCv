import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('fan.jpg',0)
template = cv2.imread('head.jpg',0)
w, h = template.shape[::-1]
method = eval(meth)
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)#(计算值越小越相关)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, 255, 2)#(画矩形)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])#(隐藏坐标)
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])#(隐藏坐标)
plt.show()
