import streamlit as st
import pickle  # Load the trained model

# Load the trained model
with open("titanic_model.pkl", "rb") as file:
    model = pickle.load(file)

# Mapping for titles
TITLE_MAPPING = {
    "Mr": 0, "Mrs": 1, "Miss": 2, "Master": 3, "Dr": 4, "Rev": 5, 
    "Col": 6, "Major": 7, "Mlle": 8, "Mme": 9, "Sir": 10
}

# Function to make predictions
def predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title, Ticket, Cabin):
    Sex = 1 if Sex == "Male" else 0
    Embarked = {"C": 0, "Q": 1, "S": 2}.get(Embarked, -1)
    Title = TITLE_MAPPING.get(Title, -1)

    features = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title, Ticket, Cabin]]
    prediction = model.predict(features)
    return "Survived" if prediction[0] == 1 else "Did Not Survive"

# Initialize session state variables if not already set
if "predict_toggle" not in st.session_state:
    st.session_state.predict_toggle = False

if "reset_toggle" not in st.session_state:
    st.session_state.reset_toggle = False

# Function to reset prediction toggle **when any feature changes**
def reset_prediction_toggle():
    st.session_state.predict_toggle = False

# Function to reset all inputs to default values
def reset_all():
    st.session_state.Pclass = 3
    st.session_state.Sex = "Male"
    st.session_state.Age = 30
    st.session_state.SibSp = 0
    st.session_state.Parch = 0
    st.session_state.Fare = 50.0
    st.session_state.Embarked = "S"
    st.session_state.Title = "Mr"
    st.session_state.Ticket = 12345
    st.session_state.Cabin = 100
    st.session_state.predict_toggle = False  # Also reset prediction toggle

# Streamlit UI
st.title("Titanic Survival Prediction")

# **Reset All Toggle (turning it on resets all values)**
reset_all_toggle = st.toggle("Reset All to Default", key="reset_toggle")
if reset_all_toggle:
    reset_all()

# Input fields (each with on_change=reset_prediction_toggle)
Pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], key="Pclass", on_change=reset_prediction_toggle)
Sex = st.radio("Sex", ["Male", "Female"], key="Sex", on_change=reset_prediction_toggle)
Age = st.slider("Age", 1, 100, 30, key="Age", on_change=reset_prediction_toggle)
SibSp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0, key="SibSp", on_change=reset_prediction_toggle)
Parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0, key="Parch", on_change=reset_prediction_toggle)
Fare = st.number_input("Fare Paid", 0.0, 500.0, 50.0, key="Fare", on_change=reset_prediction_toggle)
Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"], key="Embarked", on_change=reset_prediction_toggle)
Title = st.selectbox("Title", list(TITLE_MAPPING.keys()), key="Title", on_change=reset_prediction_toggle)
Ticket = st.number_input("Ticket Number", 1, 999999, 12345, key="Ticket", on_change=reset_prediction_toggle)
Cabin = st.number_input("Cabin Number", 1, 9999, 100, key="Cabin", on_change=reset_prediction_toggle)

# Toggle switch for prediction
st.session_state.predict_toggle = st.toggle("Show Prediction", value=st.session_state.predict_toggle)

# Show prediction only when toggle is ON
if st.session_state.predict_toggle:
    result = predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title, Ticket, Cabin)
    st.success(f"Prediction: {result}")


