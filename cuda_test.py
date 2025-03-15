import torch
import torch
print("PyTorch 版本:", torch.__version__)
print("CUDA 是否可用:", torch.cuda.is_available())
print("当前设备:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "无")

# print("Is CUDA available:", torch.cuda.is_available())
# print("GPU Device Name:", torch.cuda.get_device_name(0))