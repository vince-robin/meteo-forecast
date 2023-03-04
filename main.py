import argparse
import requests

from utils import *


# Token unique API Météo Concept (obtenu gratuitement sur inscription ici : https://api.meteo-concept.com/login)
API_KEY = '' 


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("location")
    args = parser.parse_args()
    location = args.location

    # Informations diverses sur une commune recherchée en fonction de son nom
    location = requests.get('https://api.meteo-concept.com/api/location/cities/?token='+ API_KEY +'&search='+ location +'').json()['cities'][0]['insee']

    # ********************* MENU ************************** #
    print("\nVeuillez faire votre choix entre 1 et 8 : \n")
    choice = input (" 0 > Informations diverses sur la commune \n" + 
                    " 1 > Éphéméride pour un jour à venir (J+14 maximum) \n" +
                    " 2 > Prévisions journalières sur les 14 prochains jours \n" +
                    " 3 > Prévisions journalières pour un jour (J+14 maximum) \n" +
                    " 4 > Prévisions par périodes de la journée sur les 14 prochains jours \n" +
                    " 5 > Prévisions par périodes de la journée pour un jour (J+14 maximum) \n" +  
                    " 6 > Prévisions pour une période de la journée pour un jour (J+14 maximum) \n" +
                    " 7 > Prévisions horaires pour les 12 prochaines heures \n" + 
                    " 8 > Données météorologiques d'une station à proximité \n" + 
                    " q > Quitter \n" + 
                    "\nChoix : ")
    
    if(choice == '0'):
        information_about_the_city(location, API_KEY)

    elif(choice == '1'):
        choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
        ephemeris_for_one_day(location, API_KEY, choice_day)

    elif(choice == '2'):
        daily_forecast_next_days(location, API_KEY)

    elif(choice == '3'):
        choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
        daily_forecast_for_one_day(location, API_KEY, choice_day)

    elif(choice == '4'):
        forecast_by_period_over_next_days(location, API_KEY)

    elif(choice == '5'):
        choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
        period_of_the_day_forecasts_for_one_day(location, API_KEY, choice_day)

    elif(choice == '6'):
        choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
        choice_period = input("Période de la journée : \n" + 
                          " 0 > Nuit \n" +
                          " 1 > Matin \n" + 
                          " 2 > Après-midi \n" + 
                          " 3 > Soir \n" + 
                          "Choix : ")
        forecast_period_of_the_day(location, API_KEY, choice_day, choice_period)

    elif(choice == '7'):
        hourly_forecasts_next_hours(location, API_KEY)

    elif(choice == '8'):
        choice_radius = input("\nRayon de recherche en km de la station à proximité : \n" +  
                          " 5 > 5km \n" + 
                          " 10 > 10km \n" +
                          " 20 > 20km \n" +
                          " 50 > 50km \n" + 
                          "Choix : ")
        weather_data_nearby_station(location, API_KEY, choice_radius)

    else:
        print("\nProblem with the user choice! (between 0 and 8)")
