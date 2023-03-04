import requests
import numpy as np
import matplotlib.pyplot as plt

from weather_codes import WEATHER


def add_value_label(x_list,y_list):
    for i in range(0, len(x_list)):
        plt.text(i,y_list[i],y_list[i])


# choice 0
"""
Informations diverses à propos d'une ville
"""
def information_about_the_city(location, api_key):
    
    r = requests.get('https://api.meteo-concept.com/api/location/city?token='+ api_key +'&insee='+ location).json()
    
    # city object
    insee_code = r['city']['insee']    # Code Insee de la commune
    postal_code = r['city']['cp']      # Code postal de la commune
    latitude = r['city']['latitude']   # Latitude décimale de la commune
    longitude = r['city']['longitude'] # Longitude décimale de la commune
    altitude = r['city']['altitude']   # Altitude de la commune en mètres
    city_name = r['city']['name']      # Nom de la commune
    
	# ************* PRINT RESULTS ************* #
    print("\nNom de la ville : ", city_name)
    print("Code INSEE : ", insee_code)
    print("Code postal : ", postal_code)
    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("Altitude : ", altitude, "m")


# choice 1
"""
Éphéméride pour un jour à venir 
"""
def ephemeris_for_one_day(location, api_key, choice_day):
    
    r = requests.get('https://api.meteo-concept.com/api/ephemeride/' + choice_day + '?token=' + api_key +'&insee='+ location +'').json()

    insee_code = r["ephemeride"]["insee"]                    # Code Insee de la commune
    latitude = r["ephemeride"]["latitude"]                   # Latitude décimale de la commune
    longitude = r["ephemeride"]["longitude"]                 # Longitude décimale de la commune
    day = r["ephemeride"]["day"]                             # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    datetime = r["ephemeride"]["datetime"]                   # Date en heure locale, format ISO8601
    sunrise = r["ephemeride"]["sunrise"]                     # Heure du lever du soleil, format HH:MM
    sunset = r["ephemeride"]["sunset"]                       # Heure du coucher du soleil, format HH:MM
    duration_day = r["ephemeride"]["duration_day"]           # Durée du jour en heure et minutes, format HH:MM
    diff_duration_day = r["ephemeride"]["diff_duration_day"] # Gain ou perte de durée du jour par rapport à la veille en minutes

	# ************* PRINT RESULTS ************* #
    print("\nJour  : J+"+str(day))
    print("Heure locale : ", datetime)
    print("Lever du soleil : ", sunrise)
    print("Coucher du soleil : ", sunset)
    print("Durée du jour : ", duration_day)
    print("Gain ou perte de durée du jour : ", diff_duration_day, "min")
    

# choice 2
"""
Prévisions journalières sur les 14 prochains jours
"""    
def daily_forecast_next_days(location, api_key):
	
    r = requests.get('https://api.meteo-concept.com/api/forecast/daily?token='+ api_key +'&insee='+ location +'').json()
    (city, forecast) = (r[k] for k in ('city','forecast'))

    tmin = []
    tmax = []
    rr10 = []
    sun_hours = []
    day = []
    wind10m = []
    gust10m = []
    dirwind10m = []
    rr1 = []
    probarain = []
    weather = []
    etp = []
    probafrost = []
    probafog = []
    probawind70 = []
    probawind100 = []
    gustx = []

    for i, r2 in enumerate(forecast):
        # forecast-day object
        insee_code = r2["insee"]               # Code Insee de la commune
        postal_code = r2["cp"]                 # Code postal de la commune
        latitude = r2["latitude"]              # Latitude décimale de la commune
        longitude = r2["longitude"]            # Longitude décimale de la commune
        datetime = r2["datetime"]              # Date en heure locale, format ISO8601
        day.append(r2["day"])                  # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
        wind10m.append(r2["wind10m"])          # Vent moyen à 10 mètres en km/h
        gust10m.append(r2["gust10m"])          # Rafales de vent à 10 mètres en km/h
        dirwind10m.append(r2["dirwind10m"])    # Direction du vent en degrés (0 à 360°)
        rr10.append(r2["rr10"])                # Cumul de pluie sur la journée en mm
        rr1.append(r2["rr1"])                  # Cumul de pluie maximal sur la journée en mm
        probarain.append(r2["probarain"])      # Probabilité de pluie entre 0 et 100%
        weather.append(r2["weather"])          # Temps sensible (Code temps) – Voir Annexes
        tmin.append(r2["tmin"])                # Température minimale à 2 mètres en °C
        tmax.append(r2["tmax"])                # Température maximale à 2 mètres en °C
        sun_hours.append(r2["sun_hours"])      # Ensoleillement en heures
        etp.append(r2["etp"])                  # Cumul d'évapotranspiration en mm
        probafrost.append(r2["probafrost"])    # Probabilité de gel entre 0 et 100%
        probafog.append(r2["probafog"])        # Probabilité de brouillard entre 0 et 100%
        probawind70.append(r2["probawind70"])  # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100.append(r2["probawind100"])# Probabilité de vent >100 km/h entre 0 et 100%
        gustx.append(r2["gustx"])              # Rafale de vent potentielle sous orage ou grain en km/h

		# ************* PRINT RESULTS ************* #
        print("\nPrévision : J+" + str(i))
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m[i], "km/h")
        print("Rafales de vent à 10m : ", gust10m[i], "km/h")
        print("Direction du vent : ", dirwind10m[i], "°")
        print("Cumul de pluie sur la journée: ", rr10[i], "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1[i], "mm")
        print("Probabilité de pluie : ", probarain[i], "%")
        print("Temps : ", WEATHER[weather[i]])
        print("Température minimale (à 2m) : ", tmin[i], "°C")
        print("Température maximale (à 2m) : ", tmax[i], "°C")
        print("Ensoleillement : ", sun_hours[i], "h")
        print("Evapotranspiration : ", etp[i], "mm")
        print("Probabilité de gel : ", probafrost[i], "%")
        print("Probabilité de brouillard : ", probafog[i], "%")
        print("Probabilité de vent >70 km/h : ", probawind70[i], "%")
        print("Probabilité de vent >100 km/h : ", probawind100[i], "%")
        print("Rafale de vent potentielle sous orage : ", gustx[i], "km/h")

    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure(figsize=(15,7))
    ax = plt.gca() 
    plt.suptitle("14-day forecast for "+ str(city['name']), fontsize=15)
    #manager = plt.get_current_fig_manager()  
    #manager.full_screen_toggle()   # Full-screen option

    day = np.array(day)
    tmin = np.array(tmin)
    tmax = np.array(tmax)
    sun_hours = np.array(sun_hours)
    rr10 = np.array(rr10)
    wind10m = np.array(wind10m)
    gust10m = np.array(gust10m)
    dirwind10m = np.array(dirwind10m)
    rr1 = np.array(rr1)
    weather = np.array(weather)
    etp = np.array(etp)
    probarain = np.array(probarain)
    probafrost = np.array(probafrost)
    probafog = np.array(probafog)
    probawind70 = np.array(probawind70)
    probawind100 = np.array(probawind100)
    gustx = np.array(gustx)

    plt.subplot(2, 3, 3)
    plt.plot(day, tmin, "-rs")
    add_value_label(day,tmin)
    plt.plot(day, tmax, "-bs")
    add_value_label(day,tmax)
    legend = ['Tmin', 'Tmax']
    plt.legend(legend, loc='upper right')
    plt.ylim([0,max(tmax)+5])
    plt.xlim([-0.5,13.5])
    #ax.xaxis.set_ticks(range(len(day)))
    plt.xlabel("Day")
    plt.ylabel("Temperatures (in degrees)")
    plt.grid()

    plt.subplot(2, 3, 5)
    graph_bar = plt.bar(day, rr10)
    plt.xlabel("Day")
    plt.ylabel("Total (in mm)")
    plt.ylim([0,max(rr10)+5])
    plt.xlim([-0.5,13.5])
    i = 0 
    for p in graph_bar:
      width = p.get_width()
      height = p.get_height()
      x, y = p.get_xy()
      plt.text(x+width/2, y+height/2, rr10[i], ha='center', color = 'black')
      i += 1

    plt.subplot(2, 3, 4)
    graph_bar2 = plt.bar(day, sun_hours, color = 'orange')
    plt.xlabel("Day")
    plt.ylabel("Total (in h)")
    plt.ylim([0,max(sun_hours)+5])
    plt.xlim([-0.5,13.5])
    i = 0 
    for p in graph_bar2:
      width = p.get_width()
      height = p.get_height()
      x, y = p.get_xy()
      plt.text(x+width/2, y+height/2, sun_hours[i], ha='center', color = 'black')
      i += 1
    #ax.xaxis.set_ticks(range(len(day)))

    plt.subplot(2, 3, 1)
    plt.plot(day, probarain, color='green', marker='s')
    plt.plot(day, probafrost, color='yellow', marker='s')
    plt.plot(day, probafog, color='purple', marker='s')
    plt.plot(day, probawind70, color='brown', marker='s')
    plt.xlabel("Day")
    plt.ylabel("Probability (in %)")
    plt.grid()
    legend = ['Rain', 'Frost', 'Fog', 'Wind>70km/h']
    plt.legend(legend, loc='upper left')

    plt.subplot(2, 3, 2)
    plt.plot(day, wind10m, color='green', marker='s')
    plt.plot(day, gust10m, color='purple', marker='s')
    plt.xlabel("Day")
    plt.ylabel("Speed (in km/k)")
    plt.grid()
    legend = ['Wind 10 m', 'Gust 10m', 'Fog', 'Wind>70km/h']
    plt.legend(legend, loc='upper right')

    plt.subplot(2, 3, 6)
    graph_bar = plt.bar(day, etp)
    plt.xlabel("Day")
    plt.ylabel("Total (in mm)")
    plt.ylim([0,max(etp)+3])
    plt.xlim([-0.5,13.5])
    i = 0 
    for p in graph_bar:
      width = p.get_width()
      height = p.get_height()
      x, y = p.get_xy()
      plt.text(x+width/2, y+height/2, etp[i], ha='center', color = 'black')
      i += 1

    '''
    plt.subplot(2, 3, 6)
    _, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(dirwind10m, day)
    ax.set_rmax(13)
    ax.set_rticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 
    ax.grid(True)
    '''

    plt.show()


# choice 3
"""
Prévisions journalières pour un jour (J+14 maximum) 
"""
def daily_forecast_for_one_day(location, api_key, choice_day):

    r = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day + '?token='+ api_key +'&insee='+ location +'').json()

    # forecast-day object
    insee_code = r["forecast"]["insee"]          # Code Insee de la commune
    postal_code = r["forecast"]["cp"]            # Code postal de la commune
    latitude = r["forecast"]["latitude"]         # Latitude décimale de la commune
    longitude = r["forecast"]["longitude"]       # Longitude décimale de la commune
    day = r["forecast"]["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    datetime = r["forecast"]["datetime"]         # Date en heure locale, format ISO8601
    wind10m = r["forecast"]["wind10m"]           # Vent moyen à 10 mètres en km/h
    gust10m = r["forecast"]["gust10m"]           # Rafales de vent à 10 mètres en km/h
    dirwind10m = r["forecast"]["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
    rr10 = r["forecast"]["rr10"]                 # Cumul de pluie sur la journée en mm
    rr1 = r["forecast"]["rr1"]                   # Cumul de pluie maximal sur la journée en mm
    probarain = r["forecast"]["probarain"]       # Probabilité de pluie entre 0 et 100%
    weather = r["forecast"]["weather"]           # Temps sensible (Code temps) – Voir Annexes
    tmin = r["forecast"]["tmin"]                 # Température minimale à 2 mètres en °C
    tmax = r["forecast"]["tmax"]                 # Température maximale à 2 mètres en °C
    sun_hours = r["forecast"]["sun_hours"]       # Ensoleillement en heures
    etp = r["forecast"]["etp"]                   # Cumul d'évapotranspiration en mm
    probafrost = r["forecast"]["probafrost"]     # Probabilité de gel entre 0 et 100%
    probafog = r["forecast"]["probafog"]         # Probabilité de brouillard entre 0 et 100%
    probawind70 = r["forecast"]["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
    probawind100 = r["forecast"]["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
    gustx = r["forecast"]["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h

	# ************* PRINT RESULTS ************* #
    print("\nPrévision :  J+" + str(day))
    print("Heure locale : ", datetime)
    print("Vent moyen à 10m : ", wind10m, "km/h")
    print("Rafales de vent à 10m : ", gust10m, "km/h")
    print("Direction du vent : ", dirwind10m, "°")
    print("Cumul de pluie sur la journée: ", rr10, "mm")
    print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
    print("Probabilité de pluie : ", probarain, "%")
    print("Temps : ", WEATHER[weather])
    print("Température minimale (à 2m) : ", tmin, "°C")
    print("Température maximale (à 2m) : ", tmax, "°C")
    print("Ensoleillement : ", sun_hours, "h")
    print("Evapotranspiration : ", etp, "mm")
    print("Probabilité de gel : ", probafrost, "%")
    print("Probabilité de brouillard : ", probafog, "%")
    print("Probabilité de vent >70 km/h : ", probawind70, "%")
    print("Probabilité de vent >100 km/h : ", probawind100, "%")
    print("Rafale de vent potentielle sous orage : ", gustx, "km/h")


# choice 4
"""
Prévisions par périodes de la journée sur les 14 prochains jours
"""
def forecast_by_period_over_next_days(location, api_key):
    
    r = requests.get('https://api.meteo-concept.com/api/forecast/daily/periods?token='+ api_key +'&insee='+ location +'').json()
    forecast = [r['forecast'][k][0] for k in range(0,14)]

    for f in forecast:

        # forecast-period object
        insee_code = f["insee"]          # Code Insee de la commune
        postal_code = f["cp"]            # Code postal de la commune
        latitude = f["latitude"]         # Latitude décimale de la commune
        longitude = f["longitude"]       # Longitude décimale de la commune
        day = f["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
        period = f["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
        datetime = f["datetime"]         # Date en heure locale, format ISO8601
        wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
        gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
        dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
        rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
        rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
        probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
        weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
        probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
        probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
        probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
        gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
        update = r["update"]            # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

        print("\nPrévision :  J+" + str(day))
        print("Période : ", period)
        if(period == 0):
            period = 'Nuit'
        elif(period == 1):
            period = 'Matin'
        elif(period == 2):
            period = 'Après-midi'
        else:
            period = 'Soir'
        
        # ************* PRINT RESULTS ************* #    
        print("Heure de mise à jour : ", update)
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")


# Choix 5
"""
Prévisions par périodes de la journée pour un jour (J+14 maximum)
"""
def period_of_the_day_forecasts_for_one_day(location, api_key, choice_day):
    
    r = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day+ '/periods?token='+ api_key +'&insee='+ location +'').json()
    forecast = [r['forecast'][k] for k in range(0,4)]

    for f in forecast:

        # forecast-period object
        insee_code = f["insee"]          # Code Insee de la commune
        postal_code = f["cp"]            # Code postal de la commune
        latitude = f["latitude"]         # Latitude décimale de la commune
        longitude = f["longitude"]       # Longitude décimale de la commune
        day = f["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
        period = f["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
        if(period == 0):
            period = 'Nuit'
        elif(period == 1):
            period = 'Matin'
        elif(period == 2):
            period = 'Après-midi'
        else:
            period = 'Soir'
        datetime = f["datetime"]         # Date en heure locale, format ISO8601
        wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
        gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
        dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
        rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
        rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
        probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
        weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
        probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
        probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
        probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
        gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
        update = r["update"]            # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

		# ************* PRINT RESULTS ************* #
        print("\nPrévision :  J+" + str(day))
        print("Période : ", period)
        print("Heure de mise à jour : ", update)
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")


# choice 6
"""
Prévisions pour une période de la journée pour un jour (J+14 maximum)
"""
def forecast_period_of_the_day(location, api_key, choice_day, choice_period):
    
    r = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day + '/period/' + choice_period + '?token='+ api_key +'&insee='+ location +'').json() 
    
    # forecast-period object
    insee_code = r["forecast"]["insee"]          # Code Insee de la commune
    postal_code = r["forecast"]["cp"]            # Code postal de la commune
    latitude = r["forecast"]["latitude"]         # Latitude décimale de la commune
    longitude = r["forecast"]["longitude"]       # Longitude décimale de la commune
    day = r["forecast"]["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    period = r["forecast"]["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
    if(period == 0):
        period = 'Nuit'
    elif(period == 1):
        period = 'Matin'
    elif(period == 2):
        period = 'Après-midi'
    else:
        period = 'Soir'
    datetime = r["forecast"]["datetime"]         # Date en heure locale, format ISO8601
    wind10m = r["forecast"]["wind10m"]           # Vent moyen à 10 mètres en km/h
    gust10m = r["forecast"]["gust10m"]           # Rafales de vent à 10 mètres en km/h
    dirwind10m = r["forecast"]["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
    rr10 = r["forecast"]["rr10"]                 # Cumul de pluie sur la journée en mm
    rr1 = r["forecast"]["rr1"]                   # Cumul de pluie maximal sur la journée en mm
    probarain = r["forecast"]["probarain"]       # Probabilité de pluie entre 0 et 100%
    weather = r["forecast"]["weather"]           # Temps sensible (Code temps) – Voir Annexes
    probafrost = r["forecast"]["probafrost"]     # Probabilité de gel entre 0 et 100%
    probafog = r["forecast"]["probafog"]         # Probabilité de brouillard entre 0 et 100%
    probawind70 = r["forecast"]["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
    probawind100 = r["forecast"]["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
    gustx = r["forecast"]["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
    update = r["update"]                         # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

	# ************* PRINT RESULTS ************* #
    print("\nPrévision : J+" + str(day))
    print("Période :", period)
    print("Heure de mise à jour :", update)
    print("Heure locale :", datetime)
    print("Vent moyen à 10m :", wind10m, "km/h")
    print("Rafales de vent à 10m :", gust10m, "km/h")
    print("Direction du vent :", dirwind10m, "°")
    print("Cumul de pluie sur la journée:", rr10, "mm")
    print("Cumul de pluie maximal sur la journée :", rr1, "mm")
    print("Probabilité de pluie :", probarain, "%")
    print("Temps :", WEATHER[weather])
    print("Probabilité de gel :", probafrost, "%")
    print("Probabilité de brouillard :", probafog, "%")
    print("Probabilité de vent >70 km/h :", probawind70, "%")
    print("Probabilité de vent >100 km/h: ", probawind100, "%")
    print("Rafale de vent potentielle sous orage: ", gustx, "km/h")


# choice 7 
"""
Prévisions horaires pour les 12 prochaines heures
"""
def hourly_forecasts_next_hours(location, api_key):
	
	r = requests.get('https://api.meteo-concept.com/api/forecast/nextHours?token='+ api_key +'&insee='+ location +'').json()
	forecast = r["forecast"]  # forecast-hour object

	for f in forecast:
		insee_code = f["insee"]          # Code Insee de la commune
		postal_code = f["cp"]            # Code postal de la commune
		latitude = f["latitude"]         # Latitude décimale de la commune
		longitude = f["longitude"]       # Longitude décimale de la commune
		datetime = f["datetime"]         # Date en heure locale, format ISO8601
		rh2m = f["rh2m"]                 # Humidité à 2 mètres en %
		wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
		gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
		dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
		rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
		rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
		probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
		weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
		probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
		probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
		probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
		probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
		tsoil1 = f["tsoil1"]             # Température du sol entre 0 et 10 cm en °C.
		tsoil2 = f["tsoil2"]             # Température du sol entre 10 et 40 cm en °C.
		gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
		iso0 = f["iso0"]                 # Altitude du isotherme 0°C en mètres
		update = r["update"]             # Chaîne de caractère donnant la date de la prévision (au format ISO8601)   
		

		# ************* PRINT RESULTS ************* #
		print("\nHeure locale : ", datetime)
		print("Heure de mise à jour : ", update)
		print("Vent moyen à 10m : ", wind10m, "km/h")
		print("Rafales de vent à 10m : ", gust10m, "km/h")
		print("Direction du vent : ", dirwind10m, "°")
		print("Cumul de pluie sur la journée: ", rr10, "mm")
		print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
		print("Probabilité de pluie : ", probarain, "%")
		print("Temps : ", WEATHER[weather])
		print("Probabilité de gel : ", probafrost, "%")
		print("Probabilité de brouillard : ", probafog, "%")
		print("Probabilité de vent >70 km/h : ", probawind70, "%")
		print("Probabilité de vent >100 km/h : ", probawind100, "%")
		print("Rafale de vent potentielle sous orage : ", gustx, "km/h")
		print("Altitude du isotherme 0°C : ", iso0, "m")
		print("Température du sol entre 0 et 10 cm : ", tsoil1, "°C")
		print("Température du sol entre 10 et 40 cm : ", tsoil2, "°C")


# choice 8
"""
Données météorologiques d'une station à proximité 
"""
def weather_data_nearby_station(location, api_key, choice_radius):
    
    r = requests.get('https://api.meteo-concept.com/api/observations/around?token='+ api_key +'&insee='+ location +'&radius=' + choice_radius).json()
    (station,observation) = (r[0][k] for k in ('station','observation'))
    
    # station object 
    name_station = station['name']         # Nom attribué à la station
    uuid = station["uuid"]                 # Identifiant de la station sous une forme d'une chaîne de 36 caractères hexadécimaux et tirets de la forme XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.
    latitude = station["latitude"]         # Latitude décimale de la station
    longitude = station["longitude"]       # Longitude décimale de la station
    elevation = station["elevation"]       # Altitude de la station (au-dessus du niveau de la mer)
    city = station["city"]                 # Commune et département d'installation de la commune (si connu)

    print("\nNom de la station :", name_station)
    print("Identifiant de la station :", uuid)
    print("Latitude :", latitude)
    print("Longitude :", longitude)
    print("Altitude :", elevation, "m")
    print("Commune :", city)

    # observation object
    time = observation["time"]                                            # Date et heure de l'observation, au format ISO8601
    print("Date et heure de l'observation :", time)

    if observation.get('outside_temperature') is not None:
        outside_temperature = observation["outside_temperature"]["value"] # Température extérieure en °C
        print("Température extérieure:", outside_temperature, observation["outside_temperature"]["unit"])

    if observation.get('barometer') is not None:
        barometer = observation["barometer"]["value"]                     # Pression atmosphérique en hPa
        print("Pression atmosphérique :", barometer, observation["barometer"]["unit"])

    if observation.get('wind_speed') is not None:
        wind_speed = observation["wind_speed"]["value"]                   # Vitesse du vent en km/h
        print("Vitesse du vent :", wind_speed, observation["wind_speed"]["unit"])

    if observation.get('wind_s') is not None:
        wind_s = observation["wind_s"]["value"]                           # Vent moyen en km/h
        print("Vent moyen :", wind_s, observation["wind_s"]["unit"])

    if observation.get('wind_10m') is not None:
        wind_10m = observation["wind_10m"]["value"]                       # Vent moyen en km/h
        print("Vent moyen à 10m:", wind_s, observation["wind_10m"]["unit"])
    
    if observation.get('windgust_s') is not None:
        windgust_speed = observation["windgust_s"]["value"]               # Vitesse des rafales du vent en km/h
        print("Vitesse des rafales de vent :", windgust_speed, observation["windgust_s"]["unit"])
    
    if observation.get('windgust_10m') is not None:
        windgust_10m = observation["windgust_10m"]["value"]               # Vitesse des rafales du vent à 10m en km/h
        print("Rafales de vents à 10m :", windgust_10m, observation["windgust_10m"]["unit"])

    if observation.get('wind_direction_s') is not None:
        wind_direction_s = observation["wind_direction_s"]["value"]       # Direction du vent moyen
        print("Direction du vent moyen :", wind_direction_s, observation["wind_direction_s"]["unit"])

    if observation.get("wind_direction") is not None:
        wind_direction = observation["wind_direction"]["value"]           # Direction du vent
        print("Direction du vent :", wind_direction, observation["wind_direction"]["unit"])

    if observation.get("outside_humidity") is not None:
        outside_humidity = observation["outside_humidity"]["value"]       # Humidité relative en %
        print("Humidité relative :", outside_humidity, observation["outside_humidity"]["unit"])

    if observation.get('rainfall') is not None:
        rainfall = observation["rainfall"]["value"]                       # Précipitations en mm
        print("Précipitations :", rainfall, observation["rainfall"]["unit"])
    
    if observation.get('dew_point') is not None:
        dewpoint = observation["dew_point"]["value"]                      # Point de rosée en °C
        print("Point de rosée :", dewpoint, observation["dew_point"]["unit"])

    if observation.get("evapotranspiration") is not None:
        evapotranspiration = observation["evapotranspiration"]["value"]   # Évapotranspiration en mm
        print("Évapotranspiration :", evapotranspiration, observation["evapotranspiration"]["unit"])

    if observation.get('global_radiation') is not None:
        solar_radiation = observation["global_radiation"]["value"]        # Rayonnement solaire en W/m2
        print("Rayonnement solaire : ", solar_radiation, observation["evapotranspiration"]["unit"])

    if observation.get('wind_chill') is not None:
        windchill = observation["wind_chill"]["value"]                    # Température ressentie
        print("Température ressentie :", windchill, observation["wind_chill"]["unit"] )
    
    if observation.get('rainrate') is not None:
        rainrate = observation["rainrate"]["value"]                       # Intensité des précipitation en mm/h
        print("Intensité des précipitations :", rainrate, observation["rainrate"]["unit"] )

    if observation.get('insolation_time') is not None:
        insolation_time = observation["insolation_time"]["value"]         # Durée d'ensoleillement en min
        print("Durée d'ensoleillement : ", insolation_time, observation["insolation_time"]["unit"])

    '''
    Note : Si la clé "insolation_time" n'existe pas, cela ne va pas générer une erreur. 
    Sans cette technique, on obtient une erreur KeyError car on essaye d'accéder à une valeur dans un dictionnaire à l'aide d'une clé qui n'existe pas. 
    En utilisant .get("MYKEY"), si la clé "MYKEY" n'existe pas, get() retourne None.
    '''

