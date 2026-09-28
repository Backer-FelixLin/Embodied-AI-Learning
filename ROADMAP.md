# Roadmap

This roadmap is a public overview of the learning path. Detailed notes and task lists live in `00_notes/`.

## Phase 0: PyTorch and Deep Learning Basics

Status: in progress

Focus:

- tensor operations
- autograd
- loss functions
- optimization
- training loops
- validation and inference

Artifacts:

- tensor operation demo
- autograd experiment
- linear regression from scratch
- small MLP classifier

Pass gate:

- write `zero_grad -> forward -> loss -> backward -> step` without copying a tutorial
- explain training, validation, and inference clearly

## Phase 1: Visual Representation and Attention

Focus:

- CNN basics
- feature maps and receptive fields
- ResNet-style shortcuts
- self-attention
- Transformer foundations

Artifacts:

- simple CNN experiment
- simplified self-attention implementation
- attention visualization or inspection

## Phase 2: Robotics Fundamentals

Focus:

- joints and degrees of freedom
- coordinate frames
- forward kinematics
- Jacobian
- numerical inverse kinematics
- simple simulation workflows

Artifacts:

- 2D arm implementation
- forward kinematics demo
- Jacobian and numerical IK experiment
- simple end-effector tracking task

## Phase 3: Behavior Cloning

Focus:

- observation-to-action policies
- demonstration datasets
- supervised learning for control
- compounding error

Artifacts:

- simple behavior cloning policy
- controlled experiment on demonstration quantity or data quality

## Phase 4: ACT

Focus:

- Action Chunking Transformer
- action chunk prediction
- manipulation policy evaluation

Artifacts:

- ACT training and evaluation run
- at least one controlled variable experiment
- success-rate report

## Phase 5: Diffusion Policy

Focus:

- multimodal action distributions
- action denoising
- comparison with ACT-style policies

Artifacts:

- diffusion policy training run
- ACT vs Diffusion Policy comparison
- report on success rate, latency, data quantity, and failure modes

## Phase 6: Reinforcement Learning

Focus:

- Markov decision processes
- value functions
- policy gradients
- actor-critic methods
- robot control experiments

Artifacts:

- simple RL environment
- reward curve
- simulated reaching or manipulation task

## Phase 7: VLA and Generalist Robot Policy

Focus:

- vision-language-action models
- pretrained policy evaluation
- distribution shift
- language, object, and background generalization

Artifacts:

- pretrained VLA evaluation
- controlled generalization tests
- failure analysis

## Phase 8: Research Rotations

Focus:

- choose 2-3 candidate research directions
- run short mini-projects
- compare evidence instead of choosing only from interest

Possible directions:

- data efficiency and generalization
- robot foundation models
- world models and planning
- real-time embodied AI
- reinforcement learning for manipulation

Each rotation should leave:

- question
- hypothesis
- experiment
- result
- failure analysis
- next step

## Final Gate

Before choosing a formal research direction, this repository should contain evidence of:

- a complete PyTorch training loop written from scratch
- a simple robotics kinematics implementation
- a behavior cloning experiment
- an ACT or related manipulation policy experiment
- a diffusion policy comparison
- at least one reinforcement learning task
- at least one VLA or generalist policy evaluation
