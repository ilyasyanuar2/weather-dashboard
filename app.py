import streamlit as st
import pandas as pd
import sqlite3

# --- Judul Halaman ---
st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌦️ Weather Dashboard")
st.write("Data diambil dari OpenWeather API dan disimpan ke SQLite")

# --- Koneksi ke Database ---
conn = sqlite3.connect("weather.db")

# Ambil data dari tabel
df = pd.read_sql("SELECT * FROM weather_data", conn)

# Tutup koneksi
conn.close()

# --- Filter Kota ---
cities = df["city"].unique().tolist()
selected_city = st.selectbox("Pilih Kota:", cities)

# Filter berdasarkan kota
city_data = df[df["city"] == selected_city]

# --- Tampilkan Data ---
st.subheader(f"Data Cuaca {selected_city}")
st.dataframe(city_data)

# --- Grafik Suhu ---
st.subheader("📈 Perubahan Suhu")
st.line_chart(city_data.set_index("timestamp")["temperature"])

# --- Grafik Kelembaban ---
st.subheader("💧 Perubahan Kelembaban")
st.line_chart(city_data.set_index("timestamp")["humidity"])
