# 01_pytorch_basics

This folder indexes Phase 0 artifacts. CNN/ResNet work is a later Phase 1A extension, not a Phase 0 requirement.

Do not fill it with copied tutorial code. Each file should be small enough to explain line by line.

Learning plans:

- [Public roadmap](../ROADMAP.md).
- [Phase 0 execution plan and materials](../00_notes/phase_0_plan.md).

## Current Evidence

As of 2026-10-18:

- Tensor: [lab_tensor.py](Unit1_Tensors/lab_tensor.py) and learning exercises.
- Dataset/DataLoader: teaching checks complete; [DataLoader.ipynb](Unit2_Datasets_and_DataLoaders/DataLoader.ipynb).
- Minimum math and data preprocessing: learning notebooks exist; gaps remain just-in-time work, not a separate full course.
- Autograd: worked examples, explanations, and a derivative plot; [autograd_demo.ipynb](Unit5_Autograd/autograd_demo.ipynb), [autograd_demo2.ipynb](Unit5_Autograd/autograd_demo2.ipynb), [plot](Unit5_Autograd/sin_autograd_derivative.png).

## Remaining Work

1. Linear regression: synthetic data, manual parameters, MSE, Autograd, hand-written SGD, comparison with ground truth, then a concise framework implementation.
2. MLP classification: Fashion-MNIST, model definition, loss/optimizer, training and validation/test evaluation, curves and analysis.
3. Save/load/inference: continue the classifier, restore a `state_dict` in a new session and verify predictions.
4. Final gate: independently write and explain the training loop, demonstrate results, and review a controlled experiment and short report.

Model construction and optimization are taught within these projects. The next milestone is linear regression.

Notebook or script artifacts are both valid. Reports use the [experiment template](../reports/research_notebook_template.md).

