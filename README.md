# Credit Risk Assessment Project

## Overview
This project is a web-based application that predicts the likelihood of a user defaulting on a loan. It integrates statistical analysis, predictive modeling, and data visualization to provide insights and actionable recommendations for risk mitigation.

---

## Pre-requisites
Run the following command:
```bash
pip install Flask
```

---

## Running the Program
1. Navigate to the main folder of the project.
2. Execute the following command:
   ```bash
   python project.py runserver --d
   ```

---

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Styling Frameworks:** Bootstrap, Tailwind
- **Data Visualization:** Chart.js

---

## Program Design and Architecture

### Backend
#### **`Model.py`**
- This file contains a class that handles the pre-processing of data for training, trains a decision tree model, processes input data from users, tests the model, and provides the probability of a user defaulting on a loan.
- **Algorithm:**
  - Encodes categorical columns using label encoding.
  - Splits data into training and testing sets.
  - Trains a decision tree classifier.
  - Processes user input and predicts default probabilities.
- **Input:** Dataset (`credit.csv`) and user input.
- **Output:** Default probability.

#### **`DataStats.py`**
- Provides statistical insights and preprocessing for the dataset.
- **Algorithm:**
  - Handles missing data in numerical and categorical columns.
  - Computes descriptive statistics (mean, median, mode, etc.).
  - Aggregates demographic statistics by default status.
  - Generates risk mitigation suggestions.
- **Input:** Dataset or user profile dictionary.
- **Output:** Statistical insights and risk suggestions.

#### **`Chart.py`**
-  Generates bar charts for categorical data distributions, with user-specific values highlighted.
- **Algorithm:**
  - Reads the dataset and identifies categorical columns.
  - Calculates value frequencies and generates chart configurations.
- **Input:** Dataset and optional user input.
- **Output:** List of chart configurations.

#### **`project.py`**
- This is the main script that initializes the Flask application and renders the necessary templates.
- **Algorithm:**
  - Presents a form for user input.
  - Processes user input and computes default risk using `Model.py`.
  - Generates charts and insights using `Chart.py` and `DataStats.py`.
  - Displays results, including predictions and visualizations.
- **Input:** User-provided data and dataset.
- **Output:** Web-based results page.

---

### Frontend
#### **`index.html`**
- This template displays a form for users to input data and allows them to submit the form.
- **Features:**
  - Dropdowns and numeric fields for various loan-related attributes.
  - Responsive design using Bootstrap and Tailwind.
  - Tooltips for user guidance.
- **Output:** Form data submitted to the Flask backend.

#### **`results.html`**
- This template shows the results, indicating whether the user is likely to default on a loan. Dashboards and some statistics will also be displayed
- **Features:**
  - Risk probability, insights, and demographic comparisons.
  - Interactive charts for data visualization.
  - Bootstrap-based design for a professional look.
- **Output:** Risk assessment results and recommendations.

---

## Dataset
- **File:** `credit.csv`
- **Description:** Contains historical financial and demographic data used to train the decision tree model. This CSV file contains the dataset used for training the model.

---
