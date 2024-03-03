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

month = ['January','February','March','April','May','June','July','August','September','October','November','December']
for col in aq_df.columns:
    if aq_df[col].dtype == 'month':
        aq_df[col] = aq_df[col].astype('category')

aq_df['month'] = pd.Categorical(aq_df['month'], categories=month, ordered=True)

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

# group polutions by hour
def polution_by_hour():
    polusi_per_hour = aq_df.groupby(['hour'], as_index=False).agg({'PM2.5':'mean','PM10':'mean'})
    return polusi_per_hour

# group polutions by day
def polution_by_day():
    polusi_per_day = aq_df.groupby(['day'], as_index=False).agg({'PM2.5':'mean','PM10':'mean'})
    return polusi_per_day

# group polusi by month
def polution_by_month():
    polusi_per_bulan = aq_df.groupby(['month'], as_index=False).agg({'PM2.5':'mean','PM10':'mean'})
    return polusi_per_bulan

# group polusi by tahun
def polution_by_year():
    polusi_per_year = aq_df.groupby(['year'], as_index=False).agg({'PM2.5':'mean','PM10':'mean'})
    return polusi_per_year


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
        ax.set_title('Hourly Temprature')

        # Display the plot in Streamlit
        st.pyplot(fig)
        st.write("Berdasarkan pengamatan dari tabel, pada siang hari bisa tembus 18 derajat celcius yang mungkin disebabkan oleh kegiatan manusia dan kegiatan bangun membangun")


    with tab2:
        st.header('Daily Temprature')
        fig, ax = plt.subplots()
        data2 =  temp_by_day()

        ax.plot(data2['day'], data2['Temprature'])
        ax.set_xlabel('Days')
        ax.set_ylabel('Temprature')
        ax.set_title('Daily Temprature')

        st.pyplot(fig)
        st.write("dari tabel diatas bisa disimpulkan suhu tertinggi ada di hari Rabu dan Jum'at dan suhu ter-rendah dicapai di hari Sabtu, pada hari sabtu saya menspekulasi masyarakat libur dan berdiam dirumah semua sehingga tidak ada aktivitas yang bisa meningkatkan polusi")

    with tab3:
        st.header('Monthly Temprature')
        fig, ax = plt.subplots()
        data3 = temp_by_month()

        ax.plot(data3['month'], data3['Temprature'])
        ax.set_xlabel('Months')
        ax.set_ylabel('Temprature')
        ax.set_title('Monthly Temprature')

        st.pyplot(fig)
        st.write("Berdasarkan tabel diatas, bisa disimpulkan bahwa bulan juli merupakan musim panas, dan wajar saja untuk mencapai suhu >25 derajat celcius.")

    with tab4:
        st.header('Yearly Temprature')
        fig, ax = plt.subplots()
        data4 = temp_by_year()

        ax.plot(data4['year'],data4['Temprature'])
        ax.set_xlabel('Years')
        ax.set_ylabel('Temprature')
        ax.set_title('Yearly Temprature')

        st.pyplot(fig)
        st.write("Berdasarkan tabel diatas, semenjak tahun 2013 suhu menurut 2 derajat dan stabil pada 14 derajat, dan tahun 2017 tidak dihitung karena datanya hanya sampai bulan februari, dan tidak cukup untuk memasukkan rata - ratanya ")
    
    st.text("")
    st.header("Hubungan Polusi PM2.5 dan PM10 pada waktu waktu tertentu")
    
    perjam, perhari, perbulan, pertahun = st.tabs(['Per Hour','Per Day','Per  Month', 'Per Year'])

    with perjam:
        st.header('Hourly Pollution')
        fig, ax = plt.subplots()
        
        ax.plot(polution_by_hour()['hour'], polution_by_hour()['PM2.5'], label='PM2.5')
        ax.plot(polution_by_hour()['hour'], polution_by_hour()['PM10'], label='PM10')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Pollutions (PM2.5 & PM10)')
        ax.set_title("Hourly Pollution")
        ax.legend()
        
        st.pyplot(fig)
        st.write("Dari tabel diatas, bisa disimpulkan bahwa pada jam tertentu dimana pada jam tertentu polusi PM2.5 dan PM10 meningkat, hal ini terjadi karena pabrik mulai bekerja dan tidak ingin mengganggu cuaca pada saat orang beraktivitas di luar.")

    with perhari:
        st.header('Daily Pollution')
        fig, ax = plt.subplots()

        ax.plot(polution_by_day()['day'], polution_by_day()['PM2.5'], label='PM2.5')
        ax.plot(polution_by_day()['day'], polution_by_day()['PM10'], label='PM10')
        ax.set_xlabel('Daily')
        ax.set_ylabel('Pollutions (PM2.5 & PM10)')
        ax.set_title('Daily Pollution')
        ax.legend()

        st.pyplot(fig)
        st.write("dari tabel diatas bisa disimpulkan bahwa polusi paling banyak ada di hari Kamis, Sabtu, Minggu, Senin untuk polusinya paling banyak adalah PM10 yang merupakan partikel yang berdiameter 10 Milimeter atau kurang, contoh dari asap industri, tempat pembangunan, tempat pembuangan akhir dan lainnya.")

        

main()