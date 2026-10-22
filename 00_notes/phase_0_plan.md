# Phase 0 计划：PyTorch 与 Deep Learning 基础

## 范围与学习约定

- 公开路线总览见 [ROADMAP.md](../ROADMAP.md)；本文件记录 Phase 0 的具体任务、资料和过关条件。
- 若本文件与公开总览有出入，应同步更新两处说明；不额外增加进入 Phase 1A 的门槛。
- 学习循环：精选资料 -> 自己实现 -> 改动一个变量 -> 评估与分析 -> 留下报告 -> 检查过关标准。
- Phase 开始前讨论大步骤；每个大步骤开始前讨论小步骤数量、概念和目标，确认后再开始。教学拆分不等于新增核心项目。
- 中文讲解，陌生术语先解释并标注英文，配例子、理解检查和实践。Codex 在每个小步骤前先研读可访问的指定材料，用自己的表述系统讲授；学习者不必亲自阅读原文或观看视频。仍提供准确链接供核对和日后查阅，并说明无法访问或未能核实的内容。
- 核心代码由学习者先写，Codex 提供讲解、题目、骨架、审阅和调试。不先学完全部 PyTorch 文档再实践；模型、loss、optimizer 围绕项目学习。
- 区分用户报告、代码/保存输出审阅和独立运行验证；不因文件存在就认定掌握，不声称观看过不可访问的视频。
- 学习者的 PyTorch 环境在其他位置，未经请求不配置或运行该环境，不改动已有学习产物。

## 目标与原定实践顺序

要回答：一个 batch 经过模型、loss、反向传播和优化器后，参数为什么会改变？

Phase 0 的五项实践：

1. Tensor 操作和 shape 实验。
2. 手算并验证简单导数，观察梯度累积。
3. 手动参数、MSE 与 SGD 的线性回归。
4. MLP 分类，包含训练集与验证/测试评估。
5. 保存并重新加载模型，做一次 inference。

覆盖 Tensor、shape/dtype/device、Dataset/DataLoader、`nn.Module`、forward、loss、autograd、optimizer、train/validation/inference、`state_dict`。

## 当前进度

截至 2026-10-18，依据教学对话和产物审阅记录：

| 内容 | 状态与依据 |
| --- | --- |
| Tensor 基础与实验 | 用户已报告完成，不要求为匹配旧文件名重做 |
| Dataset/DataLoader | 教学检查已完成，已有对应 Notebook 和实验文件 |
| 数据预处理、必要线性代数与微积分 | 已有学习记录与 Notebook；后续数学按需补漏 |
| Autograd | 概念与综合实践验收通过；审阅了 `autograd_demo.ipynb`、`autograd_demo2.ipynb` 的代码、保存输出及导数图，未独立重新运行 |
| 线性回归 | 待开始；下一步先讨论小步骤 |
| MLP 分类 | 待完成 |
| 保存、加载与推理 | 待完成 |
| 最终验收和实验记录核查 | 待完成；Phase 0 尚未结束 |

**剩余口径：3 项核心实践 + 1 次最终验收，共 4 个大步骤。** 不把“模型搭建”“优化与训练”单列为两门必须先完成的前置课程。

## 教材口径

- 核心是 PyTorch Learn the Basics、D2L 中文版 2.1/2.3/2.5 与第 3–4 章，以及计划书指定的李沐视频。
- 按 [D2L 中文目录](https://zh.d2l.ai/) 和 PyTorch 代码标签定位：第 3 章“线性神经网络”，第 4 章“多层感知机”。不要混用英文新版章节编号。
- P4–5、P7–8、P10–12、P13–21、P24–26 是所用合集的分集编号；原作者常合并发布。以下按标题/分集名定位，不把合集编号和原作者视频编号混用。
- 英文对照可用 [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) 和 [D2L 英文版](https://d2l.ai/)，按标题定位；不要求中英文重复完整学习。
- D2L 第 5 章、官方 YouTube 系列等是按需参考，不是新增必修或 Gate。不要求完整学习优化算法、TensorBoard、Captum、分布式、编译和性能优化。

## 剩余步骤 1：线性回归与训练循环

### 内容与产物

- 回归、特征、标签、权重、偏置、预测、MSE、batch、epoch、学习率和小批量 SGD。
- 生成已知真实参数的合成数据，手动初始化参数，用 Autograd 求梯度，自己执行 SGD 更新。
- 记录损失和真实/学习参数对照；先手写，再对照 `nn.Linear`、`nn.Module`、loss 和 optimizer 的简洁实现。
- 能解释 `backward()` 计算梯度而更新规则改变参数。改变一个核心变量（如学习率），保持其余设置尽量一致，记录结果与分析。

### 教材与视频

- [D2L 3.1 线性回归](https://zh.d2l.ai/chapter_linear-networks/linear-regression.html)：模型、损失、优化与训练；概率推导所需知识按需补。
- [D2L 3.2 从零开始实现](https://zh.d2l.ai/chapter_linear-networks/linear-regression-scratch.html)：逐段理解并自行实现。
- [D2L 3.3 简洁实现](https://zh.d2l.ai/chapter_linear-networks/linear-regression-concise.html)：比较框架封装与手写版。
- [PyTorch 构建神经网络](https://docs.pytorch.ac.cn/tutorials/beginner/basics/buildmodel_tutorial.html)：本步取模型定义、`Linear`、参数访问，多层结构留到分类项目。
- [PyTorch 优化模型参数](https://docs.pytorch.ac.cn/tutorials/beginner/basics/optimization_tutorial.html)：超参数、loss、optimizer 和训练流程；分类代码在下一步完整应用。
- [李沐 08 线性回归 + 基础优化算法](https://www.bilibili.com/video/BV1PX4y1g7KC/)：线性回归、基础优化算法、从零实现、简洁实现四个教学分集；QA 按需。

## 剩余步骤 2：分类基础与 MLP 项目

### 内容与产物

- 分类与回归、类别标签、logits、Softmax、交叉熵、准确率、Fashion-MNIST 和批量形状。
- 隐藏层、激活函数和 `Flatten/Linear/ReLU/Sequential`；用 `nn.Module` 定义 MLP，完成 loss、optimizer、训练和验证/测试循环。
- 区分训练、验证和测试用途，避免用测试集调参；理解欠拟合、过拟合、基本正则化、初始化和分布变化。
- 产物包括模型、数据划分、损失与准确率记录、评估和失败分析，以及结合项目完成的单变量对照实验。
- 先用小例子理解分类，再完成 MLP 主项目，不要求每个小节另交大型项目。

### 教材与视频

- [D2L 3.4 Softmax 回归](https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html)、[3.5 图像分类数据集](https://zh.d2l.ai/chapter_linear-networks/image-classification-dataset.html)。
- [D2L 3.6 Softmax 从零实现](https://zh.d2l.ai/chapter_linear-networks/softmax-regression-scratch.html)、[3.7 简洁实现](https://zh.d2l.ai/chapter_linear-networks/softmax-regression-concise.html)。
- [D2L 4.1 多层感知机](https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp.html)、[4.2 从零实现](https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp-scratch.html)、[4.3 简洁实现](https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp-concise.html)。
- [D2L 4.4 模型选择、欠拟合和过拟合](https://zh.d2l.ai/chapter_multilayer-perceptrons/underfit-overfit.html)：重点学习。
- [D2L 第 4 章目录](https://zh.d2l.ai/chapter_multilayer-perceptrons/index.html)：4.5 权重衰减、4.6 Dropout、4.7 传播与计算图、4.8 数值稳定性与初始化、4.9 环境和分布偏移，结合项目覆盖基础概念；4.10 房价案例按需参考，不新增竞赛项目门槛。这是教学深度细化，不改变计划书的第 3–4 章核心书目。
- 完整应用 PyTorch [构建神经网络](https://docs.pytorch.ac.cn/tutorials/beginner/basics/buildmodel_tutorial.html) 和 [优化模型参数](https://docs.pytorch.ac.cn/tutorials/beginner/basics/optimization_tutorial.html)。
- [李沐 09 Softmax 回归 + 损失函数 + 图片分类数据集](https://www.bilibili.com/video/BV1K64y1Q7wu/)：前五个教学分集。
- [李沐 10 多层感知机 + 代码实现](https://www.bilibili.com/video/BV1hh411U7gn/)：感知机、多层感知机、代码实现，已掌握内容不重复刷。
- 过拟合等补充视频在对应小步骤开始时提供并核对，不把整套视频列为新增前置。

## 剩余步骤 3：保存、加载与推理

- 延续 MLP，不另开大型项目。学习 `state_dict`、保存/恢复参数、相同模型结构、设备和单样本 batch 维。
- 区分 `model.train()`、`model.eval()` 和 `torch.no_grad()`；评估模式不等于禁用 Autograd。
- 主教材：[PyTorch 保存和加载模型](https://docs.pytorch.ac.cn/tutorials/beginner/basics/saveloadrun_tutorial.html)，重点是 `state_dict` 和推理。
- 按需参考：[D2L 5.5 读写文件](https://zh.d2l.ai/chapter_deep-learning-computation/read-write.html)，不是额外必读门槛。
- 视频辅助：[李沐 16 PyTorch 神经网络基础](https://www.bilibili.com/video/BV1AK4y1P7vs/) 的读写文件部分，不要求整讲重复学习。
- 产物：checkpoint、在新会话重建模型并加载的代码、一次预测，以及相同输入/评估条件下保存前后的输出一致性检查。
- 到本步时提醒学习者 Phase 0 接近尾声，未通过最终验收前不标记完成。

## 剩余步骤 4：最终验收

不新增教材。先独立完成，再用 [PyTorch Quickstart](https://docs.pytorch.ac.cn/tutorials/beginner/basics/quickstart_tutorial.html) 和已学章节查漏。

不看教程写出并解释以下流程，展示实际运行结果：

```python
optimizer.zero_grad()
outputs = model(inputs)
loss = criterion(outputs, targets)
loss.backward()
optimizer.step()
```

- 解释数据、预测、loss、梯度和参数更新的关系，以及 training、validation、inference 的区别；测试集用途也应清楚。
- 核查 Tensor、Autograd、手动参数/MSE/SGD 的线性回归、MLP 训练与评估、保存加载和推理的产物。
- 至少一份简短实验记录，使用 [实验记录模板](../reports/research_notebook_template.md)：Question、Hypothesis、Setup、Experiment、Result、Analysis/Failure、Next Step。
- Setup 写环境、数据、seed、模型、主要超参数、硬件和训练步数；对照尽量只改一个核心变量，说明无法控制的差异。不要将后续机器人阶段的 episode 数量和成功率统计门槛移植到 Phase 0。
- 通过才结束 Phase 0 并进入 Phase 1A；未通过则只补对应缺口。

## 产物位置与范围

- `.ipynb` 或 `.py` 均可，不为旧规划中的文件名复制或重写已验收内容。
- 当前仓库的 Phase 0 产物索引见 [01_pytorch_basics/README.md](../01_pytorch_basics/README.md)。
- 未来文件名和小步骤在开始相应项目之前讨论，本次文档对齐不提前创建程序。
- 报告放入 `reports/`，或先在 Notebook 记录并建立索引。阅读/实验精力分配可参考 30%/70%，不是硬性工时要求。
- CNN/ResNet 属于 Phase 1A，Attention/Transformer 属于 Phase 1B，不是 Phase 0 附加项目。
