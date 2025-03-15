import os
import random
import shutil

# 数据集路径，类别文件夹位于此目录下
dataset_path = "D:\\Workspace\\Projects\\tyza66\YoloTrainDemo\\datasets\\animals_origin"  # 修改为数据集的路径，例如 "dataset/"
categories = ["buffalo", "elephant", "rhino", "zebra"]

# 输出路径
output_path = "D:\\Workspace\\Projects\\tyza66\YoloTrainDemo\\datasets\\animal"  # 修改为划分后的输出路径
train_path = os.path.join(output_path, "train")
val_path = os.path.join(output_path, "valit")
test_path = os.path.join(output_path, "test")

# 数据划分比例
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 创建输出目录
for split_path in [train_path, val_path, test_path]:
    os.makedirs(os.path.join(split_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(split_path, "labels"), exist_ok=True)

# 收集文件，并为每个类别生成唯一文件名
all_files = []
for category_index, category in enumerate(categories):
    image_folder = os.path.join(dataset_path, category, "images")
    label_folder = os.path.join(dataset_path, category, "labels")
    for image_file in os.listdir(image_folder):
        if image_file.endswith(".jpg"):
            label_file = image_file.replace(".jpg", ".txt")
            all_files.append({
                "image": os.path.join(image_folder, image_file),
                "label": os.path.join(label_folder, label_file),
                "category": category_index  # 添加类别索引
            })

# 打乱数据集
random.shuffle(all_files)

# 按比例划分
num_total = len(all_files)
num_train = int(num_total * train_ratio)
num_val = int(num_total * val_ratio)

train_files = all_files[:num_train]
val_files = all_files[num_train:num_train + num_val]
test_files = all_files[num_train + num_val:]


# 定义函数，用于将文件重命名并移动
def move_files(file_list, split_path):
    for idx, file_pair in enumerate(file_list):
        # 生成唯一的文件名，例如 "buffalo_001.jpg"
        image_name = f"{file_pair['category']}_{idx:04d}.jpg"
        label_name = f"{file_pair['category']}_{idx:04d}.txt"

        # 移动图片
        shutil.copy(file_pair["image"], os.path.join(split_path, "images", image_name))
        # 移动标签
        shutil.copy(file_pair["label"], os.path.join(split_path, "labels", label_name))


# 执行移动并生成文件名
move_files(train_files, train_path)
move_files(val_files, val_path)
move_files(test_files, test_path)

print("数据集已成功整理并划分为训练集、验证集和测试集！")
