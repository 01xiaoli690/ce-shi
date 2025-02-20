import os
import pytesseract
import cv2

# 设置 TESSDATA_PREFIX 环境变量
os.environ['TESSDATA_PREFIX'] = r'D:\Tesseract\tessdata\tessdata-main'

# 指定 Tesseract 的可执行文件路径
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\bin\tesseract.exe'

# 使用 OpenCV 读取图像
image_path = r'D:\py_code\py+OpenCv+OCR\AutoCorrectRecognizeSystem\Results\test_images\image.png'
image = cv2.imread(image_path)

if image is None:
    print("无法加载图像，请检查路径是否正确！")
    exit()

# 将图像从 BGR 转换为 RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 指定语言为中文（简体中文：chi_sim）
text = pytesseract.image_to_string(image, lang='chi_sim')

# 打印识别结果
print("识别结果：")
print(text)

# 显示图像
cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()