# Embodied AI Learning

This repository documents my learning path toward embodied AI, robot learning, and research engineering.

The goal is not to collect copied tutorials. The goal is to build evidence of learning through:

- small implementations written from first principles
- controlled experiments
- debugging notes
- research-style writeups
- direction decisions based on actual results

## Current Focus

**Phase 0: PyTorch and deep learning basics**

Current objective:

- understand tensors, autograd, loss, optimization, and training loops
- implement small experiments instead of only reading tutorials
- clearly distinguish training, validation, and inference

As of 2026-10-18, this repository contains Tensor, Dataset/DataLoader, minimum-math, and Autograd learning exercises. Phase 0 remains in progress.

Remaining sequence: **linear regression -> MLP classification -> save/load/inference -> final gate**. Model construction, loss, and optimization are learned within these projects. The next milestone is linear regression.

See the [roadmap](ROADMAP.md) for the public learning route and the [Phase 0 execution plan](00_notes/phase_0_plan.md) for current materials, tasks, and completion criteria.

## Repository Map

- `00_notes/` - planning notes and research questions
- `01_pytorch_basics/` - Phase 0 implementations
- `02_attention/` - attention and Transformer foundations
- `03_robotics/` - robotics fundamentals
- `04_behavior_cloning/` - imitation learning basics
- `05_act/` - Action Chunking Transformer experiments
- `06_diffusion_policy/` - diffusion policy experiments
- `07_reinforcement_learning/` - reinforcement learning practice
- `08_vla/` - vision-language-action and generalist policy work
- `09_research_rotations/` - focused mini research directions
- `reports/` - experiment report templates and writeups

## Working Style

For core algorithms, I try to follow this loop:

1. Understand the concept.
2. Write a first implementation.
3. Debug and review the code.
4. Run a measurable experiment.
5. Record results, failure modes, and next steps.

The long-term direction is generalizable robot learning for manipulation, with possible future depth in real robots, sim-to-real transfer, real-time deployment, and world models or planning.
