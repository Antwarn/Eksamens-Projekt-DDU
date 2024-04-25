import pandas as pd

# Indlæs datasættet i en DataFrame
data = './output/AlphabetIncClassAGOOGL.csv'

# Opret en DataFrame
df = pd.read_csv(data)

# Konverter 'Time' kolonnen til datetidsformat
df['Time'] = pd.to_datetime(df['Time'])

# Filtrer rækkerne mellem 22:00 og 15:30
filtered_df = df[~(((df['Time'].dt.hour >= 22) & (df['Time'].dt.minute > 0)) | ((df['Time'].dt.hour < 15) | ((df['Time'].dt.hour == 15) & (df['Time'].dt.minute > 30))))]

# Skriv det filtrerede datasæt til en ny CSV-fil
filtered_df.to_csv('filtered_dataset.csv', index=False)

print("Filtrering afsluttet. Filen 'filtered_dataset.csv' er blevet oprettet.")
