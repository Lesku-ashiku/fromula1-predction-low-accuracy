import pandas as pd


drivers = pd.read_csv('drivers.csv', usecols=['driverId', 'forename', 'surname'])
results = pd.read_csv('results.csv', usecols=['driverId', 'position'])


results = results[results['position'].apply(lambda x: str(x).isdigit())]
results['position'] = results['position'].astype(int)


sum_positions = {}
count_positions = {}

for index, row in results.iterrows():
    driver_id = row['driverId']
    position = row['position']

    if driver_id not in sum_positions:
        sum_positions[driver_id] = 0
        count_positions[driver_id] = 0

    sum_positions[driver_id] += position
    count_positions[driver_id] += 1

media_driver = {
    driver_id: sum_positions[driver_id] / count_positions[driver_id]
    for driver_id in sum_positions
}

#
media_df = pd.DataFrame(list(media_driver.items()), columns=['driverId', 'media_posizione'])
media_df = media_df.merge(drivers[['driverId', 'forename', 'surname']], on='driverId', how='left')


media_df.sort_values(by='media_posizione', inplace=True)


nomi_input = []
print("Inserisci 5 nomi o cognomi di piloti (uno per volta):")
for i in range(15):
    nome = input(f"{i+1}) ").strip().lower()
    nomi_input.append(nome)

filtrati = media_df[
    media_df['forename'].str.lower().isin(nomi_input) |
    media_df['surname'].str.lower().isin(nomi_input)
]

# Stampa i risultati
if not filtrati.empty:
    print("\nPosizioni medie dei piloti inseriti:")
    print(filtrati[['forename', 'surname', 'media_posizione']])
else:
    print("Nessun pilota trovato con i nomi/cognomi inseriti.")