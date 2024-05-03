import pandas as pd

# Indlæs datasættet i en DataFrame
data = './output02052024/AlphabetIncClassAGOOGL.csv'

# Opret en DataFrame
df = pd.read_csv(data)

# Konverter 'Time' kolonnen til datetidsformat
df['Time'] = pd.to_datetime(df['Time'])

# Filtrer rækkerne mellem 22:00 fredag og 15:30 mandag
filtered_df = df[~(((df['Time'].dt.dayofweek == 4) & (df['Time'].dt.hour >= 22)) |
                   ((df['Time'].dt.dayofweek == 0) & (df['Time'].dt.hour < 15)) |
                   ((df['Time'].dt.dayofweek == 0) & (df['Time'].dt.hour == 15) & (df['Time'].dt.minute > 30)) |
                   (df['Time'].dt.dayofweek == 5) | (df['Time'].dt.dayofweek == 6))]

# Skriv det filtrerede datasæt til en ny CSV-fil
filtered_df.to_csv('google26.csv', index=False)

print("Filtrering afsluttet. Filen 'google26.csv' er blevet oprettet.")
