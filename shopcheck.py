import requests
import json
import datetime


def jprint(obj):
    # Creates a formatted string of the Python JSON object.
    # Not neccessary for the project itself, but convinent when debugging.
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_parameters():
    # Simply gets all the parameters neccessary for the GET-request.
    parameters = {

        "q": str(input("Where would you like to check? ")),
        "appid": "430bff2dbcf98539d1f52ea4ab99f4cf",            # I hope no-one steals my incredibly valuable API-key
        "cnt": 1,
        "units": "metric"

    }
    return parameters


def get_response():
    link = "https://api.openweathermap.org/data/2.5/weather?"
    while True:
        response = requests.get(link, get_parameters())
        # Checks if the city exists, and loops if it does not.
        if response.json()["cod"] == "404":
            print("Not a real city, try again.")
        else:
            return response


def print_beverage(temp):
    # Determines an approptiate beverage, with respect to the temperature.
    if temp < 10:
        print("Because of the cold outside, you should probably serve some hot beverages, such as coffee, or tea.")
    elif temp > 20:
        print("Because of the warmth outside, you should probably serve some cold beverages, such as ice tea, or soda.")
    else:
        print("You could probably get away with selling any beverage, considering the average temperature.")


def print_food(weather):
    # Determines what kind of food should be served, using a dictionary.
    food = {

        "Thunderstorm": "Considering the thunderstorm outside, you could serve some warm sweets, such as brownies, or muffins.",
        "Drizzle": "Considering the light percipitation outside, you could serve some warm food, such as spaghetti and meatballs.",
        "Rain": "Considering the rain outside, you could serve some fresh bread, and the likes.",
        "Snow": "Considering the snowing outside, you could serve some sweet hot food, like pancakes, or waffles.",
        "Clear": "Considering the clear skies, you could serve simple foods, like beef, or pork.",
        "Clouds": "Because of the overcast, you could serve warm soups."

    }
    print(food[weather])


def print_drinks(localtime):
    # Uses the fact that the icon response changes depending on the time of day.
    if localtime == "n":
        print("Considering how late it is, you could probably get away with serving some alcoholic beverages.")
    else:
        print("Considering it's daytime, you could serve some juice.")


def print_price():
    # Checks the proximity to payday to determine if the prices can be increased or decreased.
    date = int(datetime.date.today().strftime("%d"))
    days_since_payday = (date-25) % 30
    if days_since_payday < 10:
        print("Because of the recent payday, you could possibly increase the prices somewhat.")
    elif days_since_payday > 20:
        print("Because of how late in the month it is, maybe you should lower the prices slightly.")
    else:
        print("You should offer normal prices.")


def run():
    # Uses the Requests library to query the API.
    response = get_response()
    # Collects the response and stores variables.
    temp = response.json()["main"]["temp"]
    weather = response.json()["weather"][0]["main"]
    localtime = response.json()["weather"][0]["icon"][2]

    # Prints the different stored variables, good for debugging.
    # print("It is currently " + weather + " and " + str(temp) + " degrees celcius. " + "It is currently " + localtime)

    # Prints all the tips.
    print_food(weather)
    print_beverage(temp)
    print_drinks(localtime)
    print_price()


if __name__ == "__main__":
    run()
