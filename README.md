# archaeology-vlm-analysis

A brief description of what this project does and who it's for.

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

- Python 3.x
- pip (Python package installer)

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Flask](https://flask.palletsprojects.com/) for making web development simple.
- Thanks to [SQLite](https://www.sqlite.org/) for providing an easy-to-use database engine.
