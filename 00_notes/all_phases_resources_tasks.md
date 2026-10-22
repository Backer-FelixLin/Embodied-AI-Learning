# 全 Phase 书籍章节、视频与任务总结

## 总原则

- 本文件汇总各阶段的资料与任务；公开路线总览见 [ROADMAP.md](../ROADMAP.md)。后续阶段仍是规划，Phase 0 的具体执行安排见 [phase_0_plan.md](phase_0_plan.md)。
- 不按“看完多少课”算进度，按“写出代码、跑出实验、记录结果”算进度。
- 学习方式：Codex 在当前步骤前研读计划书指定且可访问的资料，再用中文系统讲授概念、推导、例子和实践要求。学习者不必亲自阅读原文或观看视频；资料链接用于来源核对和按需查阅。无法访问的材料要明确说明，并寻找可核实的同主题资料。
- 每个阶段都要留下可运行代码或实验报告。
- 核心算法尽量先自己写第一版，Codex 负责拆任务、review、debug 和搭实验框架。

## Phase 0: PyTorch 与 Deep Learning 基础

Phase 0 执行细节、最新进度与完整链接见 [phase_0_plan.md](phase_0_plan.md)，避免在多处维护相互冲突的独立任务单。

截至 2026-10-18：Tensor、Dataset/DataLoader、必要数学与 Autograd 的教学/实践检查已完成；Tensor 包含用户完成报告，Autograd 依据代码和保存输出审阅，非独立重跑。Phase 0 尚未结束。

剩余四个大步骤：

1. 线性回归：手动参数、MSE、SGD、训练循环、真实参数对照和单变量实验。
2. MLP 分类：分类基础、模型定义、训练与验证/测试评估。
3. 保存、加载与推理：延续分类项目，保存 `state_dict`、新会话加载并验证预测。
4. 最终验收：独立写并解释训练循环，核对运行证据与简短实验记录。

模型搭建、loss、optimizer 融入项目，不另设必须先学完的完整前置课程。下一步先讨论线性回归的小步骤，确认后再学习。

PyTorch 主教材（贯穿项目，不是独立前置）：

- PyTorch 官方 Learn the Basics / 中文“学习基础知识”
- 必看：Quickstart、Tensors、Datasets and DataLoaders、Build the Neural Network、Automatic Differentiation、Optimization、Save and Load
- Transforms 第一轮快速浏览即可
- [PyTorch 官方 Learn the Basics 中文入口](https://docs.pytorch.ac.cn/tutorials/beginner/basics/intro.html)，分步骤链接见详细计划
- PyTorch 官方 YouTube Series 仅作可选英文术语对照，不要求和中文材料重复完整学习
- 第一轮跳过 TensorBoard、Captum、分布式、编译、性能优化

书籍章节：

- 《动手学深度学习 / Dive into Deep Learning》
- Ch.2: 2.1 Data Manipulation、2.3 Linear Algebra、2.5 Automatic Differentiation
- 中文版 Ch.3：线性神经网络；3.1–3.3 对应线性回归，3.4–3.7 对应分类基础
- 中文版 Ch.4：多层感知机；4.1–4.4 核心研读，4.5–4.9 结合项目覆盖基础概念，4.10 案例按需参考，不新增竞赛项目门槛
- [中文版目录](https://zh.d2l.ai/)：选择 PyTorch 代码标签，不混用英文新版章节编号
- D2L 5.1/5.2/5.5 等是按需参考，不是额外必读门槛

视频：

- 李沐 D2L P4-P5: 数据操作
- P7-P8: 线性代数
- P10-P12: 矩阵 / 自动求导
- P13-P16: 线性回归和实现
- P17-P21: Softmax / Loss / Classification
- P24-P26: Perceptron / MLP
- 上述 P 编号采用所用合集的分集口径；原作者合并发布的视频按标题/分集名定位，链接见详细计划，不混用两套编号

任务：

- Tensor 小实验
- Autograd 小实验
- 从零实现 Linear Regression
- MLP/Fashion-MNIST 分类，包含训练与验证/测试评估；CNN/ResNet 属于 Phase 1A
- 保存、重新加载模型并进行 inference
- 一次受控变量实验与至少一份简短实验记录
- 已验收的 Notebook 可作为产物，不为匹配旧 `.py` 文件名重写

通过标准：

- 能不看教程写出 `zero_grad -> forward -> loss -> backward -> step`
- 能解释 training / validation / inference 的区别
- 展示实际运行结果并完成实验记录核查；只有达到 Gate 才进入 Phase 1A

## Phase 1A: CNN 与视觉表示

书籍章节：

- D2L Ch.6: Convolutional Neural Networks
- D2L Ch.7 中 ResNet 相关部分

视频：

- Stanford CS231n Lecture 5: CNN
- Stanford CS231n Lecture 6: CNN Architectures / ResNet

任务：

- 自己搭一个 CNN
- 用 CIFAR-10 或类似数据训练
- 比较简单 CNN 与 ResNet / transfer learning

通过标准：

- 能解释 convolution、feature map、channel、receptive field、ResNet shortcut
- 能自己搭一个基本视觉模型

## Phase 1B: Attention 与 Transformer

书籍章节：

- D2L Attention / Transformer 对应章节
- 只读 Self-Attention、Multi-Head Attention、Transformer 核心部分

视频：

- Stanford CS231n Lecture 8: Attention and Transformers

任务：

- 不用 `nn.MultiheadAttention`，自己实现简化版 Self-Attention
- 画 attention 权重或检查 attention 输出

通过标准：

- 能解释 token 如何通过 attention 读取其他 token
- 看到 Transformer 架构时不再觉得是黑箱

## 数学补漏轨道: 全程按需

书籍章节：

- Mathematics for Machine Learning
- Ch.2: Linear Algebra
- Ch.4: Matrix Decompositions
- Ch.5: Vector Calculus
- Ch.6: Probability and Distributions
- Ch.7: Continuous Optimization

视频：

- 不单独刷完整数学课程

任务：

- 建个人 math-notes
- 每遇到一个当前项目卡住的数学概念，就补一个短笔记

通过标准：

- 不要求完整学完，只要求能理解当前项目用到的公式

## Phase 2: Robotics 基础

书籍章节：

- Modern Robotics / 《现代机器人学》
- Ch.2: 2.1 Degrees of Freedom、2.2 Degrees of Freedom of a Robot、2.5 Task Space and Workspace
- Ch.3: Rotation Matrix、Angular Velocity、Homogeneous Transformation、必要 Screw/Twist 基础
- Ch.4: Forward Kinematics
- Ch.5: Jacobian、Singularity
- Ch.6: Numerical Inverse Kinematics

视频：

- Modern Robotics 官方章节短视频，对应上述章节即可

任务：

- 实现 2-DOF arm
- 实现 Forward Kinematics
- 实现 Jacobian
- 实现 Numerical IK
- 让末端跟踪目标点
- 初步操作 MuJoCo / ManiSkill 中的机械臂

通过标准：

- 能解释 joint、DOF、end-effector、joint space、Cartesian space、FK、IK、Jacobian
- 能不用 robotics 库完成一个简单 2D arm

## Phase 3: Behavior Cloning

书籍 / 阅读：

- 不需要额外买书
- 阅读 CS285 Lecture 2 配套 slides / notes

视频：

- Berkeley CS285 Lecture 2: Supervised Learning of Behaviors

任务：

- 自己构造或使用 demonstration dataset
- 训练最简单的 `observation -> action` policy

通过标准：

- 真正理解 `Observation -> Policy -> Action`
- 知道 classification/regression 与 policy learning 的关系
- 能解释 BC 为什么会累积误差

## Phase 4: ACT

论文：

- Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
- 阅读顺序：Abstract、Introduction、Figure / Architecture、Method 中 ACT 和 Action Chunking、Experiments、Conclusion
- Related Work 快速浏览，Appendix 第一遍不看

视频 / 教程：

- LeRobot ACT 官方教程

任务：

- 使用 LeRobot 完成 Dataset -> Train ACT -> Evaluate
- 至少测试 50 episodes
- 修改一个核心变量，例如 chunk size
- 记录 success rate

通过标准：

- 不仅能跑 ACT，还能解释为什么输出 action chunk
- 至少完成一个 controlled experiment

## Phase 5: Diffusion Policy

论文：

- Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- 阅读 Abstract、Introduction、核心 Architecture、multimodal action distribution、Experiments、Conclusion

视频 / 教程：

- Stanford CS231n Lecture 14: Diffusion Models
- Diffusion Policy 官方教程 / Notebook

任务：

- 在与 ACT 尽量相同 task 和 dataset 条件下训练 Diffusion Policy
- 制作 ACT vs Diffusion Policy 对比实验
- 比较 success rate、training time、inference latency、20/50/100 demos、failure modes

通过标准：

- 能解释 MSE regression 为什么会平均多个合理动作
- 能解释 Diffusion Policy 为什么适合 multimodal action
- 有完整对比表

## Phase 6: Reinforcement Learning

书籍章节：

- Sutton & Barto, Reinforcement Learning: An Introduction, Second Edition
- 必看 Ch.1: Introduction
- 必看 Ch.3: Finite Markov Decision Processes
- 必看 Ch.6: Temporal-Difference Learning
- 必看 Ch.13: Policy Gradient Methods
- 可选 / 快速看 Ch.2: Multi-armed Bandits
- 可选 / 快速看 Ch.4: Dynamic Programming
- 可选 / 快速看 Ch.5: Monte Carlo Methods
- Ch.7-Ch.12 第一轮不系统读

视频：

- WindyLab《强化学习的数学原理》精选到 MDP、Bellman、Value、TD、Q-learning
- Berkeley CS285 Lecture 4: Introduction to Reinforcement Learning
- Lecture 5: Policy Gradients
- Lecture 6: Actor-Critic Algorithms
- Lecture 7: Value Function Methods
- Lecture 8: Deep RL with Q-Functions
- 时间够再看 Lecture 9: Advanced Policy Gradients

任务：

- 简单 RL 环境
- Isaac Lab Cartpole
- 一个 manipulation / reaching RL task
- 记录 reward curve 和 success rate

通过标准：

- 能清楚说出 BC 与 RL 的本质区别
- 懂 Policy / Value / Q
- 知道 PPO / SAC 大体做什么
- 能独立跑训练和评估

## Phase 7: VLA / Generalist Policy

阅读：

- 第一遍不从大型论文开始
- 先读 SmolVLA / LeRobot 官方技术说明
- 再视情况读 VLA 论文的 Introduction、Architecture、Experiments

视频 / 教程：

- LeRobot / SmolVLA 官方教程
- Stanford CS231n Lecture 16: Vision and Language
- Stanford CS231n Lecture 17: Robot Learning

任务：

- 使用 pretrained VLA
- fine-tune 或 benchmark
- 改变 object、background、position、language wording
- 记录 distribution shift 下性能

通过标准：

- 能把 VLA 解释成更复杂的 policy
- 知道 image / language / state 如何进入模型
- 能设计泛化测试

## Phase 7 可选补充: 3D Vision

触发条件：

- 只有 manipulation 中发现 RGB 不够用时再补

书籍：

- 不单独读整本书

视频：

- Stanford CS231n Lecture 15: 3D Vision

任务：

- 一个最简单 depth / point cloud / pose 小实验

通过标准：

- 理解 2D perception 与 3D spatial reasoning 的区别

## Phase 8: Research Rotation

阅读：

- 开始按候选方向读精选论文，而不是教材

视频：

- 按候选方向补专题 lecture
- World Model / Model-Based Rotation 时再看 CS285 Lecture 10、11、12

任务：

- 选 2-3 个候选方向
- 每个方向做 1-2 周 mini-project
- 至少完成 2 个 rotation，最好 3 个

推荐 rotation：

- Generalization / Data Efficiency: 比较 20、50、100 demonstrations
- VLA / Robot Foundation Model: 测 object、position、background、language paraphrase 泛化
- World Model / Planning: 做 `(s_t, a_t) -> s_{t+1}` 预测并尝试简单 planning
- Real-Time Embodied AI: 比较 FP32、FP16、quantized、resolution、batch、设备下的 latency / FPS / memory / success rate
- RL / Dexterous Manipulation: PPO、SAC、contact-rich manipulation、dexterous hand、humanoid whole-body

通过标准：

- 每个 rotation 必须留下 Question、Hypothesis、Experiment、Result、Failure、Next Step

## 正式选方向 Gate

阅读：

- 回顾前面全部实验记录，不再靠新课推进

视频：

- 不需要再学新课

任务：

- 写一页 Research Direction Statement v1.0
- 写下一年 Research Roadmap

硬门槛：

- 自己写过完整 PyTorch training loop
- 自己实现过 FK、Jacobian、Numerical IK，并操作过 simulation robot
- 训练过简单 Behavior Cloning policy
- 完成 ACT manipulation project，并做自己的参数实验
- 完成 ACT vs Diffusion Policy 对比实验
- 完成至少一个 RL robot task
- 运行 / fine-tune / evaluate 过至少一个 VLA，并完成至少两个 Research Rotation
