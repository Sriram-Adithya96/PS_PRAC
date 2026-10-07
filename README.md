# Machine Learning Prediction System

A machine learning project implementing one **Regression** model and one
**Classification** model, with FastAPI backends and a frontend for
making predictions.

## 📌 Project Overview

This project demonstrates how trained Machine Learning models can be
integrated into a complete application using:

-   Machine Learning models
-   Python
-   FastAPI
-   REST APIs
-   HTML, CSS and JavaScript
-   Frontend-Backend integration

The project contains:

1.  **Linear Regression** -- Regression
2.  **Decision Tree Classifier** -- Classification

------------------------------------------------------------------------

# 🤖 Machine Learning Models

## 1. Linear Regression

Linear Regression is used to predict a continuous numerical value.

### Dataset

**Housing Dataset**

### Algorithm

Linear Regression

### Evaluation Metrics

-   Mean Absolute Error (MAE)
-   Mean Squared Error (MSE)
-   Root Mean Squared Error (RMSE)
-   R² Score
-   Cross-Validation

### Model

The trained model is saved using **Joblib** and stored in:

``` text
linear/model/house_price_model.pkl
```

------------------------------------------------------------------------

## 2. Decision Tree Classifier

Decision Tree is used to solve classification problems.

### Dataset

**Mushroom Dataset**

### Algorithm

Decision Tree Classifier

### Criteria Used

-   Gini Index
-   Entropy

### Evaluation

-   Accuracy
-   Cross-Validation
-   Feature Importance
-   Hyperparameter Tuning

### Model

The trained model is saved using Joblib and stored in:

``` text
decision/model/mushroom_model.pkl
```

------------------------------------------------------------------------

# 🛠️ Technologies Used

## Machine Learning

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Joblib
-   Jupyter Notebook

## Backend

-   FastAPI
-   Uvicorn
-   REST API

## Frontend

-   HTML
-   CSS
-   JavaScript

------------------------------------------------------------------------

# 📂 Project Structure

``` text
PS_PRAC/
│
├── linear/
│   ├── backend/
│   │   └── main.py
│   ├── data/
│   │   └── Housing.csv
│   ├── model/
│   │   └── house_price_model.pkl
│   ├── train.py
│   ├── requirements.txt
│   └── .gitignore
│
├── decision/
│   ├── backend/
│   │   └── main.py
│   ├── data/
│   │   └── mushrooms.csv
│   ├── model/
│   │   └── mushroom_model.pkl
│   └── train.ipynb
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── .gitignore
```

------------------------------------------------------------------------

# 🔄 System Architecture

The application works as follows:

``` text
                    USER
                      │
                      ▼
              HTML/CSS/JavaScript
                  FRONTEND
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       REST API :8000    REST API :8001
             │                 │
             ▼                 ▼
       Linear Regression   Decision Tree
          FastAPI             FastAPI
             │                 │
             ▼                 ▼
      house_price_model   mushroom_model
             │                 │
             └────────┬────────┘
                      │
                      ▼
                  PREDICTION
                      │
                      ▼
                  FRONTEND
```

------------------------------------------------------------------------

# ⚙️ Setup and Installation

## 1. Clone the Repository

``` bash
git clone https://github.com/Sriram-Adithya96/PS_PRAC.git
```

Move into the project directory:

``` bash
cd PS_PRAC
```

------------------------------------------------------------------------

# 🐍 2. Create a Python Virtual Environment

Creating a virtual environment is recommended.

``` bash
python -m venv venv
```

### Windows

Activate the environment:

``` bash
venv\Scripts\activate
```

------------------------------------------------------------------------

# 📦 3. Install Dependencies

Install the required Python packages:

``` bash
pip install -r linear/requirements.txt
```

The main dependencies include:

``` text
fastapi
uvicorn
pandas
numpy
scikit-learn
joblib
```

------------------------------------------------------------------------

# 🚀 Running the Project

The project uses **two separate FastAPI backends**.

Both backends should be running at the same time.

You will need **two terminals**.

------------------------------------------------------------------------

## 1️⃣ Run Linear Regression Backend

Open Terminal 1.

Go to the Linear Regression folder:

``` bash
cd linear
```

Start the FastAPI server:

``` bash
uvicorn main:app --app-dir backend --reload --port 8000
```

The server will start at:

``` text
http://127.0.0.1:8000
```

You should see:

``` text
Uvicorn running on http://127.0.0.1:8000
```

------------------------------------------------------------------------

## 2️⃣ Run Decision Tree Backend

Open another terminal.

Go to the Decision Tree folder:

``` bash
cd decision
```

Start the FastAPI server:

``` bash
uvicorn main:app --app-dir backend --reload --port 8001
```

The server will start at:

``` text
http://127.0.0.1:8001
```

You should see:

``` text
Uvicorn running on http://127.0.0.1:8001
```

------------------------------------------------------------------------

# 🌐 3️⃣ Run the Frontend

The frontend is built using:

-   HTML
-   CSS
-   JavaScript

Go to:

``` text
frontend/
```

Open:

``` text
frontend/index.html
```

in a web browser.

You can also use the **Live Server extension in VS Code**.

### Using Live Server

1.  Open `frontend/index.html`
2.  Right-click the file
3.  Select **Open with Live Server**
4.  The frontend will open in your browser

The frontend communicates with:

``` text
Linear Regression API
http://127.0.0.1:8000
```

and:

``` text
Decision Tree API
http://127.0.0.1:8001
```

------------------------------------------------------------------------

# 🔌 API Endpoints

## Linear Regression API

Base URL:

``` text
http://127.0.0.1:8000
```

Prediction endpoint:

``` text
POST /predict
```

The frontend sends the required housing features to the backend.

The backend loads the trained Linear Regression model and returns the
predicted house price.

------------------------------------------------------------------------

## Decision Tree API

Base URL:

``` text
http://127.0.0.1:8001
```

Prediction endpoint:

``` text
POST /predict
```

The frontend sends the required mushroom features to the backend.

The backend loads the trained Decision Tree model and returns the
predicted class.

------------------------------------------------------------------------

# 🔗 Frontend-Backend Integration

The frontend uses JavaScript `fetch()` to communicate with the FastAPI
servers.

The basic workflow is:

``` text
User enters input
       ↓
JavaScript collects input
       ↓
fetch() sends POST request
       ↓
FastAPI receives input
       ↓
Trained ML model makes prediction
       ↓
FastAPI returns prediction
       ↓
JavaScript receives response
       ↓
Prediction displayed on webpage
```

This allows the trained Machine Learning models to be used through a web
interface.

------------------------------------------------------------------------

# 🧠 Machine Learning Workflow

The general workflow followed in this project is:

``` text
Dataset
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Cross-Validation
   ↓
Hyperparameter Tuning
   ↓
Save Trained Model
   ↓
Load Model in FastAPI
   ↓
Make Predictions
```

------------------------------------------------------------------------

# 📊 Concepts Covered

## Regression

-   Linear Regression
-   Train-Test Split
-   Data Preprocessing
-   MAE
-   MSE
-   RMSE
-   R² Score
-   Cross-Validation

## Classification

-   Decision Trees
-   Gini Index
-   Entropy
-   Accuracy
-   Feature Importance
-   Cross-Validation
-   Hyperparameter Tuning

## Integration

-   Model Serialization using Joblib
-   FastAPI
-   REST APIs
-   POST Requests
-   Frontend-Backend Integration
-   JSON Data
-   JavaScript `fetch()`

------------------------------------------------------------------------

# 🎯 Purpose of the Project

The purpose of this project is to understand the complete process of
building a Machine Learning application:

1.  Train a Machine Learning model.
2.  Evaluate the model.
3.  Save the trained model.
4.  Create a FastAPI backend.
5.  Load the trained model in the backend.
6.  Create a frontend interface.
7.  Connect the frontend with the backend using REST APIs.
8.  Display the prediction to the user.

------------------------------------------------------------------------

# ▶️ Quick Start

After cloning the repository:

### Terminal 1 -- Linear Regression

``` bash
cd PS_PRAC/linear
uvicorn main:app --app-dir backend --reload --port 8000
```

### Terminal 2 -- Decision Tree

``` bash
cd PS_PRAC/decision
uvicorn main:app --app-dir backend --reload --port 8001
```

### Browser -- Frontend

Open:

``` text
PS_PRAC/frontend/index.html
```

or use VS Code Live Server.

Make sure **both FastAPI servers are running before using the prediction
features**.

------------------------------------------------------------------------

# 👨‍💻 Author

**Adithya Sriram**

GitHub: https://github.com/Sriram-Adithya96

------------------------------------------------------------------------

## 📌 Note

This project was developed for learning and demonstrating the
integration of Machine Learning models with backend APIs and a frontend
application.
