# 🧪 ModelLab

**An interactive machine-learning dashboard to train, evaluate, and experiment with classification models.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

🚀 **[Launch ModelLab — Live Demo](https://model-lab-qgmhwjy6adtjgp5pnrb3dk.streamlit.app/)**

## Overview

ModelLab is a web application built with Python and Streamlit that makes machine-learning experimentation interactive. Train different classification algorithms, adjust their parameters, and compare their performance on the Wine dataset.

## Features

- **Four classification algorithms:** Random Forest, Logistic Regression, K-Nearest Neighbours (KNN), and Decision Tree.
- **Interactive hyperparameters:** Adjust tree depth, number of estimators, K, and regularization strength.
- **Evaluation metrics:** Accuracy, weighted precision, weighted recall, and weighted F1-score.
- **Confusion matrix:** Visualize correct and incorrect classifications.
- **Dataset explorer:** Inspect the Wine dataset and its features.
- **Prediction analysis:** Compare actual and predicted classes.
- **CSV export:** Download model predictions for further analysis.
- **Reproducible experiments:** Change the random seed and test-set size.

## Tech Stack

- Python
- Streamlit
- pandas
- Matplotlib
- scikit-learn

## Dataset

ModelLab uses the built-in Wine dataset from scikit-learn. It contains 178 samples, 13 numerical features, and 3 wine classes.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/onooyt-prog/model-lab.git
cd model-lab
```

Create and activate a virtual environment:

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies and start the application:

```bash
pip install pandas matplotlib streamlit scikit-learn
streamlit run app.py
```

## Project Structure

```text
model-lab/
├── app.py
├── README.md
└── requirements.txt
```

## Future Improvements

- Compare all models in a leaderboard.
- Add feature-importance visualizations.
- Support user-uploaded datasets.
- Add cross-validation and hyperparameter search.

---

Built with Python, Streamlit, and scikit-learn. 🧪
