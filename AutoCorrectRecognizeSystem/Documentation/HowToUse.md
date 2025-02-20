# 前期准备

Pycharm中下载OpenCv库

pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

下载PyQt5库

 pip install PyQt5

下载Tesseract库

下载地址：[首页 ·UB-曼海姆/tesseract 维基](https://github.com/UB-Mannheim/tesseract/wiki)

安装python接口:pip install pytesseract



# 代码目录结构

CharacterRecognitionSoftware/
│
├── Code/
│   ├── main.py          # 主程序入口
│   ├── preprocess.py    # 图像预处理代码
│   ├── ui/              # PyQt5界面代码
│   │   ├── main_window.py
│   │   └── ...
│   └── ocr/            # OCR相关代码
│       ├── ocr_engine.py
│       └── ...
│
├── Documentation/
│   ├── CodeStructure.md # 代码结构文档
│   ├── Installation.md  # 安装环境文档
│   ├── HowToUse.md      # 操作步骤文档
│   └── KeyTechnologies.md # 关键技术文档
│
├── Schedule.md          # 进度表文档
│
└── Results/             # 实验结果文件夹
    ├── test_images/
    │   └── ...
    └── recognition_results/
        └── ...