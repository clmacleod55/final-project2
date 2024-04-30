import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('team_stats_2003_2023.csv')

# Sidebar
st.sidebar.title('Filter Data')
selected_teams = st.sidebar.multiselect('Select Teams', df['team'].unique(), default=df['team'].unique())

# Filter data based on selected teams
filtered_df = df[df['team'].isin(selected_teams)]

# Group the data by year and team
grouped_df = filtered_df.groupby(['year', 'team']).mean()['win_loss_perc'].unstack()

# Plotting
plt.figure(figsize=(12, 8))

# Bar plot for each team
for i, team in enumerate(grouped_df.columns):
    plt.bar(grouped_df.index + 0.2 * i, grouped_df[team], width=0.2, label=team)

plt.title('Winning Percentage by Year')
plt.xlabel('Year')
plt.ylabel('Winning Percentage')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

st.pyplot(plt)
