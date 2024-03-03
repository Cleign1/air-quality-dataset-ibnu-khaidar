# import yang diperlukan package
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# import dataset
aq_df = pd.read_csv("data/output.csv", delimiter=',')

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

# rain possibility based on humidity
def rain_pos():
    rain_possibility = aq_df.groupby('Pressure', as_index=False).agg({'RAIN':'max'})
    return rain_possibility

# ozone per day
def ozone_per_day():
    ozone_content = aq_df.groupby('day', as_index=False).agg({'O3':'mean'})
    return ozone_content

# ozone per month
def ozone_per_month():
    ozone_content_per_month = aq_df.groupby('month', as_index=False).agg({'O3':'mean'})
    return ozone_content_per_month

# ozone per year
def ozone_per_year():
    ozone_content_per_year = aq_df.groupby('year', as_index=False).agg({'O3':'mean'})
    return ozone_content_per_year

# gas lain di udara per day
def othergas_perday():
    gas_content_per_day = aq_df.groupby('day', as_index=False).agg({'SO2':'mean','NO2':'mean'})
    return gas_content_per_day

# gas lain di udara per month
def othergas_permonth():
    gas_content_per_month = aq_df.groupby('month', as_index=False).agg({'NO2':'mean','SO2':'mean'})
    return gas_content_per_month

# gas lain di udara per tahun
def othergas_peryear():
    gas_content_per_year = aq_df.groupby('year',as_index=False).agg({'NO2':'mean','SO2':'mean'})
    return gas_content_per_year

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

    with perbulan:
        st.header("Monthly Pollution")
        fig, ax = plt.subplots()

        ax.plot(polution_by_month()['month'], polution_by_month()['PM2.5'], label='PM2.5')
        ax.plot(polution_by_month()['month'], polution_by_month()['PM10'], label='PM10')
        ax.set_xlabel('Monthly')
        ax.set_ylabel('Pollutions (PM2.5 & PM10)')
        ax.set_title('Monthly Pollution')
        ax.legend()

        st.pyplot(fig)
        st.write("Dari Tabel diatas bisa disimpulkan bahwa Polusi PM10 paling tinggi ada di bulan maret dan PM2.5 ada di bulan December ini bisa dipengaruhi banyak faktor yang lain")

    with pertahun:
        st.header('Yearly Pollution')
        fig, ax = plt.subplots()

        ax.plot(polution_by_year()['year'], polution_by_year()['PM2.5'], label='PM2.5')
        ax.plot(polution_by_year()['year'], polution_by_year()['PM10'], label='PM10')
        ax.set_xlabel('Year')
        ax.set_ylabel('Pollutions (PM2.5 & PM10)')
        ax.set_title('Yearly Pollution')
        ax.legend()

        st.pyplot(fig)
        st.write("Dari Chart diatas bisa disimpulkan bahwa Polusi meningkat dari tahun ke tahun, seiring berkembangnya zaman dan berjalannya waktu, polusi akan meningkat dan pada tahun 2017 merupakan puncaknya dan pada waktu 2016 masih ada upaya untuk menurunkan polusi udara")

    # added rain probability
    st.header("Kemungkinan terjadinya hujan karena tekanan udara")
    plt.figure(figsize=(10, 6))
    plt.scatter(rain_pos()['Pressure'], rain_pos()['RAIN'])
    plt.xlabel('Tekanan Udara')
    plt.ylabel('Kemungkinan Hujan')
    plt.title('Probabilitas Hujan')

    garis = plt.axvline(x=1013, ymin=0, ymax=100, color='r')
    legend = Line2D([0], [0], color='r', label='Tekanan Udara = 1013')
    plt.legend(handles=[legend])
    st.pyplot(plt.gcf())
    st.write('Berdasarkan dari scatter chart diatas, probabilitas akan terjadinya sebuah hujan bisa dipengaruhi dari teknanan udara, semakin rendah tekanan udara, semakin besar probabilitasnya terjadi hujan. contoh dari tabel diatas adalah, 1013 millibar atau yang digarisi warna merah dan dibawah angka standar tekanan udara, probabilitas hujan bisa lebih tinggi.')

    # ozone level

    st.header('Ozone Content')
    ozone1, ozone2, ozone3 = st.tabs(['Per Day', 'Per Month', 'Per Year'])

    with ozone1:
        st.header('Daily Ozone Content')
        plt.figure(figsize=(10,6))
        plt.plot(ozone_per_day()['day'], ozone_per_day()['O3'])
        plt.xlabel('Hari')
        plt.ylabel('O3 Content')
        plt.title('Kandungan Ozone Tahun (PPM)')
        st.pyplot(plt.gcf())
        st.write("Dari Line chart diatas kandungan ozone di udara paling tinggi ada di 60 PPM yang masih masuk kategori aman di index kualitas udara dan yang paling rendah ada di hari selasa di 50 PPM")

    with ozone2:
        st.header("Monthly Ozone Content")
        plt.figure(figsize=(10,6))
        plt.plot(ozone_per_month()['month'], ozone_per_month()['O3'])
        plt.title('Kandungan Ozone per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Kandungan Ozone (PPM)')
        st.pyplot(plt.gcf())
        st.write("Dari chart diatas ada kandungan ozone yang berlebihan tetapi masih standar index aman dari mulai maret - september")

    with ozone3:
        st.header('Yearly ozone Content')
        plt.figure(figsize=(10,6))
        plt.plot(ozone_per_year()['year'], ozone_per_year()['O3'])
        plt.xlabel('Tahun')
        plt.ylabel('O3 Content')
        plt.title('Kandungan Ozone Tahun (PPM)')
        st.pyplot(plt.gcf())
        st.write("Ternyata ada penurunan Kandungan Ozone di udara, yang merupakan hal yang sangat baik. karena peningkatan ozon bisa menyebabkan penyakit kesehatan, kerusakan tanaman, Global warming, dll.")


    st.write("")
    st.write("Faktor lain yang menyebabkan polusi udara adalah kandungan NO2 dan SO2 di udara")

    gas1, gas2, gas3 = st.tabs(['Other gas per day','Other gas per month','Other gas per year'])

    with gas1:
        st.header('Other gas content per day')
        plt.figure(figsize=(10,6))
        plt.plot(othergas_perday()['day'], othergas_perday()['SO2'], label='SO2')
        plt.plot(othergas_perday()['day'], othergas_perday()['NO2'], label='NO2')
        plt.legend()
        plt.title('Kandungan Gas lain per Hari')
        plt.xlabel('Hari')
        plt.ylabel('Kandungan Gas (PPM)')
        st.pyplot(plt.gcf())
    
    with gas2:
        st.header('Other gas content per month')
        plt.figure(figsize=(10,6))
        plt.plot(othergas_permonth()['month'], othergas_permonth()['SO2'], label='SO2')
        plt.plot(othergas_permonth()['month'], othergas_permonth()['NO2'], label='NO2')
        plt.legend()
        plt.title('Kandungan Gas lain per Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Kandungan Gas (PPM)')
        st.pyplot(plt.gcf())

    with gas3:
        st.header('Other gas content per year')
        plt.figure(figsize=(10,6))
        plt.plot(othergas_peryear()['year'], othergas_peryear()['SO2'], label='SO2')
        plt.plot(othergas_peryear()['year'], othergas_peryear()['NO2'], label='NO2')
        plt.legend()
        plt.title('Kandungan Gas lain per Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('Kandungan Gas (PPM)')
        st.pyplot(plt.gcf())        

    st.write('Kandungan gas lain yang mempengaruhi kualitas udara adalah SO2 dan NO2, dan untuk SO2, memang tidak begitu banyak dibandingkan dengan NO2. SO2 dan NO2 adalah polutan udara yang dihasilkan dari aktivitas manusia, membentuk prekursor partikel berbahaya dan ozon troposfer, menyebabkan polusi udara yang berbahaya bagi kesehatan manusia dan merusak lingkungan. Konsentrasi yang tinggi dari kedua gas ini di atmosfer menyebabkan iritasi pada saluran pernapasan, mengurangi jarak pandang dan mengurangi kualitas udara secara keseluruhan. Pentingnya pengendalian emisi SO2 dan NO2 dalam perlindungan kualitas udara dan kesehatan masyarakat tidak dapat ditekankan lagi.')

    st.header('Kesimpulan')
    st.write("Berbagai aktivitas manusia, termasuk industri, transportasi, pertanian, dan pembakaran bahan bakar fosil, menghasilkan polutan udara seperti partikel debu, sulfur dioksida (SO2), nitrogen dioksida (NO2), karbon monoksida (CO), ozon (O3), senyawa organik volatil (VOCs), dan partikel-partikel lainnya. Polutan-polutan ini mencemari udara dan dapat menyebabkan berbagai masalah kesehatan dan lingkungan, termasuk iritasi saluran pernapasan, masalah pernapasan kronis, kerusakan tanaman, polusi udara, pemanasan global, dan berkurangnya kualitas udara secara keseluruhan. Oleh karena itu, pengendalian emisi polutan udara dan promosi praktik-praktik ramah lingkungan sangat penting untuk menjaga kualitas udara dan melindungi kesehatan manusia serta ekosistem Bumi.")



main()