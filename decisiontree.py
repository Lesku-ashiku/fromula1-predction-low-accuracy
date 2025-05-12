#'made by alessio ashiku
#



import skibidy
import pandas as pd
from skibidy import filtrati
df = filtrati
driver_dict = {}
#for i(pilots) in (length of the list made out of pilots).
for i in range(len(df)):
    #basically formatting the data in a way that i can use it properly
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
#same thing as line 12. yes it has to be detatched because this for
#uses the data that just got made in the last for so if i had to merge the 2 for
#this part would need to use data that doesnt exist yet.
for i in range(len(df)):
   
    driver_dict[i]['points']= 0
  
      #formatting the driver averege position for each driver
    mediasoggetto = driver_dict[i]['media_posizione']
    #formatting the driver age for eache driver
    etasoggetto = driver_dict[i]['eta']
    etasoggetto = etasoggetto - 28
    #formatting the driver starting position for each driver
    posizione_griglia_soggetto=driver_dict[i]['posizione']
    #if MISS INPUT MISS INPUT CALM DOWN
    #no seriusly in line 37 i made a subtraction between the drivers age and the ideal age for f1
    #here i make it positive in case the pilot is younger 
    #ill use it for another subtracion later
    if etasoggetto<0:
        etasoggetto= etasoggetto*-1
    for j in range(len(df)):
        
        mediacomparazione = driver_dict[j]['media_posizione']
        etacomparazione = driver_dict[j]['eta']
        etacomparazione = etacomparazione - 28
        posizione_griglia_comparazione=driver_dict[j]['posizione']
        if etacomparazione<0:
           etacomparazione= etacomparazione*-1
        #same as line 41 but im doing it for the guy im comparing the (i) with 
        
        if j != i:
            mediacomparazione = driver_dict[j]['media_posizione']
            if mediasoggetto < mediacomparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
            if etasoggetto < etacomparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
            if posizione_griglia_soggetto < posizione_griglia_comparazione:
                driver_dict[i]['points']=driver_dict[i]['points']+1
                #line43
    print(f"{df.iloc[i]['forename']} {df.iloc[i]['surname']} → Punti: {driver_dict[i]['points']}")
sorted_drivers = sorted(driver_dict.items(), key=lambda x: x[1]['points'], reverse=True)

print("\n🏁 Classifica finale ordinata per punti:")
for idx, info in sorted_drivers:
    nome = f"{df.iloc[idx]['forename']} {df.iloc[idx]['surname']}"
    print(f"{nome} → {info['points']} punti")
    #from line 63 ti 72 is all just formatting data to look good
