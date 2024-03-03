# import yang diperlukan package
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# import dataset
aq_df = pd.read_csv("output.csv", delimiter=',')

# group temprature by hour






def main():
    st.title('Kualitas Udara')

    st.text('Standart Air Quality index')
    st.image('Screenshot 2024-03-03 141028.png')


main()