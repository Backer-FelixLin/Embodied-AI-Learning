# Phase 0 Plan - PyTorch and Deep Learning Basics

## Goal

Build a working mental model of how neural networks learn:

zero_grad -> forward -> loss -> backward -> step

By the end of this phase, the user should be able to write a simple training loop without copying a tutorial.

## PyTorch Foundation Pre-Step

Before the main deep learning chapters, build the minimum PyTorch workflow needed for Phase 0.

Primary docs / reading:

- PyTorch official "Learn the Basics" / PyTorch 中文 "学习基础知识"
  - Quickstart
  - Tensors
  - Datasets and DataLoaders
  - Build the Neural Network
  - Automatic Differentiation with `torch.autograd`
  - Optimizing Model Parameters
  - Save and Load the Model
- Optional English reference: PyTorch "Introduction to PyTorch - YouTube Series"
  - Introduction to PyTorch
  - Introduction to PyTorch Tensors
  - The Fundamentals of Autograd
  - Building Models with PyTorch
  - Training with PyTorch
  - Skip TensorBoard and Captum on the first pass

Chinese video support:

- 李沐 D2L PyTorch / 动手学深度学习:
  - 4 数据操作
  - 5 数据操作实现
  - 7 线性代数
  - 8 线性代数实现
  - 10 矩阵计算
  - 11 自动求导
  - 12 自动求导实现

English terms to annotate while learning:

- `Tensor`, `shape`, `dtype`, `device`
- `Dataset`, `DataLoader`, `batch`, `shuffle`
- `nn.Module`, `forward`, `parameters`
- `autograd`, `requires_grad`, `.backward()`, `.grad`
- `loss function`, `optimizer`, `zero_grad`, `step`
- `state_dict`, `checkpoint`, `inference`

PyTorch pre-step is complete when the user can:

- create and inspect tensors
- move tensors/model to a device if available
- use `Dataset` / `DataLoader` at a basic level
- define a tiny `nn.Module`
- run one forward pass
- compute a loss
- call `.backward()`
- update parameters with an optimizer
- save and load a `state_dict`

## Core Reading

Dive into Deep Learning / 动手学深度学习:

- 2.1 Data Manipulation
- 2.3 Linear Algebra
- 2.5 Automatic Differentiation
- Chapter 3
- Chapter 4

Use the Chinese text for concepts and the English/PyTorch code for terminology and implementation details.

## Programs

### Program 1: Tensor Operations

File to create later:

`01_pytorch_basics/tensor_demo.py`

Must demonstrate:

- tensor creation
- shape / dtype / device
- indexing and slicing
- broadcasting
- matrix multiplication
- reshape / view / transpose
- simple timing or memory observation if useful

### Program 2: Autograd Experiment

File to create later:

`01_pytorch_basics/autograd_demo.py`

Must demonstrate:

- scalar function gradient
- vector/tensor gradient
- `.backward()`
- `.grad`
- what happens if gradients are not cleared
- one small manually checked derivative

### Program 3: Linear Regression from Scratch

File to create later:

`01_pytorch_basics/linear_regression.py`

Must include:

- synthetic data generation
- parameters initialized manually
- prediction
- MSE loss
- gradient computation
- SGD update
- loss curve or printed progress
- learned parameters compared with ground truth

### Program 4: MLP Classification

File to create later:

`01_pytorch_basics/mlp.py`

Must include:

- dataset loading
- train/validation split or train/test evaluation
- model definition
- loss and optimizer
- training loop
- evaluation loop
- saved model checkpoint

## Pass Gate

Phase 0 is complete only when the user can explain and write:

```text
optimizer.zero_grad()
outputs = model(inputs)
loss = criterion(outputs, targets)
loss.backward()
optimizer.step()
```

And can explain the difference between:

- training
- validation
- inference
