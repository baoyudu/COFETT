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

This dataset was collected using the same acquisition setup as our previous work, [Chisco: An EEG-based BCI dataset for decoding of imagined speech](https://www.nature.com/articles/s41597-024-04114-1), ensuring consistency in the EEG recording hardware and experimental environment.

## EEG Experimental Paradigm

The EEG experiment follows a neuropsychology-inspired repeated inner-speech design.

- The experiment lasts for **8 days**
- Each day contains **4 sessions**
- Each session contains multiple trials
- Each trial consists of three phases:
  1. **Reading phase**  
     Participants first read a target sentence presented **word by word with sequential highlighting** on the screen.  
     If a sentence contains **x words**, the duration of this phase is **0.4x seconds**.  
     This phase serves as a controlled language-encoding stage: it standardizes the semantic content to be processed, reduces variability introduced by unconstrained imagination, and primes the participant for the subsequent silent recall stage.

  2. **Recall / inner-speech phase**  
     After reading, participants are instructed to **silently recall the sentence verbatim without speaking aloud**.  
     The duration of this phase is **0.4(x + 1) seconds**.  
     This is the core phase of the paradigm and corresponds to the **inner-speech signal** used in the downstream EEG-to-text analysis. The extra time relative to the reading phase gives participants sufficient time to internally reproduce the sentence in a speech-like manner rather than merely recognize it visually.  
     The design is motivated by prior work suggesting that imagined speech is embedded within inner speech, and by evidence that speech-related language networks engaged during reading show partial overlap with those involved in speech imagery and internal speech generation. This helps create a smoother transition from visual language processing to covert verbal rehearsal.

  3. **Rest phase**  
     After the recall stage, a fixation cross is presented and participants enter a **1.8-second rest period**.  
     This phase separates consecutive trials, reduces carryover from the previous sentence, and provides a short recovery interval before the next stimulus begins. In practice, it helps make trial boundaries cleaner and stabilizes the temporal structure of the EEG recordings.

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
