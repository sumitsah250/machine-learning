<h1 align="center">🧠 Machine Learning & Deep Learning Practice Repository</h1>
<p align="center">
  <b>By Sumit Sah</b><br>
  Android Developer & AI Enthusiast | Exploring the world of Machine Learning & Neural Networks
</p>

<p align="center">
  <a href="https://github.com/sumitsah250"><img src="https://img.shields.io/badge/GitHub-sumitsah250-black?logo=github"></a>
  <a href="https://www.linkedin.com/in/your-linkedin"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin"></a>
  <a href="https://your-portfolio-link"><img src="https://img.shields.io/badge/Website-Portfolio-green?logo=google-chrome"></a>
</p>

---

<h2 align="center">📚 Overview</h2>

This repository is a collection of my **Machine Learning and Deep Learning practice notebooks & scripts**.  
It includes everything from basic model training to more refined neural network implementations — showcasing my growth as an **AI & ML developer**.

Each file and folder represents hands-on experiments with algorithms, datasets, and performance optimization.

---

<h2 align="center">📂 Project Structure</h2>

| Folder/File | Description |
|--------------|-------------|
| **__pycache__/** | Compiled Python cache files |
| **deep learning/** | Experiments with Artificial Neural Networks (ANN) and misclassification analysis |
| **projects/** | Refined and graduate-level model implementations |
| **AllAboutLinearRegression.ipynb** | Linear Regression theory and implementation |
| **AllAboutLogiticRegression.ipynb** | Logistic Regression with dataset-based evaluation |
| **Linear_regression_function.py** | Custom Python implementation of Linear Regression |
| **all_about_k_fold_cross_validation.ipynb** | Cross-validation experiments on churn dataset |
| **all_about_support_vector_machine.ipynb** | Support Vector Machine applied on diabetes dataset |
| **diabetes.csv** | Dataset for classification and regression tasks |
| **heart.csv** | Dataset used for cross-validation and model testing |
| **salary_data.csv** | Salary prediction dataset for regression models |
| **requirements.txt** | List of dependencies for running all notebooks and scripts |

---

<h2 align="center">🧩 Concepts Covered</h2>

- Linear Regression  
- Logistic Regression  
- Support Vector Machines (SVM)  
- Artificial Neural Networks (ANN)  
- Model Evaluation & Misclassification  
- K-Fold Cross Validation  
- Data Preprocessing & Normalization  
- Model Refinement and Accuracy Improvement  

---

<h2 align="center">🧠 Tech Stack</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" />
  <img src="https://img.shields.io/badge/Library-NumPy-red?logo=numpy" />
  <img src="https://img.shields.io/badge/Library-Pandas-green?logo=pandas" />
  <img src="https://img.shields.io/badge/Library-Scikit--learn-yellow?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Library-TensorFlow-orange?logo=tensorflow" />
  <img src="https://img.shields.io/badge/Library-Matplotlib-blue?logo=plotly" />
</p>

---

<h2 align="center">📊 Example Use Case</h2>

```python
# Linear Regression Example
from Linear_regression_function import LinearRegressionModel

model = LinearRegressionModel()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
model.evaluate(y_test, predictions)
