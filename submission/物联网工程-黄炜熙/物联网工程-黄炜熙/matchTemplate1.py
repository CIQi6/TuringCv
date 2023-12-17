import cv2
import numpy as np

def template_matching(image, template):
    # 首先将图像和模板转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 进行模板匹配
    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果中最大值的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 计算模板的宽度和高度
    template_width, template_height = gray_template.shape[::-1]

    # 在原始图像中绘制矩形框标记匹配位置
    top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    return image

# 读取原始图像和模板图像
image = cv2.imread('./original_image.jpg')
template = cv2.imread('./template_image.jpg')

# 进行模板匹配
matched_image = template_matching(image, template)


# 显示结果图像
cv2.imshow('Template Matching', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
