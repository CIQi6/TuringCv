# affine Trans仿射变换



`import cv2` 
`from matplotlib import pyplot as plt`
`import numpy as np`

`turing=cv2.imread("D://noisy_turing.png")`
`gray=cv2.imread("D://noisy_turing.png",cv2.IMREAD_GRAYSCALE)`

`def cv_show(img):`
    `cv2.imshow("1",img)`
    `cv2.waitKey(0)`
    `cv2.destroyAllWindows()`

### 使用导向滤波进行图片降噪

`guide=cv2.imread("D://turing_true.jpg")`
guide=cv2.resize(guide,(640, 640),interpolation=cv2.INTER_LINEAR)<!--调整引导图象大小与目标图片一致-->
turing=cv2.medianBlur(turing,3) <!--对原图进行中值滤波-->
Filter=cv2.ximgproc.createGuidedFilter(guide=guide,radius=15,eps=200)<!--radius滤波器半径与eps滤波器精度越大，图像越平滑越好，-->

result=Filter.filter(turing)<!--对目标图像应用导向滤波器-->
`cv_show(turing)`
`cv_show(result)`

## 进行仿射变换



`rows,cols,channels=result.shape`

Rotating = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)<!--向左旋转90°-->
`res1 = cv2.warpAffine(result, Rotating, (cols, rows))`
`cv_show(res1)`
Shifting = np.float32([[1, 0, 200], [0, 1, 100]])<!--x方向平移200 y方向平移100-->
`res2 = cv2.warpAffine(result, Shifting, (cols, rows))`      

`cv_show(res2)`

`pts1 = np.float32([[0, 0], [cols , 0], [0, rows]])`
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.1], [cols * 0.2, rows * 0.8]])<!--更改参数任意变换-->

`Any = cv2.getAffineTransform(pts1, pts2)`
`res3 = cv2.warpAffine(result, Any, (cols, rows))`
`cv_show(res3)`

# match Template模板匹配

`import cv2` 
`from matplotlib import pyplot as plt`
`import numpy as np`

## 使用pvz中的游戏截图完成模板匹配

`target=cv2.imread("D://zombies.png")`
`template=cv2.imread("D://head.png")`
`def cv_show(img):`
    `cv2.imshow("1",img)`
    `cv2.waitKey(0)`
    `cv2.destroyAllWindows()`
`theight, twidth = template.shape[:2]`

## 使用标准相关匹配 值越接近1匹配效果越好

`result = cv2.matchTemplate(target,template,cv2.TM_CCORR_NORMED)`

`index=np.where(result>0.94)`
`draw=target.copy()`
`for i in zip(*index[::-1]):
    result=cv2.rectangle(draw,i,(i[0]+twidth, i[1]+theight*2), (0, 0, 255), 1)`
`cv_show(target)`
`cv_show(result)`