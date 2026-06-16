# 🚀 AutoEDA Pro

## 📌 Overview

AutoEDA Pro is a production-level Automated Exploratory Data Analysis (EDA) framework built using Python. It automates the complete data analysis pipeline including data loading, validation, cleaning, statistical analysis, visualization, feature engineering, and automated report generation.

The project follows a modular Object-Oriented Programming (OOP) architecture and provides a Streamlit dashboard for interactive data exploration.

---

# ✨ Features

## 📂 Data Loading
- Load CSV datasets
- Dataset information extraction
- Efficient data handling

## 🔍 Data Validation
- Missing value analysis
- Duplicate detection
- Data type checking
- Unique value analysis
- Data quality score calculation

## 🧹 Data Cleaning
- Automatic missing value handling
- Duplicate removal
- Text standardization
- Outlier detection using IQR method

## 📊 Exploratory Data Analysis
- Descriptive statistics
- Numerical analysis
- Correlation analysis
- Categorical analysis
- Automatic insights generation

## 📈 Visualization
- Histograms
- Box plots
- Correlation heatmaps
- Scatter plots
- Interactive Plotly charts

## ⚙️ Feature Engineering
- Label Encoding
- Feature Scaling
- Date feature extraction

## 📝 Automated Reporting
- Dataset summary
- Statistical reports
- Feature information reports

## 🌐 Streamlit Dashboard
- CSV upload
- Dataset preview
- Missing value analysis
- Interactive visualizations

---

# 🏗️ Project Architecture

```
AutoEDA-Pro
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── validator.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   ├── feature_engineering.py
│   ├── report_generator.py
│   └── pipeline.py
│
├── tests/
│   ├── test_loader.py
│   └── test_cleaner.py
│
├── data/
├── reports/
├── logs/
├── requirements.txt
├── README.md
└── version.py
```

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- Streamlit
- PyYAML

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SurajKumar1425/AutoEDA-Pro.git
```

### Go to Project Folder

```bash
cd AutoEDA-Pro
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🔄 AutoEDA Workflow

```
CSV Dataset
     |
     ↓
DataLoader
     |
     ↓
DataValidator
     |
     ↓
DataCleaner
     |
     ↓
EDAAnalyzer
     |
     ↓
Visualizer
     |
     ↓
FeatureEngineer
     |
     ↓
ReportGenerator
     |
     ↓
Final EDA Report
```

---

# 🧪 Running Tests

```bash
pytest tests/
```

---

# 🚀 Future Improvements

- AI-powered data insights
- SQL database integration
- PDF & HTML report generation
- Cloud deployment
- CI/CD pipeline
- Docker support

---

# 📈 Skills Demonstrated

- Python Programming
- Object-Oriented Programming (OOP)
- Data Analysis with Pandas
- Data Cleaning
- Statistical Analysis
- Data Visualization
- Feature Engineering
- Streamlit App Development
- Software Engineering Practices
- Git & GitHub

---

# 👨‍💻 Author

**Suraj Kumar**

Data Science & Machine Learning Enthusiast

---

# ⭐ Support

If you found this project useful, please give this repository a star ⭐ on GitHub.
