import streamlit as st
from Computation import main


def main():
    st.title("Education Effectiveness")
    st.write("""
             This is a web app to predict the effectiveness of education, using quantitatve metrics. 
             The goal of this project is to create a model that, based on pillars determined from existing research can accuratly rank the effectiveness of education in different organizations.
             
             """)
    
    st.sidebar.header("User Input Parameters")
    
    
    
    
    
#Running the program
main()