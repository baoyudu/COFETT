# COFETT: EEG-to-Text Benchmark for Real-World Scenarios

This repository accompanies the paper:

**Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark**

## Overview

This repository is the official code and resource repository for the above paper.  
It is built around **COFETT**, a neuropsychology-inspired benchmark for evaluating **EEG-to-Text** in more realistic settings.

Unlike prior EEG-to-Text benchmarks that heavily rely on teacher forcing during evaluation, this work focuses on **teacher-forcing-free assessment** and investigates whether EEG contains linguistically decodable information in real-world scenarios.

## Dataset

The dataset used in this work can be obtained from OpenNeuro:

**https://openneuro.org/datasets/ds006317**

Please download the data from OpenNeuro and place it in the appropriate local directory before running preprocessing or experiments.

## EEG Experimental Paradigm

The EEG experiment follows a neuropsychology-inspired repeated inner-speech design.

- The experiment lasts for **8 days**
- Each day contains **4 sessions**
- Each session contains multiple trials
- Each trial consists of three phases:
  1. **Reading phase**  
     Participants read a sentence presented word by word
  2. **Recall / inner-speech phase**  
     Participants silently recall the sentence verbatim without speaking aloud
  3. **Rest phase**

To reduce the impact of EEG instability, the benchmark includes **within-participant repeated recordings of the same sentences across sessions and days**.  
EEG signals were recorded using a **128-channel high-density EEG cap**.  
Stimulus presentation was implemented with **PsychoPy (v2024.2.3)**.

## Purpose of This Repository

This repository is intended to provide resources for:

- EEG-to-Text benchmarking
- teacher-forcing-free evaluation
- EEG preprocessing and feature extraction
- sentence-level EEG-text alignment
- reproducible experiments on COFETT

## Citation

If you use this repository, dataset, or any related materials, please cite:

**Zihan Zhang, Yu Bao, Xiao Ding, Tianyi Jiang, Kai Xiong.**  
*Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark.*
