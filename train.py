from ultralytics import YOLO
import os
import torch

# 设置不更新 albumentations
os.environ['NO_ALBUMENTATIONS_UPDATE'] = '1'

if __name__ == '__main__':
    # 检测 CUDA 设备
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 加载 YOLO 模型
    model = YOLO("yolo11n.pt")
    model.to("cuda")  # 将模型加载到 GPU

    # 模型训练
    model.train(
        data='train_config.yaml',  # 数据集配置文件
        epochs=100,  # 训练轮数
        imgsz=640#,  # 输入图像大小
        # batch=16,  # 批量大小
        # project='YOLOv11n_Project',  # 项目目录
        # name='exp1',  # 实验名
        # exist_ok=True,  # 如果目录存在，覆盖
        # half=True  # 启用混合精度训练
    )

    # # 评估模型
    # metrics = model.val()  # 验证集评估
    # print("验证结果:", metrics)
    #
    # # 模型推理
    # model.predict(source='./test_images', save=True)  # 预测测试图片并保存结果
