# Weather Type Classification 🌦️

A machine learning web application built with **Python** and **Streamlit** that predicts weather types based on environmental parameters using multiple classification algorithms.

## 🎯 Project Overview

This project uses synthetic environmental data to classify weather into four categories: **Sunny**, **Rainy**, **Cloudy**, and **Snowy**. The application provides an interactive interface where users can input environmental parameters and get real-time weather predictions.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Multiple ML Models**: Choose from 4 different classification algorithms:
  - 🌲 **Random Forest Classifier** (optimized with max_features=0.2, max_samples=0.5, n_estimators=120)
  - 🌳 **Decision Tree** (optimized with max_depth=4, max_leaf_nodes=5, min_samples_split=50)
  - 📊 **Logistic Regression**
  - 🎯 **Support Vector Machine (SVM)**
- **Real-time Predictions**: Instant weather classification based on user inputs
- **Visual Feedback**: Weather-specific emojis and images for predictions

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **scikit-learn** - Machine learning models and preprocessing
- **pandas** - Data manipulation
- **numpy** - Numerical computations
- **matplotlib & seaborn** - Data visualization

## 📊 Input Parameters

The model accepts the following environmental parameters:

- **Temperature** (°C): -50 to 60
- **Humidity** (%): 0 to 100
- **Wind Speed** (km/h): 0 to 200
- **Precipitation** (%): 0 to 100
- **Atmospheric Pressure** (hPa): 800 to 1100
- **UV Index**: 0 to 11
- **Visibility** (km): 0 to 100
- **Cloud Cover**: partly cloudy, clear, overcast, cloudy
- **Season**: Winter, Spring, Summer, Autumn

## 📁 Project Structure

```
Weather-Type-Classification/
├── data/
│   └── weather_classification_data.csv    # Training dataset
├── environment/
│   ├── requirements.txt                   # Python dependencies
│   └── setup.py                           # Setup configuration
├── notebook/
│   └── eda.ipynb                          # Exploratory Data Analysis
├── src/
│   ├── app.py                             # Main Streamlit application
│   ├── train.py                           # Model training pipeline
│   ├── test.py                            # Prediction and testing
│   └── features/
│       └── build_features.py              # Feature engineering
├── .gitignore
└── README.md
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Maharsh8805/Weather-Type-Classification.git
   cd Weather-Type-Classification
   ```

2. **Install dependencies**
   ```bash
   pip install -r environment/requirements.txt
   ```

## 🎮 Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run src/app.py
   ```

2. **Select a model** from the sidebar:
   - Random Forest Classifier
   - Decision Tree
   - Logistic Regression
   - SVM

3. **Input environmental parameters** using the sidebar controls

4. **Click Submit** to get the weather prediction

## 🤖 Machine Learning Models

### 1. Random Forest Classifier
- **Hyperparameters**: 
  - n_estimators: 120
  - max_features: 0.2
  - max_samples: 0.5
- Best for handling complex, non-linear relationships

### 2. Decision Tree
- **Hyperparameters**:
  - max_depth: 4
  - max_leaf_nodes: 5
  - min_samples_split: 50
- Provides interpretable decision rules

### 3. Logistic Regression
- Default configuration
- Fast and efficient for linear relationships

### 4. Support Vector Machine (SVM)
- Default configuration
- Effective for high-dimensional data

## 📈 Model Pipeline

The application uses a scikit-learn Pipeline that includes:
1. **Preprocessing**: Feature scaling and encoding
2. **Model Training**: Selected algorithm training
3. **Prediction**: Real-time weather classification

## 🎨 Output

The application displays:
- Weather prediction with emoji (☀️ 🌧️ ☁️ ❄️)
- Weather-specific images
- Formatted prediction message

## 📝 Dataset

The project uses a synthetic weather classification dataset containing environmental parameters and corresponding weather types. The dataset is located in `data/weather_classification_data.csv`.

## 👨‍💻 Author

**Lakhankiya Maharsh**

## 📄 License

© 2025 Lakhankiya Maharsh. All Rights Reserved.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This is a synthetic weather classification project for educational and demonstration purposes.