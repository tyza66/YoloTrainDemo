# 模型训练
from ultralytics import YOLO
import os
os.environ['NO_ALBUMENTATIONS_UPDATE'] = '1'

if __name__ == '__main__':
    # 1. 初始化模型 这个不一定好用 但是小 演示快
    model = YOLO("yolo11n.pt")
    # 2. 模型训练 数据集配置文件 训练轮数 输入图像大小
    model.train(data='./train_config.yaml', epochs=100,imgsz=640)