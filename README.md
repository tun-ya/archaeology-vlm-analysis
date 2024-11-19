# Analysis of Vision Language Models in Archaeology

This project is to analyze and evaluate how existing VLMs perform on archaeological data. Without further training on these datasets, we aim to explore which VLM is most suitable for sorting, describing, and mainly answering questions regarding archaeological artifacts through Visual Question Answering (VQA). Our project will focus on zero-shot classification and assess how well these VLMs do on unseen data.

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)
5. [Acknowledgments](#acknowledgments)

## Description

This project is a Python web application that allows users to track their daily tasks and productivity. It provides a simple user interface to add, edit, and delete tasks. The project is built using Flask for the backend and SQLite for the database.

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

## Usage

Once the application is running, you can access it via your browser. The main features include:

- **Add a task**: Use the form to add tasks to your to-do list.
- **Edit a task**: Click on a task to edit it.
- **Delete a task**: Remove tasks you no longer need.

### Example:

After running the app, you can visit `http://localhost:5000` in your browser, where you can start adding tasks.

## License

.

## Acknowledgments

- Thanks to [LLaVa-NeXT](https://huggingface.co/llava-hf/llava-v1.6-mistral-7b-hf).
- Thanks to [Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct).
