#'made by alessio ashiku
#



import skibidy
import pandas as pd
from skibidy import filtrati
df= filtrati
driver_dict = {}
for i in range(len(df)):
    row = df.iloc[i]
    eta = int(input(f"Inserire età del guidatore {row['forename']} {row['surname']}: "))
    posizione_griglia = int(input(f"Inserire poizione iniziale del guidatore {row['forename']} {row['surname']}: "))
    full_name = f"{row['forename']} {row['surname']}"
    driver_dict[i] = {
        'driverId': row['driverId'],
        'media_posizione': row['media_posizione'],
        'points': 0,
        'eta':eta,
        'posizione':posizione_griglia
    }
    driver_dict[i]['points']= 0

for i in range(len(df)):
   
    driver_dict[i]['points']= 0
    #lol decision tree start hereeeee 
    #i could make more decision tree in the same for 
    
    mediasoggetto = driver_dict[i]['media_posizione']
    etasoggetto = driver_dict[i]['eta']
    etasoggetto = etasoggetto - 28
    posizione_griglia_soggetto=driver_dict[i]['posizione']
    if etasoggetto<0:
        etasoggetto= etasoggetto*-1
    for j in range(len(df)):
        
        mediacomparazione = driver_dict[j]['media_posizione']
        etacomparazione = driver_dict[j]['eta']
        etacomparazione = etacomparazione - 28
        posizione_griglia_comparazione=driver_dict[j]['posizione']
        if etacomparazione<0:
           etacomparazione= etacomparazione*-1
        
        
        if j != i:
            mediacomparazione = driver_dict[j]['media_posizione']
            if mediasoggetto < mediacomparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
            if etasoggetto < etacomparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
            if posizione_griglia_soggetto < posizione_griglia_comparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
    print(f"{df.iloc[i]['forename']} {df.iloc[i]['surname']} → Punti: {driver_dict[i]['points']}")
sorted_drivers = sorted(driver_dict.items(), key=lambda x: x[1]['points'], reverse=True)

print("\n🏁 Classifica finale ordinata per punti:")
for idx, info in sorted_drivers:
    nome = f"{df.iloc[idx]['forename']} {df.iloc[idx]['surname']}"
    print(f"{nome} → {info['points']} punti")