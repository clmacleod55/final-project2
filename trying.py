import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('team_stats_2003_2023.csv')

# Sidebar
st.sidebar.title('Filter Data')
selected_teams = st.sidebar.multiselect('Select Teams', ['All'] + list(df['team'].unique()), default=['All'])

# Filter data based on selected teams
filtered_df = df[df['team'].isin(selected_teams)]

# Remove teams with less than 10 wins
filtered_df = filtered_df[filtered_df['wins'] >= 10]

# Plotting
plt.figure(figsize=(12, 8))

# Line plot for each team
for team in filtered_df['team'].unique():
    team_data = filtered_df[filtered_df['team'] == team]
    team_data['yards_per_win'] = team_data['pass_yds'] / team_data['wins']  # Calculate yards per win
    plt.plot(team_data['year'], team_data['yards_per_win'], marker='o', label=team)

plt.title('NFL Team Stats')
plt.xlabel('Year')
plt.ylabel('Passing Yards per Win')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)

st.pyplot(plt)
