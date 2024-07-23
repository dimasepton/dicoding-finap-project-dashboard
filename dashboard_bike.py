# -*- coding: utf-8 -*-
"""dashboard_bike

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17OL33h-2qcGrf6YvNju0A-jQlSRcyCn8
"""

import pandas as pd
import seaborn as sns
import streamlit as st
sns.set(style='dark')

pd.read_csv("bike_hourly.csv")

hourly_df = pd.read_csv("bike_hourly.csv")

#Membuat Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_byseason_df(hourly_df):
    byseason_df = hourly_df.groupby(by="season").cnt.sum().reset_index()
    byseason_df.rename(columns={
        "cnt": "user count"
    }, inplace=True)
    byseason["season"] = pd.Categorical(byseason_df["season"], ["1", "2", "3", "4"])

    return byseason_df

def create_byhour_df(hourly_df):
    byhour_df = hourly_df.groupby(by="hr").cnt.sum().reset_index()
    byhour_df.rename(columns={
        "cnt": "user count"
    }, inplace=True)
    byhour["hr"] = pd.Categorical(byhour_df["hr"], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21","22", "23"])

    return byhour_df

# Mengubah kolom musim menjadi label
season_dict = {1: "Springer (Musim Semi)", 2: "Summer (Musim Panas)", 3: "Fall (Musim Gugur)", 4: "Winter (Musim Dingin)"}
hourly_df["season"] = hourly_df["season"].map(season_dict)

# Mengatur tata letak Streamlit
st.header("Dashboard Jumlah Sepeda yang Disewa")

selected_season = st.selectbox("Pilih Musim", hourly_df["season"].unique())
selected_hour = st.selectbox("Pilih Jam", sorted(hourly_df["hr"].unique()))

# Filter data berdasarkan pilihan musim dan membuat bar plot jumlah sepeda berdasarkan jam untuk musim yang dipilih
filtered_data_season = hourly_df[hourly_df["season"] == selected_season]

hourly_counts_season = filtered_data_season.groupby("hr")["cnt"].sum()
fig, ax = plt.subplots()
ax.bar(hourly_counts_season.index, hourly_counts_season.values, color="skyblue")
ax.set_title(f"Jumlah Sepeda yang Disewa Berdasarkan Jam pada Musim {selected_season}")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sepeda")
st.pyplot(fig)

# Filter data berdasarkan pilihan jam dan membuat bar plot jumlah sepeda berdasarkan musim untuk jam yang dipilih
filtered_data_hour = hourly_df[hourly_df["hr"] == selected_hour]

season_counts_hour = filtered_data_hour.groupby('season')['cnt'].sum()
fig, ax = plt.subplots()
ax.bar(season_counts_hour.index, season_counts_hour.values, color="skyblue")
ax.set_title(f"Jumlah Sepeda yang Disewa Berdasarkan Musim pada Jam {selected_hour}")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Sepeda")
st.pyplot(fig)

st.caption("Copyright (c) Dimas Septo Nugroho")
