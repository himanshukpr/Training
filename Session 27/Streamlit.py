import streamlit as st

st.title('BMI Calculator')


st.columns(2)

col1, col2 = st.columns(2) # it will return number of columns as mentioned

with col1:
    name = st.text_input('Enter your name: ')
    height = st.number_input('Enter you height (in m): ')
    weight = st.number_input('Enter you weight (in kg): ')


with col2:
    if height > 0 and weight > 0:
        height = height / 100

        bmi = weight / height  ** 2

        st.metric(label='Your BMI', value=bmi)

        if bmi < 18.5:
            st.warning('You are Underweight')
        elif bmi > 18.5 and bmi < 24.9:
            st.success('You are healthy with ideal weight')
        elif bmi>25 and bmi< 29.9:
            st.error('you are Overweight')
        else:
            st.error( 'You are Obese')
    
