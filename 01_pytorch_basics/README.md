# Phase 0：PyTorch 基础

本目录保存 Phase 0 的学习笔记和实验代码。总体路线见 [ROADMAP](../ROADMAP.md)，具体任务与过关条件见 [Phase 0 计划](../00_notes/phase_0_plan.md)。Notebook 中的讲解片段用于学习，运行时可能依赖前面的单元格。

## 已有内容

- [Unit 1：Tensor](Unit1_Tensors/)：张量操作与形状实验。
- [Unit 2：Dataset 和 DataLoader](Unit2_Datasets_and_DataLoaders/)：数据集、批处理和数据加载。
- [Unit 3：数据预处理](Unit3_Data_Preprocessing/) 与 [Unit 4：必要数学](Unit4_Linear_Algebra/)：按项目所需补充基础。
- [Unit 5：Autograd](Unit5_Autograd/)：自动微分练习与导数图。
- [Unit 6：线性回归与训练循环](Unit6_Linear_Regression_and_the_Training_Loop/)：手写 SGD、框架实现和学习率对照。
- [Unit 7：分类基础与 MLP](Unit7_Classification_Fundamentals&MLP_Project/)：Fashion-MNIST 分类、手写与框架 MLP 的训练和验证；`Classification_demo.ipynb`、`MLP_demo.ipynb` 汇集对应代码。`activation-curves.png` 展示激活函数及其局部导数，生成脚本为 `activation-curves.py`。

## 数据与环境

Unit 7 的 Fashion-MNIST 代码使用相对于 Unit 7 目录的 `../Unit2_Datasets_and_DataLoaders/data`，并设置了 `download=False`。运行这些单元格前，需要在该位置准备好数据；本地数据由仓库的 `.gitignore` 排除。`activation-curves.py` 使用 Windows 的 `C:/Windows/Fonts/arial.ttf`，图像文件可直接查看。

Phase 0 仍需完成模型选择等后续学习、模型保存与加载、推理及最终验收。实验记录可参考 [报告模板](../reports/research_notebook_template.md)。

