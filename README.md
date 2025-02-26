# Titanic-Survival-Prediction  

## 📄 **Problem Statement**  
The objective of this project is to predict whether a passenger survived or not based on features such as class, sex, age, fare, and other passenger details. The dataset used for this project is the famous Titanic dataset from Kaggle.

---

## 📊 **Dataset Description**  
The Titanic dataset contains the following key features:

| **Feature Name** | **Description** |
|-----------------|-----------------|
| `PassengerId` | Unique identifier for each passenger |
| `Survived`    | Survival (0 = No, 1 = Yes) |
| `Pclass`      | Passenger class (1 = First, 2 = Second, 3 = Third) |
| `Name`        | Name of the passenger |
| `Sex`         | Gender (male or female) |
| `Age`         | Age of the passenger |
| `SibSp`       | Number of siblings/spouses aboard |
| `Parch`       | Number of parents/children aboard |
| `Ticket`      | Ticket number |
| `Fare`        | Fare paid |
| `Cabin`       | Cabin number |
| `Embarked`    | Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

---

## 🔧 **Steps in the Solution**  

1. **Data Loading:**  
   Imported the Titanic dataset using `pandas`.

2. **Data Cleaning and Preprocessing:**  
   - Handled missing values in `Age`, `Cabin`, and `Embarked`.  
   - Dropped unnecessary columns (`PassengerId`, `Name`, and `Ticket`).  
   - Converted categorical variables (`Sex`, `Embarked`) to numerical using label encoding.

3. **Feature Engineering:** 
   - Bucketed age into categories.  
   - Scaled numerical features using Standard Scaler.

4. **Model Selection and Training:**  
   - Split the dataset into training and testing sets.  
   - Trained multiple machine learning models: 
     - Decision Tree
     - Random Forest
     - Logistic Regression  
   - Evaluated models using accuracy and confusion matrices.

5. **Model Evaluation:**  
   - Achieved a training accuracy of **85%** using Random Forest.  
   - Tested models to determine their generalization ability.

---

## ⚙ **Algorithms Used and Performance**  

| **Algorithm**       | **Training Accuracy** | **Test Accuracy** |
|---------------------|------------------------|------------------|
| Logistic Regression | 78%                    | ---              |
| SMV                 | 65%                    | ---              |
| Random Forest       | 83%                    | 90%              |

---

## 🏃‍♂️ **Instructions on How to Run the Code**

1. **Clone the Repository:**  
   ```bash
   git clone <repository_link>
   cd titanic_project

2. Install Required Libraries:
   ```
    pip install -r requirements.txt

3. Run the Notebook:
Open the Jupyter Notebook:
  ```
    jupyter notebook Titanic Survival Prediction.ipynb

  ```

4. Execution:
Follow the steps in the notebook to preprocess data, train models, and evaluate their performance.

## 🚀 Running the Flask App

This project includes a Flask web application to allow users to enter passenger details and predict survival.

1. Run the Flask App:
```bash
python app.py
```
2. Access the Web Interface:

   Open http://127.0.0.1:5000/ in your browser.

## 🏃‍♂️ Running the Streamlit App
1. Start the Streamlit server:

```bash
streamlit run app.py
```
2. Access the web app: Open http://localhost:8501 in your browser.

## Deployment
To deploy on a cloud platform, you can use Streamlit Cloud or any other cloud platform that supports Streamlit apps.

Push your code to a GitHub repository.

1. Deploy to Streamlit Cloud:

2. Go to Streamlit Cloud.
- Sign in with your GitHub account and deploy the app.
- Now, your application is live!


## 🎯 Future Enhancements

- Improve model accuracy with hyperparameter tuning.

- Add more user-friendly UI elements.
