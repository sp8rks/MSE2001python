import pandas as pd

filename = r'bulk_modulus.csv'
path = r'data_for_exercises/MP_Data/'
df = pd.read_csv(path+filename)

# bulk_modulus1 = df.to_dict()
# bulk_modulus2 = df.to_dict('series')
# bulk_modulus3 = df.to_dict('split')
# bulk_modulus4 = df.to_dict('records')
# bulk_modulus5 = df.to_dict('index')

bulk_modulus = dict(zip(df.formula.dropna(), df.bulk_modulus.dropna()))
