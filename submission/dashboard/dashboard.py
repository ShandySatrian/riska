import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
st.write(
    """
# DASHBOARD ANALISIS AIR QUALITY DATASET
    
- Nama: [Riska Dewi Yuliyanti]
- Email: [riskadewiyuliyanti@gmail.com]
- ID Dicoding: [riskady]
"""
)

# Memuat data dari CSV
main_df = pd.read_csv("./dashboard/main_data.csv")

# Mengatur judul untuk tampilan
st.title('Hasil Analisis')

# Container untuk Distribusi Suhu Harian
with st.container():
    st.header("Distribusi Suhu Harian")
    
    # Membuat histogram distribusi suhu harian
    fig, ax = plt.subplots(figsize=(10, 6))  # Mengatur ukuran figure
    sns.histplot(main_df['temp_x'], bins=30, kde=True, ax=ax)  # Pastikan kolom 'temp_x' ada
    ax.set_title('Distribusi Suhu Harian')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Frekuensi')

    # Menampilkan plot di dalam container
    st.pyplot(fig)
    
    # Container untuk Analisis Jumlah Berdasarkan Musim
with st.container():
    st.header("Analisis Jumlah (CNT) Berdasarkan Musim")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt_x', data=main_df, ax=ax)  # Pastikan kolom 'season' dan 'cnt_x' ada
    ax.set_title('Variasi Jumlah Pengendara Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Pengendara')

    st.pyplot(fig)

# Container untuk Distribusi Kelembapan Harian
with st.container():
    st.header("Distribusi Kelembapan Harian")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(main_df['hum_x'], bins=30, kde=True, ax=ax)  # Pastikan kolom 'hum_x' ada
    ax.set_title('Distribusi Kelembapan Harian')
    ax.set_xlabel('Kelembapan (%)')
    ax.set_ylabel('Frekuensi')

    st.pyplot(fig)

# Container untuk Identifikasi Outliers
with st.container():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=main_df[['temp_x', 'hum_x', 'cnt_x']])
    plt.title('Identifikasi Outliers Suhu, Kelembapan, dan Jumlah Pengendara')
    plt.ylabel('Nilai')
    plt.xticks([0, 1, 2], ['Suhu', 'Kelembapan', 'Jumlah Pengendara'])
    st.pyplot(plt)  # Gunakan st.pyplot untuk menampilkan plot

# Container untuk Korelasi Antar Variabel
with st.container():
    correlation_matrix = main_df[['temp_x', 'hum_x', 'cnt_x']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Korelasi Antar Variabel')
    st.pyplot(plt)  # Gunakan st.pyplot untuk menampilkan plot

# Container untuk Rata-rata Harian Suhu
with st.container():
    main_df['dteday'] = pd.to_datetime(main_df['dteday'])  # Mengubah ke datetime
    main_df.set_index('dteday', inplace=True)  # Mengatur kolom 'dteday' sebagai indeks

    # Menghitung rata-rata harian suhu
    daily_temperature = main_df['temp_x'].resample('D').mean()

    # Membuat plot
    plt.figure(figsize=(15, 6))
    daily_temperature.plot(title='Rata-rata Harian Suhu', xlabel='Tanggal', ylabel='Suhu (°C)')
    plt.axhline(y=daily_temperature.mean(), color='r', linestyle='--', label='Rata-rata Suhu Harian')
    plt.legend()
    st.pyplot(plt)  # Gunakan st.pyplot untuk menampilkan plot

# Container untuk Jumlah Total Pengendara Berdasarkan Musim
with st.container():
    seasonal_counts = main_df.groupby('season')['cnt_x'].sum()

    # Membuat plot
    plt.figure(figsize=(10, 6))
    seasonal_counts.plot(kind='bar', color='skyblue')
    plt.title('Jumlah Total Pengendara Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Pengendara')
    plt.xticks(ticks=range(4), labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'], rotation=0)
    plt.grid(axis='y')
    st.pyplot(plt)  # Gunakan st.pyplot untuk menampilkan plot

# Container untuk Distribusi Kelembapan Harian
with st.container():
    plt.figure(figsize=(10, 6))
    main_df['hum_x'].hist(bins=30, color='lightblue', edgecolor='black')
    plt.title('Distribusi Kelembapan Harian')
    plt.xlabel('Kelembapan (%)')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y')
    st.pyplot(plt)  # Gunakan st.pyplot untuk menampilkan plot
