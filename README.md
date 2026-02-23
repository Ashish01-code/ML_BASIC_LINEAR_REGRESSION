# ML_BASIC_LINEAR_REGRESSION
# 💼 Salary Prediction using Linear Regression (Python + Scikit-Learn)

## 📌 Project Overview

This project builds a **Simple Linear Regression model** to predict salary based on years of experience using Python and Scikit-Learn.

It demonstrates a complete beginner-friendly Machine Learning workflow:

* Loading dataset from CSV
* Splitting data into training and testing sets
* Training a Linear Regression model
* Making predictions
* Evaluating model performance using R² score
* Visualizing regression line

---

## 📊 Dataset

The dataset contains:

| Column          | Description                        |
| --------------- | ---------------------------------- |
| YearsExperience | Number of years of work experience |
| Salary          | Corresponding salary               |

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn

---

## 🧠 Machine Learning Workflow

### 1️⃣ Import Libraries

Used for data handling, visualization, and model building.

### 2️⃣ Load Dataset

CSV file is read using pandas.

### 3️⃣ Feature Selection

* X → YearsExperience (input)
* y → Salary (target)

### 4️⃣ Train-Test Split

* 80% training data
* 20% testing data

### 5️⃣ Model Training

Linear Regression model is trained on training data.

### 6️⃣ Prediction

Model predicts salary for unseen test data.

### 7️⃣ Evaluation

Model accuracy measured using **R² Score**.

### 8️⃣ Visualization

Scatter plot + regression line for visual understanding.

---

## 📈 Model Output

The model predicts salary using:

Salary = m × YearsExperience + b

Where:

* m → slope (learned from data)
* b → intercept

Example prediction:

Salary for 12 years of experience → model generated value

---

## 📉 Performance Metric

R² Score indicates how well the model fits the data.

* 1 → perfect prediction
* 0 → no relationship

---

## 📷 Visualization

Blue dots → Actual data
Red line → Regression prediction

This helps visually understand how the model fits the data.

---

## ▶️ How to Run

1. Install required libraries

```bash
pip install numpy pandas matplotlib scikit-learn
```

2. Place `salary_data.csv` in your system

3. Run Python script

---

## 🎯 Learning Outcomes

After completing this project you understand:

✅ What Linear Regression is
✅ How ML models learn from data
✅ Train vs Test data concept
✅ Prediction process
✅ Model accuracy measurement
✅ Visual interpretation of regression

---

## 🚀 Next Learning Steps

* Manual Linear Regression (no library)
* Gradient Descent
* Multiple Linear Regression
* Polynomial Regression
* Logistic Regression
* Overfitting vs Underfitting

---
