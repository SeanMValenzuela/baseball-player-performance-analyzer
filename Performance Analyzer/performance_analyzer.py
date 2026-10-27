import pandas as pd

df_batting = pd.read_csv('batting.csv')
df_people = pd.read_csv('people.csv')

df_merged = df_batting.merge(df_people[['playerID', 'nameFirst', 'nameLast']], on='playerID', how='left')

filtered_df_1997 = df_merged[df_merged['yearID'] == 1997]

filtered_df_1997 = filtered_df_1997.groupby(['playerID','nameFirst', 'nameLast'], as_index=False).agg({
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

sorted_df_1997 = filtered_df_1997.sort_values(by='HR', ascending = False)

top_10_hrs_1997 = sorted_df_1997.head(10)

print(top_10_hrs_1997[['nameFirst', 'nameLast', 'HR']].to_string(index=False))