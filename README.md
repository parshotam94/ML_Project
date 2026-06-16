# 🎓 Student Performance Tracker

A Machine Learning web application that predicts a student's mathematics score based on demographic, parental, and academic-related features. The project follows an end-to-end ML pipeline including data ingestion, preprocessing, model training, evaluation, and deployment.

---

## 📌 Project Overview

Student Performance Tracker is designed to help educators and students estimate academic performance using machine learning.

The application takes inputs such as:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

and predicts the **Mathematics Score** of the student.

---

## ✨ Features

* End-to-End Machine Learning Pipeline
* Data Ingestion Module
* Data Transformation Pipeline
* Model Training and Evaluation
* Exception Handling and Logging
* Web Application Interface
* Modular Code Structure
* Easy Deployment

---

## 🏗️ Project Architecture

```text
Student-Performance-Tracker
│
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── raw.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── ModelTraining.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

# 📊 Dataset Information

The dataset contains information about students and their academic background.

### Input Features

| Feature                     | Description                    |
| --------------------------- | ------------------------------ |
| gender                      | Student gender                 |
| race_ethnicity              | Ethnicity group                |
| parental_level_of_education | Parent's education             |
| lunch                       | Standard or free/reduced lunch |
| test_preparation_course     | Completed or none              |
| reading_score               | Reading marks                  |
| writing_score               | Writing marks                  |

### Target Variable

```text
math_score
```

The model predicts the mathematics score.

---

# ⚙️ Machine Learning Workflow

### 1. Data Ingestion

* Read dataset from CSV.
* Split into training and testing sets.
* Save raw, train and test datasets.

---

### 2. Data Transformation

Preprocessing steps:

#### Numerical Features

* Reading Score
* Writing Score

Transformation:

* Standard Scaling

#### Categorical Features

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course

Transformation:

* Missing Value Imputation
* One Hot Encoding

---

### 3. Model Training

The following algorithms can be trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* AdaBoost Regressor
* CatBoost Regressor

Evaluation Metric:

```text
R² Score
```

The best-performing model is saved as:

```text
model.pkl
```

---

# 🧠 Technologies Used

### Programming Language

* Python

### Libraries

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* xgboost
* catboost
* dill

### Web Framework

* Flask

### Deployment

* Render / Railway / Docker

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/student-performance-tracker.git
```

Move to project directory:

```bash
cd student-performance-tracker
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Run Flask app:

```bash
python app.py
```

or

```bash
flask run
```

Open browser:

```text
http://localhost:5000
```

---

# 📈 Model Training

To train the model:

```bash
python src/components/data_ingestion.py
```

or

```bash
python src/pipeline/train_pipeline.py
```

Artifacts generated:

```text
artifacts/

├── raw.csv
├── train.csv
├── test.csv
├── model.pkl
└── preprocessor.pkl
```

---

# 🖥️ User Interface

The web application allows users to:

1. Enter student details.
2. Submit the form.
3. View predicted mathematics score instantly.

Example:

```text
Gender: Female

Reading Score: 75

Writing Score: 80

Prediction:

Mathematics Score = 78.5
```

---

# 📊 Evaluation Metrics

The following metrics can be used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

# 🔥 Future Improvements

* Student performance dashboard
* Authentication system
* Database integration
* Multiple subject prediction
* Real-time analytics
* Performance visualization charts
* Recommendation system for weak subjects
* Attendance tracking
* Student ranking system

---

# 💡 Learning Outcomes

This project demonstrates:

* End-to-End Machine Learning Pipeline
* Feature Engineering
* Data Preprocessing
* Model Evaluation
* Flask Application Development
* Exception Handling
* Logging
* Modular Coding Structure
* Model Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Your Name**

* Machine Learning Enthusiast
* Data Science Intern
* Aspiring AI Engineer

If you found this project useful, give it a ⭐ on GitHub.
