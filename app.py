import streamlit as st
import joblib
import numpy as np


st.title("Salary Prediction App")

st.divider()

st.write("This app empowers you to estimate employee salaries based on role performance and tenure—instantly and interactively.")

years = st.number_input("Enter the years at company." , value= 1 , step= 1 , min_value= 0)

jobrate = st.number_input("Enter the job rate." , value= 3.5, step= 0.5, min_value= 0.0 )


X = [years,jobrate]

model = joblib.load("linearmodel.pkl")


st.divider()

predict = st.button("Press The Button For Salary Prediction")

st.divider()

if predict :

    st.balloons()
    
    X1 = np.array([X])

    prediction = model.predict(X1)[0]

    st.write(f"Salary Prediction is {prediction:.2f}")


else :

    "Please Press The Button For App to Make The Prediction."



