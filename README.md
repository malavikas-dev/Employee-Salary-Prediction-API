# 💼 Employee Salary Prediction Web Application

A Machine Learning web application that predicts an employee's salary based on company, department, work experience, age, annual bonus, and other employee-related features.

The application is built using:

- Python
- Flask
- LightGBM
- Scikit-learn
- HTML
- CSS
- JavaScript

## ✨ Features

- Predict employee salary using a trained LightGBM model.
- User-friendly web interface.
- REST API built using Flask.
- Automatic preprocessing using a saved preprocessing pipeline.
- Fast salary prediction.
- Responsive and easy-to-use design.

## 📁 Project Structure

```text
Employee_Salary_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── LightGBM_model.pkl
│   └── preprocessor.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── Employee_Salary_Prediction.ipynb
```
## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/malavikas-dev/Employee-Salary-Prediction-API.git
```

### Navigate to the project folder

```bash
cd Employee-Salary-Prediction-API
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```
## 🚀 API Endpoints

### Home

**GET /**

Returns:

```json
{
  "message": "Salary Prediction API Running",
  "status": "success"
}
```

---

### Predict Salary

**POST /predict**

Example Request:

```json
{
  "company": "Google",
  "department": "Engineering",
  "age": 30,
  "age_when_joined": 25,
  "years_in_the_company": 5,
  "annual_bonus": 5000,
  "prior_years_experience": 3,
  "full_time": 1,
  "part_time": 0,
  "contractor": 0,
  "age_diff": 5,
  "bonus_per_year": 1000,
  "total_experience": 8,
  "experience_ratio": 1.6,
  "company_department": "Google_Engineering",
  "employment_type": "full_time"
}
```
## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- HTML
- CSS
- JavaScript
## 🔮 Future Improvements

- User authentication
- Model retraining with new datasets
- Better visualizations
- Cloud deployment
- Improved responsive UI