import cv2
import numpy as np

def affine_transform(image):
    # 噪声消除，可使用高斯模糊或中值滤波
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    # 进行仿射变换
    rows, cols, _ = image.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    transformed = cv2.warpAffine(blurred, M, (cols, rows))

    return transformed

# 读取原始图像和模板图像
image = cv2.imread('Tuing_image.jpg')

# 进行模板匹配
matched_image = template_matching(image, template)

# 进行仿射变换
transformed_image = affine_transform(image)

# 显示结果图像
cv2.imshow('Template Matching', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
