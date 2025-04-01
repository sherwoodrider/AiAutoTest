# import torch
# import time
import torch_directml

# 方法1：检查计算设备
print(torch_directml.is_available())  # 应返回True

# # 方法2：基准测试
# with torch.no_grad():
#     start = time.time()
#     _ = model(torch.randn(1,3,224,224).to(device))
#     print(f"推理耗时: {time.time()-start:.3f}s")