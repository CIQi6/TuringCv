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

def linear_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched_image#（采用图像拉伸函数）
plt.subplot(1,1, 1)
plt.imshow(stretched_image, cmap='gray')
plt.title('Stretched Image')
plt.axis('off')
plt.savefig('Stretched Image')#（保存对比图像）
plt.show()

tx, ty = 50, 30 
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])#（平移矩阵）

translated_image = cv2.warpAffine(original_image, translation_matrix, (original_image.shape[1], original_image.shape[0]))#（应用平移变化）

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
plt.title('Translated Image')#(平移后)
plt.axis('off')
plt.savefig('Translated Image')
plt.show()   #（显示原始与平移后的图像）

flipped_image_horizontal = cv2.flip(original_image, 1)  # （水平翻转）
flipped_image_vertical = cv2.flip(original_image, 0)    # （垂直翻转）
flipped_image_both = cv2.flip(original_image, -1)       # （水平和垂直翻转）
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(flipped_image_horizontal, cv2.COLOR_BGR2RGB))
plt.title('Flipped Horizontal')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(flipped_image_vertical, cv2.COLOR_BGR2RGB))
plt.title('Flipped Vertical')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(flipped_image_both, cv2.COLOR_BGR2RGB))
plt.title('Flipped Both')
plt.axis('off')
plt.savefig('Overturn')#（保存对比图像）
plt.show()


target_size = (original_image.shape[1] //2, original_image.shape[0] //1)# （定义目标大小，这里将图像缩小为原来的一半）

resized_image = cv2.resize(original_image, target_size, interpolation=cv2.INTER_LINEAR)# （缩放图像）

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')
plt.axis('off')
plt.savefig('Resized Image')#（保存对比图像）
plt.show()# （显示原始图像和缩放后的图像）


