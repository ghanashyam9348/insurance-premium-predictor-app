# 🚑 health-insurance-premium-predictor-app

This project is a **Machine Learning-based web application** that predicts the estimated **health insurance premium** for an individual based on personal and medical information. The app is built using **Streamlit** for an interactive UI and leverages **scikit-learn** for ML modeling.

---

## 🔗 Demo

👉 Try the live app here:   
[**🏥 Health Insurance Premium Estimator – Streamlit App**](https://ml-health-insurance-premium-predictor--1.streamlit.app)

---

## 🔍 Overview

The project demonstrates a complete end-to-end ML pipeline, including:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training and Selection
- Model Evaluation and Fine-Tuning
- Deployment via Streamlit UI

---

## 📁 Project Structure

```
insurance-premium-predictor-app/
│
├── .devcontainer/
│   └── devcontainer.json           # Dev container configuration for GitHub Codespaces
│
├── artifacts/                       # Trained models and preprocessors
│   ├── model_rest.joblib           # ML model for age > 25
│   ├── model_young.joblib          # ML model for age <= 25
│   ├── scaler_rest.joblib          # Feature scaler for age > 25
│   └── scaler_young.joblib         # Feature scaler for age <= 25
│
├── . gitignore                       # Git ignore file
├── LICENSE                          # Apache 2.0 License
├── README.md                        # Project documentation
├── main.py                          # Streamlit web application (UI)
├── prediction_helper. py            # Core prediction logic and model loading
└── requirements.txt                # Python dependencies
```

---

## 🛠 Technologies Used

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Joblib** (for model persistence)
- **Streamlit** (for interactive web UI)
- **Git & GitHub**

---

## 📊 Features

- Predicts health insurance premium based on: 
  - Age, Income, Dependents
  - Region, Employment, Marital Status
  - BMI Category, Smoking Habits
  - Medical History & Genetic Risk
- Dynamically selects different ML models based on age groups
- Real-time prediction via Streamlit UI
- Clean, user-friendly form layout

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ghanashyam9348/insurance-premium-predictor-app.git
   cd insurance-premium-predictor-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

---

## 📝 Usage

1. Fill in the form with your personal and medical information
2. Click the **"Predict Premium"** button
3. View your estimated annual health insurance premium

---

## 🤖 Model Details

- **Two separate models** are trained for different age groups:
  - **Young model** (age ≤ 25): Optimized for younger demographics
  - **Rest model** (age > 25): Optimized for older demographics
- Models are saved using **joblib** for efficient loading
- Features are scaled using **StandardScaler** before prediction

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ghanashyam**  
GitHub: [@ghanashyam9348](https://github.com/ghanashyam9348)

---

## 🙏 Acknowledgments

- Built with ❤️ using Python and Streamlit
- Deployed on Streamlit Community Cloud

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!   
Feel free to check the [issues page](https://github.com/ghanashyam9348/insurance-premium-predictor-app/issues).

---

## ⭐ Show your support

Give a ⭐️ if this project helped you! 
