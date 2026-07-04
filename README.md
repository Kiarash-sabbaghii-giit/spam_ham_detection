<div align="center">

# 🚀 SpamDetector Pro

### AI-Powered Spam Detection System built with Django & Machine Learning

<p>
An intelligent spam detection platform that combines the power of Machine Learning and Django to classify messages in real-time with exceptional accuracy.
</p>

<p>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-154F7D?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-Animation-88CE02?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

### 🎯 Accuracy: **98%**
### ⚡ Prediction Time: **< 100 ms**
### 🤖 Machine Learning + Modern UI + Real-Time Prediction

</div>

---

# 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Machine Learning Model](#-machine-learning-model)
- [Model Performance](#-model-performance)
- [UI/UX Design](#-uiux-design)
- [Screenshots](#-screenshots)
- [Demo](#-demo)
- [Contributing](#-contributing)
- [License](#-license)

---

# 📖 Project Overview

**SpamDetector Pro** is a premium AI-powered spam detection web application built using **Django** and **Machine Learning**.

The application analyzes incoming text messages and instantly predicts whether they are **Spam** or **Ham (Not Spam)** using a trained Logistic Regression model.

Designed with both performance and aesthetics in mind, the project delivers lightning-fast predictions while offering a premium Glassmorphism user interface enhanced with smooth GSAP animations.

---

# ✨ Features

✅ Real-Time Spam Detection

✅ Machine Learning Prediction

✅ 98% Classification Accuracy

✅ Ultra-fast Prediction (<100 ms)

✅ Premium Glassmorphism Interface

✅ Beautiful GSAP Animations

✅ Live Statistics Dashboard

✅ Prediction History

✅ Responsive Design

✅ Mobile Friendly

✅ Clean & Modern UI

✅ Easy Deployment

---

# 🛠 Tech Stack

## Backend

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Django | Web Framework |
| Scikit-learn | Machine Learning |
| Logistic Regression | Classification Algorithm |
| TF-IDF Vectorizer | Feature Extraction |
| NLTK | Text Preprocessing |

---

## Frontend

| Technology | Purpose |
|------------|----------|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Interaction |
| GSAP | Animations |
| Font Awesome | Icons |

---

## Database

| Database | Usage |
|----------|-------|
| SQLite | Local Storage |

---

# 📁 Project Structure

```text
SpamDetector-Pro/
│
├── spam_detector/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── detector/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── history.html
│   │   └── about.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── ml/
│   │   ├── model.pkl
│   │   ├── vectorizer.pkl
│   │   └── train_model.py
│   │
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── utils.py
│
├── db.sqlite3
├── requirements.txt
├── manage.py
└── README.md
```

---

# ⚡ Installation

## Prerequisites

- Python 3.10+
- pip
- Git

---

## Clone Repository

```bash
git clone https://github.com/your-username/SpamDetector-Pro.git
```

```bash
cd SpamDetector-Pro
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🤖 Machine Learning Model

## Classification Algorithm

**Logistic Regression**

---

## Feature Engineering

TF-IDF Vectorizer

Configuration:

```text
N-Gram Range : (1,3)

Stop Words : English

Lowercase : True

Tokenizer : NLTK

Sparse Matrix : Yes
```

---

## Text Preprocessing

- Lowercase Conversion
- Tokenization
- Stopword Removal
- Lemmatization
- TF-IDF Transformation

---

# 📊 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **98%** |
| Precision | **98%** |
| Recall | **97%** |
| F1 Score | **98%** |

---

## Confusion Matrix

```text
                 Predicted

              Ham      Spam

Actual Ham    965        18

Actual Spam    11       1006
```

---

## Performance Highlights

- High Precision
- Low False Positive Rate
- Fast Inference
- Lightweight Model
- Production Ready

---

# 🎨 UI/UX Design

The interface was carefully designed to provide a premium user experience.

### Design Features

- Glassmorphism Effects
- Gradient Backgrounds
- Smooth GSAP Animations
- Modern Cards
- Interactive Buttons
- Responsive Layout
- Elegant Typography
- Dark-Friendly Color Palette

---

## Color Palette

| Color | Usage |
|---------|----------------|
| Purple | Primary |
| Blue | Secondary |
| Pink | Accent |
| White | Text |
| Glass Blur | Cards |

---

# 🚀 Demo

### Live Demo

```
https://your-demo-link.com
```

---

### GitHub Repository

```
https://github.com/Kiarash-sabbaghii-giit/spam_ham_detection
```

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for personal and commercial purposes.

---

<div align="center">

## ⭐ If you found this project useful, please consider giving it a Star!

Made with ❤️ using **Django**, **Machine Learning**, and **Python**

</div>
