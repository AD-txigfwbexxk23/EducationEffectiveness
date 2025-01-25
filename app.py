import streamlit as st
from Computation import main


def main():
    
    if st.session_state.query is None:
        st.session_state.query = ""
        
    
    st.title("Education Effectiveness")
    st.write("""
             This is a web app to predict the effectiveness of education, using quantitatve metrics. 
             The goal of this project is to create a model that, based on pillars determined from existing research can accuratly rank the effectiveness of education in different organizations.
             We hope that this model can be used to help organizations improve their education programs and to help investors make informed decisions.
             
             """)    
    st.sidebar.title("User Input")
    st.sidebar.text("Please enter the following information:")
    st.sidebar.text_input(
            "Student-teacher Ratio:", value=st.session_state.query, key="query"
        )   
    st.sidebar.text_input(
            "Frequency of Sessions:", value=st.session_state.query, key="query"
        ) 
    st.sidebar.text_input(
            "PLACEHOLDER: ", value=st.session_state.query, key="query"
    ) 
    st.sidebar.button("Submit") 
    
    
    
    
    
#Running the program
main()
