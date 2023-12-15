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
cv2.imwrite('ASL_img.png', ASL_img)