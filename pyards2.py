import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('team_stats_2003_2023.csv')

# Sidebar
st.sidebar.title('Filter Data')
selected_year = st.sidebar.slider('Select Year', min_value=2003, max_value=2023, value=2023)

# Filter data based on selected year
filtered_df = df[df['year'] == selected_year]

# Sort data by passing yards
filtered_df = filtered_df.sort_values(by='pass_yds', ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['team'], filtered_df['pass_yds'])
plt.title(f'Passing Yards by Team in {selected_year}')
plt.xlabel('Team')
plt.ylabel('Passing Yards')
plt.xticks(rotation=45, ha='right')

# Add median line
median_pass_yards = filtered_df['pass_yds'].median()
plt.axhline(y=median_pass_yards, color='r', linestyle='--', label='Median Passing Yards')

plt.legend()
plt.tight_layout()

st.pyplot(plt)

