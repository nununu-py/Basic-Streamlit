import streamlit as st
import pandas as pd
import datetime

st.markdown("""
    <h2 style='text-align: center; color: orange;'>Registration Form</h2> 
    """, unsafe_allow_html=True)
st.caption("Fill All Information Below")

st.markdown("---")

with st.container():

    col1, col2, col3 = st.columns(spec=3, gap="medium")

    with col1:
        col1 = st.selectbox(label="Title", options=[None, "Mr.", "Mrs."])
    with col2:
        col2 = st.text_input(label="First Name")
    with col3:
        col3 = st.text_input(label="Last Name")

    role = st.selectbox(label="What is your role",
                        options=[None, "Intern", "Manager", "Data Analyst", "Accountant",
                                 "Social Media Marketing", "Admin"])

    birth = st.date_input("Add Birth Day", min_value=datetime.date(1990, 1, 1),
                          max_value=datetime.date(2030, 12, 31))

    geneder = st.radio(label="Gender", options=["Male", "Female"])

    home_distance = st.slider(label="Distance from Home to Office (KM)",
                              min_value=1, max_value=100, value=1)
    st.write(f"Your Home-Office Distance : {home_distance} KM")

    submit_button = st.button("SUBMIT")

    if submit_button:

        st.success("Your Data is Success Upload")

        name = f"{col1} {col2} {col3}"
        user_data = {
            "Name": [name],
            "Role": [role],
            "Birth": [birth],
            "Geneder": [geneder],
            "Distace (Km)": [home_distance]
        }

        userdata_df = pd.DataFrame(data=user_data)

        st.dataframe(userdata_df, width=800)

    st.markdown("---")
