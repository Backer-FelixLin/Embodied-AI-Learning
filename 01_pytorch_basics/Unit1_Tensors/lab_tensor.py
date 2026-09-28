"""
题目 1：要求创建下面几种 Unit1_Tensors，并打印它们的 shape、dtype、device：
1. 从 Python list 创建一个 2x3 Unit1_Tensors
2. 创建全 0 Unit1_Tensors，形状是 (2, 4)
3. 创建全 1 Unit1_Tensors，形状是 (3, 2)
4. 创建 0 到 11 的一维 Unit1_Tensors，然后 reshape 成 (3, 4)
5. 创建一个随机正态分布 Unit1_Tensors，形状是 (2, 3)
"""

import torch

# 1. 从 Python list 创建一个 2x3 Unit1_Tensors
tensor1 = torch.tensor([[1, 2, 3],[4, 5, 6]])
print(tensor1)

# 2. 创建全 0 Unit1_Tensors，形状是 (2, 4)
tensor2 = torch.zeros(2, 4)
print(tensor2)

# 3. 创建全 1 Unit1_Tensors，形状是 (3, 2)
tensor3 = torch.ones(3, 2)
print(tensor3)

# 4. 创建 0 到 11 的一维 Unit1_Tensors，然后 reshape 成 (3, 4)
tensor4 = torch.arange(12)
print(tensor4)
tensor5 = torch.reshape(tensor4, [3, 4])
print(tensor5)

# 5. 创建一个随机正态分布 Unit1_Tensors，形状是 (2, 3)
tensor6 = torch.randn(2, 3)
print(tensor6)

"""
题目 2：索引和切片
用下面这个 Unit1_Tensors：
x = torch.arange(12).reshape(3, 4)
完成：
1. 取第一行
2. 取第二列
3. 取左上角 2x2 子矩阵
4. 把最后一列全部改成 100
"""

x = torch.arange(12).reshape(3, 4)
print(x)

# 1. 取第一行
first_raw = x[0]
print(first_raw)

# 2. 取第二列
second_raw = x[:, 1]
print(second_raw)

# 3. 取左上角 2x2 子矩阵
child_matrix = x[:2, :2]
print(child_matrix)
# 取右上角 2x2 子矩阵
child_matrix2 = x[:2, 2:]
print(child_matrix2)

# 4. 把最后一列全部改成 100
x[:, -1:] = 100
print(x)

"""
题目 3：reshape、view、transpose
创建：
x = torch.arange(12)
完成：
1. reshape 成 (3, 4)
2. 再 transpose 成 (4, 3)
3. 打印 transpose 前后的 shape
4. 尝试把 transpose 后的 Unit1_Tensors 用 .reshape(12) 拉平
"""

x = torch.arange(12)

# 1. reshape 成 (3, 4)
x = torch.reshape(x, [3, 4])
print(x)
print(x.shape)

# 2. 再 transpose 成 (4, 3)
x = x.T
print(x)
print(x.shape)

# 4. 尝试把 transpose 后的 Unit1_Tensors 用 .reshape(12) 拉平
x = x.reshape(12)
print(x)

"""
题目 4：Broadcasting 广播
创建：
x = torch.ones((3, 4))
y = torch.arange(4)
计算 x + y，并解释为什么可以相加。
"""

x = torch.ones((3, 4))
print(x)
y = torch.arange(4)
print(y)
z = x + y
print(z)

"""
题目 5：矩阵乘法
创建：
A = torch.randn(2, 3)
B = torch.randn(3, 4)
计算 A @ B，并打印结果 shape。然后回答：为什么结果是 (2, 4)？
"""

A = torch.randn(2, 3)
B = torch.randn(3, 4)
C = A @ B
print(C)
print(C.shape)

"""
题目 6：模拟一个小型神经网络输入
假设有 4 个样本，每个样本有 3 个特征：
X = torch.randn(4, 3)
现在有一个线性层参数：
W = torch.randn(3, 2)
b = torch.randn(2)
计算：
Y = X @ W + b
并打印所有 shape。
"""
X = torch.randn(4, 3)

W = torch.randn(3, 2)
b = torch.randn(2)

Y = X @ W + b
print(Y)
print("Y: " + str(Y.shape))
print(X)
print("X: " + str(X.shape))
print(W)
print("W: " + str(W.shape))
print(b)
print("b: " + str(b.shape))

"""
题目 7：Reduction 操作
创建：
x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
计算：
1. 所有元素的和
2. 每一列的和
3. 每一行的平均值
4. 保持维度的每一行平均值
"""

x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print(x)

# 1. 所有元素的和
print(x.sum())

# 2. 每一列的和
print(x.sum(dim=0))

# 3. 每一行的平均值
print(x.mean(dim=1))

# 4. 保持维度的每一行平均值
print(x.mean(dim=1, keepdim=True))

"""
题目 8：Device 检查
写一段代码：
1. 检查是否有 CUDA GPU
2. 如果有，把 Unit1_Tensors 放到 GPU
3. 如果没有，就用 CPU
4. 打印 Unit1_Tensors 的 device
"""

# 检查电脑现在能不能用 CUDA GPU，如果 CUDA 可用，就用 "cuda"，否则就用 "cpu"
device = "cuda" if torch.cuda.is_available() else "cpu"

# 把 x 移动到指定设备上。
x = torch.randn(2, 3).to(device)

print("using device:", device)
print("x device:", x.device)
print(x)