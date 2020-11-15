import pandas as pd

filename = r'class_exercises/fantasy_sets.csv'
df = pd.read_csv(filename)

LoTR = df['LOTR'].dropna()
StarWars = df['SW'].dropna()
HarryPotter = df['HP'].dropna()

LoTR = set(LoTR)
StarWars = set(StarWars)
HarryPotter = set(HarryPotter)

LoTR_HP_common = LoTR.intersection(HarryPotter)
LoTR_SW_common = LoTR.intersection(StarWars)
all_three_common = LoTR.intersection(HarryPotter, StarWars)

diffs = LoTR.difference(HarryPotter)

union_fantasy = LoTR.union(HarryPotter, StarWars)
