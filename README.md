# Analysis of Vision Language Models in Archaeology

This project is to analyze and evaluate how existing VLMs perform on archaeological data. Without further training on these datasets, we aim to explore which VLM is most suitable for sorting, describing, and mainly answering questions regarding archaeological artifacts through Visual Question Answering (VQA). Our project will focus on zero-shot classification and assess how well these VLMs do on unseen data.

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Project Structure](#structure)
4. [Acknowledgments](#acknowledgments)

## Description

This project consists of two main components: the creation of a dataset and taxonomy, and the evaluation of Visual Language Models (VLMs) for archaeological data. The first part focuses on developing a comprehensive dataset and taxonomy to effectively categorize and analyze archaeological data. The second part involves evaluating VLM performance through Visual Question Answering (VQA) tasks to test their applicability to archaeological research. We provide the necessary code for both dataset creation and evaluation on this GitHub repository, allowing users to replicate and extend the research.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Anaconda

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/tun-ya/archaeology-vlm-analysis.git
    cd archaeology-vlm-analysis
    ```

2. Create a conda environment:

    ```bash
    conda create --name myenv
    ```

3. Activate the virtual environment:

    ```bash
    conda activate myenv
    ```

4. Install the dependencies:

    ```bash
    conda install -r requirements.txt
    ```

## Project Structure

This repository is organized into the following key directories and files:

- **`data/`**: This directory includes all necessary files and scripts for creating the dataset and taxonomy for archaeological data.
- **`models/`**: Contains the scripts for evaluating Visual Language Models (VLMs) using Visual Question Answering (VQA) tasks on the dataset.
- **`demo/`**: Contains example for evaluation.
- **`requirements.txt`**: A file listing the required libraries and dependencies to run the project.
- **`README.md`**: This file, providing an overview of the project, setup instructions, and usage guidelines.

Each section has its own **README.md** for specific setup and usage instructions.


## Acknowledgments

- Thanks to [Penn Museum](https://www.penn.museum/)
- Thanks to [LLaVa-NeXT](https://huggingface.co/llava-hf/llava-v1.6-mistral-7b-hf).
- Thanks to [Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct).
