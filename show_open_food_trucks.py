#!/usr/bin/env python

# Make sure to install requests before running:
# > pip install requests
# Documentation for the requests library can be found here: http://docs.python-requests.org/en/master/

import json
import pprint
import requests
from datetime import datetime
from pytz import timezone

# Format printer for debugging purposes. Real life scenario would utilize a proper logger for scalable monitoring
pp = pprint.PrettyPrinter(indent=4)

# Calculate time
# get west coast time (since socrata is for San Francisco)
western = timezone("America/Los_Angeles")
west_time = datetime.now(western)

def getWeekday():

    weekday = west_time.strftime("%A")
    print(f"Current day of the week: {weekday}")

    return weekday


def getHour():
    
    hour = west_time.strftime("%H")
    print(f"Current time in San Francisco (24hrs): {hour}")

    return hour


def constructQuery(hour, weekday):

    day_query = f"dayofweekstr={weekday}"

    url = f"http://data.sfgov.org/resource/bbb8-hzi6.json?{day_query}"

    print(f"Constructed query: {url}")

    return url


def filterByHours(restaurants, hour):
    
    filtered_restaurants = []

    for restaurant in restaurants:
        start_time, _ = restaurant.get("start24").split(":")
        end_time, _ = restaurant.get("end24").split(":")
        
        if start_time < hour and end_time > hour:
            filtered_restaurants.append(restaurant)

    return filtered_restaurants


def sortRestaurants(restaurant):
    return restaurant.get("applicant")

if __name__ == "__main__":

    # Construct query to socrata
    weekday = getWeekday()
    hour = getHour()
    url = constructQuery(hour, weekday)

    # Make call to socrata for restaurants open now
    response = requests.get(url)

    # Filter by hours

    # Successful call
    if response.status_code == 200:
        
        txt = response.text
        all_restaurants  = json.loads(txt)
        restaurants = filterByHours(all_restaurants, hour)
        restaurants.sort(key=sortRestaurants)

        count = 1

        # Initialize to any value that is not None
        user_continue = ""

        while(user_continue is not None):
            for i in range(count, count + 10):
                if(len(restaurants) >= i):
                    restaurant = restaurants[i-1]
                    print(f"{i}) {restaurant.get('applicant')}")
                    print(f"\t Address: {restaurant.get('location')}")
                    print(f"\t Opens: {restaurant.get('start24')}")
                    print(f"\t Closes: {restaurant.get('end24')} \n")
                else:
                    print("End of list, bon appetit!")
                    exit()
            count += 10
            user_continue = input('Click any button to continue: ')


    else:
        print("Error while making request to socrata")