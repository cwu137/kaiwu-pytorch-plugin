<!-- ```YAML
title: Kaiwu PyTorch Plugin Getting Started
slug: kpp-getting-started
sidebar_position: 0
layout: home
hide: false
keywords:
  - KPP
  - Guide
``` -->


# KPP Getting Started

> **Kaiwu-PyTorch-Plugin (KPP)** is a PyTorch plugin for training and evaluating quantum-native energy models and enhanced AI models on **Special Purpose Quantum Computers (SPQC)**.
> 
> It offloads Boltzmann sampling to the **Coherent Ising Machine (CIM)** through the Kaiwu SDK, while keeping all other computations, parameter updates, autograd, data loading, in the standard PyTorch workflow.

This guide walks you through the essentials in four parts:

```{toctree}
:maxdepth: 1
:hidden:

introduction
background
installation
quickstart
```

## Overview

Core concepts, design goals, features, and typical usage workflow.  
Read the [Introduction](introduction.md) to learn:

- What is KPP? Quantum-Classical Hybrid Programming Suite
- System Architecture & Component Interaction
- Core Concepts: Hybrid Workflow, Energy Model Hierarchy, Hardware Abstraction
- Typical Usage Workflow

## Prerequisite

Before proceeding, ensure you have basic knowledge of energy-based models and Boltzmann machines.  
Please read the [Prerequisites](background.md), it covers the essentials of RBM and energy functions.  
For a deeper dive into the statistical physics and neural network foundations, see the [Theoretical Foundations](../theoretical-foundations/index.md).

## Installation Guide

System requirements, local (conda/pip) and Docker setup, Kaiwu SDK configuration, and installation verification.  
See the [Installation Guide](installation.md) for:

- System Requirements
- Option 1: Local Setup
- Option 2: Docker Setup
- Kaiwu SDK Configuration & License
- Installation Verification

## Quick Start

RBM and BM training examples, sampler switching (SA / CIM), and next learning paths.  
Jump to the [Quick Start](quickstart.md) page to explore:

- RBM Training Walkthrough
- Code Mapping
- Switching Samplers: SA (classical) vs CIM (quantum)
- Next Learning Paths & Resources

---

# Tutorials for Beginners

```{toctree}
:maxdepth: 2
:hidden:

tutorials/index
```


The [Tutorials for Beginners](tutorials/index.md) section is designed for users who have already installed KPP and read the [Quick Start](quickstart.md) guide. 

Tutorials are organized into two tracks:

**Beginner Track**: Start from the [sampling bottleneck](tutorials/quantum_sampling_bottleneck.md) and build up to your first hands‑on application: [RBM classification](tutorials/rbm_classification.md) on handwritten digits.

**Generative Model Track**, explore more powerful models:

  - **BM Generation**: Use a fully connected Boltzmann Machine for fast, small‑scale data generation.
  - **Q-VAE (MNIST)**: A quantum‑enhanced variational autoencoder that combines a variational autoencoder with a quantum Boltzmann machine for image generation and representation learning.

