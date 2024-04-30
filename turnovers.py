import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('team_stats_2003_2023.csv')

# Filter data for the year 2023
df_2023 = df[df['year'] == 2023]

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of turnovers vs points allowed
plt.scatter(df_2023['turnovers'], df_2023['points_opp'], alpha=0.7)
plt.title('Turnovers vs Points Allowed for 2023 Teams')
plt.xlabel('Turnovers')
plt.ylabel('Points Allowed')
plt.grid(True)

st.pyplot(plt)


