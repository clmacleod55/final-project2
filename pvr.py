import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Colin/Downloads/team_stats_2003_2023.csv')

# Sidebar
st.sidebar.title('Filter Data')
selected_year = st.sidebar.slider('Select Year', min_value=2003, max_value=2023, value=2023)

# Filter data based on selected year
filtered_df = df[df['year'] == selected_year]

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of passing yards vs rushing yards
plt.scatter(filtered_df['pass_yds'], filtered_df['rush_yds'], alpha=0.7)
plt.title(f'Passing Yards vs Rushing Yards in {selected_year}')
plt.xlabel('Passing Yards')
plt.ylabel('Rushing Yards')
plt.grid(True)

st.pyplot(plt)


