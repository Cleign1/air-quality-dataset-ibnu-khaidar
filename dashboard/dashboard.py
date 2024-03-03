# import yang diperlukan package
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# import dataset
aq_df = pd.read_csv("data\output.csv", delimiter=',')

# ordering days by default days monday to sunday
hari = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for col in aq_df.columns:
    if aq_df[col].dtype == 'day':
        aq_df[col] = aq_df[col].astype('category')

aq_df['day'] = pd.Categorical(aq_df['day'], categories=hari, ordered=True)

# group temprature by hour
def temp_by_hour():
    temps_per_hour = aq_df.groupby('hour', as_index=False).agg({'Temprature':'mean'})
    return temps_per_hour

# group temprature by day
def temp_by_day():
    temps_per_day = aq_df.groupby('day',as_index=False).agg({'Temprature':'mean'})
    return temps_per_day

# group temprature by month
def temp_by_month():
    temps_per_month = aq_df.groupby('month', as_index=False).agg({'Temprature':'mean'})
    return temps_per_month

# group temprature by year
def temp_by_year():
    temprature_per_year = aq_df.groupby('year', as_index=False).agg({'Temprature':'mean'})
    return temprature_per_year


def main():
    st.title('Kualitas Udara')

    st.text('Standart Air Quality index')
    st.image('Screenshot 2024-03-03 141028.png')
    st.text("")
    st.text('Perbedaan Suhu Per jam')

    tab1, tab2, tab3, tab4 = st.tabs(['By Hour','By Day', 'By Month', 'By Year'])

    with tab1:
        st.header('Hourly Temprature')
        fig, ax = plt.subplots()
        data1 = temp_by_hour()

        # Plot the data as a line chart
        ax.plot(data1['hour'], data1['Temprature'])
        ax.set_xlabel('Hour')
        ax.set_ylabel('Temperature')
        ax.set_title('Temperature by Hour')

        # Display the plot in Streamlit
        st.pyplot(fig)

    with tab2:
        st.header('Daily Temprature')
        fig, ax = plt.subplots()
        data2 =  temp_by_day()

        ax.plot(data2['day'], data2['Temprature'])
        ax.set_xlabel('Days')
        ax.set_ylabel('Temprature')
        ax.set_title('Temprature by  Days')

        st.pyplot(fig)


main()