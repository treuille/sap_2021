import streamlit as st
import pandas as pd

def run_home(data):
    st.header(":house_with_garden: Homepage")
    st.write("""Lets look at the data.""")
    display_data = st.empty()

    # slider_value = st.slider("pick a number", 0, len(data), (0,500), 500)
    # st.write(slider_value,slider_value[0],slider_value[1])

    #display_data.dataframe(data.loc[slider_value[0]:slider_value[1]])
    display_data.dataframe(data)

    st.subheader("Features of the data")
    st.write("""
* **enrollee_id:** Unique ID for candidate
    * Presumably each one of these will be different (no repeats) :crossed_fingers:
* **city:** City code
    * Not particularly useful for us
* **city_ development _index:** Developement index of the city (scaled)
    * The City Developement Index measuers the level of development in a city based
    on a number of metics and can help easily compare cities.
    [Read more about it here](https://en.wikipedia.org/wiki/City_development_index)
* **gender:** Gender of candidate
    * Includes: Male, Female and Other
* **relevent_experience:** Relevant experience of candidate
    * Consists of 2 categories: Has relevent experience	and No relevent experience
* **enrolled_university:** Type of University course enrolled if any
    * Consists of 3 categories: no_enrollment, Full time course, and Part time course
* **education_level:** Education level of candidate
    * Consists of 5 categories: Primary School, High School, Graduate, Masters, and Phd
* **major_discipline:** Education major discipline of candidate
    * Consists of 5 categories: STEM, Humanities, Business Degree, Arts and Other
* **experience:** Candidate total experience in years
    * A number representing the years of work experience
* **company_size:** No of employees in current employer's company
    * Consists of categories for the sizes of companies
* **company_type:** Type of current employer
    * Consists of 5 categories: Early Stage Startup, Funded Startup, Pvt Ltd, Public Sector, and NGO
* **lastnewjob:** Difference in years between previous job and current job
    * Consists of 5 categories: 1, 2, 4, >4, and never
* **training_hours:** training hours completed
    * Consists of numbers of hours that person spent training
* **target:** If your going to run some machine learning methods, this is the intended column for predictions
    * Consists of 2 categories: 0 – Not looking for job change, 1 – Looking for a job change
    """)
    return
