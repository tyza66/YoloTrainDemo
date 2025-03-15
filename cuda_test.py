import torch
print("Is CUDA available:", torch.cuda.is_available())
print("GPU Device Name:", torch.cuda.get_device_name(0))