import cv2
import matplotlib.pyplot as plt #（导入模块）
image_path = 'pic.jpg'
original_image = cv2.imread(image_path)#（读取图像）
image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)#（将图像从 BGR 转换为 RGB）
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')#（显示没处理的图像）
denoised_image = cv2.medianBlur(original_image, 5)#（用中值滤波进行降噪）
denoised_image_rgb = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB)#（将降噪后的图像从bgr转换为rgb）
plt.subplot(1, 2, 2)
plt.imshow(denoised_image_rgb)
plt.title('makeImage')
plt.axis('off')
cv2.imwrite('filter_turing.png', denoised_image_rgb)#(保存降噪后的图像)
plt.show()#（显示降噪后的图像）
