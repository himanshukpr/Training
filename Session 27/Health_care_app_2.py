import streamlit as st

st.set_page_config(page_title='Health Calculator')
st.title('All In One Health Care')

st.sidebar.header('Enter you Details')
name = st.sidebar.text_input('Enter your name: ')
name = name.capitalize()
age = st.sidebar.number_input('Enter your Age: ', min_value=10,max_value=100)
gender = st.sidebar.radio('Gender: ',['Male','Female'])
height = st.sidebar.number_input('Enter you height (in cm): ')
weight = st.sidebar.number_input('Enter you weight (in kg): ')

height = height / 100

tab_list = st.tabs(['BMI','BMR','Body Fat Percentage','Water Intake','Ideal Weight'])

bmi_tab, bmr_tab, body_fat_tab, water_tab, ideal_tab = tab_list



with bmi_tab:
    st.subheader('Body Mass Index (BMI)')
    if height > 0 and weight > 0:

        bmi = weight / (height  ** 2)

        st.metric(label='Your BMI', value=bmi)

        if bmi < 18.5:
            st.warning('Hi {}, You are Underweight'.format(name))
        elif bmi > 18.5 and bmi < 24.9:
            st.success('Hi {}, You are healthy with ideal weight'.format(name))
        elif bmi>25 and bmi< 29.9:
            st.error('Hi {}, You are Overweight'.format(name))
        else:
            st.error( 'Hi {}, You are Obese'.format(name))
    
with bmr_tab:
    st.subheader('Basal Metabolic Rate (BMR)')
    if height > 0 and weight > 0 and age:
        if gender == 'Male':
            bmr = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))


        elif gender == 'Female':
            bmr = round(447.593 + (9.247 * weight ) + (3.098 * height) - (4.330 * age))

        st.metric(label='Your BMR',value=bmr)

with body_fat_tab:
    st.subheader('Body Fat Percentage')
    if height > 0 and weight > 0:

        bmi = weight / (height  ** 2)

        if gender=='Male':
            body_fat = 1.20 * bmi + 0.23 * age - 10.8 * 1 - 5.4
            st.metric(label='Your body fat is: ',value=body_fat)

            if body_fat < 6:
                st.warning('Below essential fat (Dangerous)')
            elif body_fat > 6 and body_fat < 13:
                st.success('Athlete')
            elif body_fat > 14 and body_fat < 17:
                st.success('Fitness')
            elif body_fat > 18 and body_fat < 24:
                st.success('Average')
            else:
                st.error('Above average')


        elif gender == 'Female':
            body_fat = 1.20 * bmi + 0.23 * age - 10.8 * 0 - 5.4
            st.metric(label='Your body fat is: ',value=body_fat)

            if body_fat < 14:
                st.warning('Below essential fat (Dangerous)')
            elif body_fat > 14 and body_fat < 20:
                st.success('Athlete')
            elif body_fat > 21 and body_fat < 24:
                st.success('Fitness')
            elif body_fat > 25 and body_fat < 31:
                st.success('Average')
            else:
                st.error('Above average')


with water_tab:
    st.subheader('Water Intake')
    if height > 0 and weight > 0:

        water_intake  = weight * 0.033
        st.metric(label='Water intake should be ',value=water_intake)



with ideal_tab:
    st.subheader('Ideal Weight')
    if height > 0 and weight > 0:
        height_in = (height*100) / 2.54
        if gender == 'Male':
            ideal_weight = 50 + 2.3 * (height_in  - 60)
        else:
            ideal_weight = 45.5 + 2.3 * (height_in  - 60)

        st.metric(label='Your ideal weight is: ',value=ideal_weight)
