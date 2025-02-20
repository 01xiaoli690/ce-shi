import cv2
import numpy as np

# 读取图像
image_path = r'D:\py_code\py+OpenCv+OCR\AutoCorrectRecognizeSystem\Results\test_images\image.png'  # 替换为你的图像路径
image = cv2.imread(image_path)

if image is None:
    print("无法加载图像，请检查路径是否正确！")
    exit()

# 显示原始图像
cv2.imshow("Original Image", image)

# 1. 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)

# 2. 二值化处理
# 使用自适应阈值二值化（效果通常比全局阈值更好）
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Binary Image", binary_image)

# 3. 去噪处理
# 使用高斯模糊去除噪声
blurred_image = cv2.GaussianBlur(binary_image, (5, 5), 0)
cv2.imshow("Blurred Image", blurred_image)

# 4. 边缘增强（可选）
# 使用 Canny 算法检测边缘
edges = cv2.Canny(blurred_image, 50, 150)
cv2.imshow("Edges", edges)

# 5. 形态学操作（可选）
# 使用膨胀和腐蚀操作增强文字连通性
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated_image = cv2.dilate(blurred_image, kernel, iterations=1)
cv2.imshow("Dilated Image", dilated_image)

# 等待用户按键并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()