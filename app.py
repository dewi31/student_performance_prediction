import streamlit as st
import joblib

model = joblib.load('my_model.joblib')
st.title("Student Dropout Prediction")

with st.form(key='data_form'):
    
    scholar_holder = st.number_input("Scholarship holder (1 – yes 0 – no)", min_value=0, max_value=1)
    fee = st.number_input("Tuition fees up to date (1 – yes 0 – no)", min_value=0, max_value=1)
    first_sem_approve = st.number_input("Curricular units 1st sem (approved)", min_value=0, max_value=25)
    first_sem_grade = st.number_input("Curricular units 1st sem (grade)", min_value=0.0, max_value=20.0)
    sec_sem_approve = st.number_input("Curricular units 2nd sem (approved)", min_value=0, max_value=25)
    sec_sem_grade = st.number_input("Curricular units 2nd sem (grade)", min_value=0.0, max_value=20.0)
    
    submit_button = st.form_submit_button(label='Predict')


    if submit_button:
        input_data = [[scholar_holder, fee, first_sem_approve, first_sem_grade, sec_sem_approve, sec_sem_grade]]  
        
        prediction = model.predict(input_data)
        
        if prediction == 0:
            st.error("Dropout")
        elif prediction == 1:
            st.info("Enrolled")
        else:
            st.success("Graduate")
    