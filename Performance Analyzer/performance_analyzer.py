import pandas as pd

df_batting = pd.read_csv('batting.csv')
df_people = pd.read_csv('people.csv')

df_merged = df_batting.merge(df_people[['playerID', 'nameFirst', 'nameLast']], on='playerID', how='left')

year = input("Enter the year you want find stats for: ")
stat = input("Enter the specific stat you want: ")
top_positions = input("Enter the ranks of the stat you want (e.g. 5 for top 5, 10 for top 10): ")


filtered_df = df_merged[df_merged['yearID'] == int(year)]

filtered_df = filtered_df.groupby(['playerID','nameFirst', 'nameLast'], as_index=False).agg({
    'G': 'sum',
    'AB': 'sum',
    'R': 'sum',
    'H': 'sum',
    '2B': 'sum',
    '3B': 'sum',
    'HR': 'sum',
    'RBI': 'sum',
    'SB': 'sum',
    'CS': 'sum',
    'BB': 'sum',
    'SO': 'sum',
    'IBB': 'sum',
    'HBP': 'sum',
    'SH': 'sum',
    'SF': 'sum',
    'GIDP': 'sum',
})

sorted_df = filtered_df.sort_values(by=stat, ascending = False)

top_of_list = sorted_df.head(int(top_positions))

print(top_of_list[['nameFirst', 'nameLast', stat]].to_string(index=False))