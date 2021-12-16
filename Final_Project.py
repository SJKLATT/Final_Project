"""
Name:   Stephen Klatt
CS230: Section 006
Data: Skyscraper2021
URL:streamlit run /Users/klatt_step/Python/Final_Project.py
Description: This project provides information about the world's 100 tallest skyscrapers

"""
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from streamlit_folium import folium_static
import folium
from collections import Counter
df_skyscrapers = pd.read_csv("Skyscrapers2021.csv")
s_df = df_skyscrapers.iloc[:,10]

number = st.slider('Pick a number', 2, 50)
def avg_ln(s_df,number):
    if number < len(s_df):
        total_n = 0
        for i in range(number):
            total_n = total_n + s_df[i]
        return total_n/number
    else:
        return sum(s_df)/len(s_df)

st.write(f"The average number of floors for the tallest {number} of skyscrapers is {int(avg_ln(s_df,number))}")

st.sidebar.header("Criteria for Pie Chart")
st.header("Information about Skyscrapers by CIty")
city_info = []
average_info = []
selection = st.sidebar.multiselect("Please choose the criteria to filter by:", ["Meters", "FUNCTION"])
if len(selection) == 0:
    meters = ""
    functions = ""
    locate = df_skyscrapers.loc[:, ["CITY", "Meters"]]
    locate = locate.groupby(by="CITY").count()
    locate = locate.reset_index()
    for i in range(len(locate)):
        average_info.append(f"{locate.iloc[i, 1]:.0f}")
        city_info.append(f"{locate.iloc[i, 0]}")
    fig, ax = plt.subplots()
    ax.pie(average_info, labels=city_info, autopct='%.1f%%')
    st.pyplot(fig)
elif len(selection) == 1:
    if selection[0] == "Meters":
        height = st.sidebar.slider("Pick the minimum height of the skyscraper", 330, 830)
        functions = ""
        locate = df_skyscrapers.loc[(df_skyscrapers["Meters"] > height), ["CITY", "Meters"]]
        locate = locate.groupby(by="CITY").count()
        locate = locate.reset_index()
        for i in range(len(locate)):
            average_info.append(f"{locate.iloc[i, 1]:.0f}")
            city_info.append(f"{locate.iloc[i, 0]}")
        fig, ax = plt.subplots()
        ax.pie(average_info, labels=city_info, autopct='%.1f%%')
        st.pyplot(fig)
    elif selection[0] == "FUNCTION":
        height = ""
        functions = st.sidebar.radio("Please select the type of function:", ("office / residential / hotel", "hotel / office", "other / hotel", "office", "hotel / residential / office / retail", "hotel / residential / office", "hotel / serviced apartments / office", "residential", "residential / hotel", "residential / office"))
        locate = df_skyscrapers.loc[(df_skyscrapers["FUNCTION"] == functions), ["CITY", "Meters"]]
        locate = locate.groupby(by="CITY").count()
        locate = locate.reset_index()
        for i in range(len(locate)):
            average_info.append(f"{locate.iloc[i, 1]:.0f}")
            city_info.append(f"{locate.iloc[i, 0]}")
        fig, ax = plt.subplots()
        ax.pie(average_info, labels=city_info, autopct='%.1f%%')
        st.pyplot(fig)
elif len(selection) == 2:
    if selection[0] == "Meters" and selection[1] == "FUNCTION":
        height = st.sidebar.slider("Pick the minimum height of the skyscraper", 330, 830)
        functions = st.sidebar.radio("Please select the type of function:", ("office / residential / hotel", "hotel / office", "other / hotel", "office", "hotel / residential / office / retail", "hotel / residential / office", "hotel / serviced apartments / office", "residential", "residential / hotel", "residential / office"))
        locate = df_skyscrapers.loc[(df_skyscrapers["FUNCTION"] == functions) & (df_skyscrapers["Meters"] > height), ["CITY", "Meters"]]
        locate = locate.groupby(by="CITY").count()
        locate = locate.reset_index()
        for i in range(len(locate)):
            average_info.append(f"{locate.iloc[i, 1]:.0f}")
            city_info.append(f"{locate.iloc[i, 0]}")
        fig, ax = plt.subplots()
        ax.pie(average_info, labels=city_info, autopct='%.1f%%')
        st.pyplot(fig)
    elif selection[1] == "Meters" and selection[0] == "FUNCTION":
        height = st.sidebar.slider("Pick the minimum height of the skyscraper", 330, 830)
        functions = st.sidebar.radio("Please select the type of function:", ("office / residential / hotel", "hotel / office", "other / hotel", "office", "hotel / residential / office / retail", "hotel / residential / office", "hotel / serviced apartments / office", "residential", "residential / hotel", "residential / office"))
        locate = df_skyscrapers.loc[(df_skyscrapers["FUNCTION"] == functions) & (df_skyscrapers["Meters"] > height), ["CITY", "Meters"]]
        locate = locate.groupby(by="CITY").count()
        locate = locate.reset_index()
        for i in range(len(locate)):
            average_info.append(f"{locate.iloc[i, 1]:.0f}")
            city_info.append(f"{locate.iloc[i, 0]}")
        fig, ax = plt.subplots()
        ax.pie(average_info, labels=city_info, autopct='%.1f%%')
        st.pyplot(fig)
st.header("Map of Location of the Tallest 100 Skyscrapers and Links for More Information")
df_skyscrapers.head()
center = [0, 0]
skyscraper_map = folium.Map(location=center, zoom_start=1)
for i, v in df_skyscrapers.iterrows():
    location = [v["Latitude"], v["Longitude"]]
    folium.Marker(location, popup=f"Name: {v['NAME']}\nCITY:"
                                  f" {v['CITY']}\nLink: {v['Link']}").add_to(skyscraper_map)
folium_static(skyscraper_map)

if st.button("Click to see an Image of the World's Largest Skyscraper"):
    st.image("Burj.webp", width=400)
