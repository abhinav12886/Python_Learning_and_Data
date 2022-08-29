# Akhbaar padhkar sunao
# it is a program which reads and speaks out news using the news REST API

import requests
import json


def speak(str):
    """
    This function will speak out the news.......
    """
    #There are several APIs available to convert text to speech in python.
    # One of such APIs available in the python library commonly known as win32com library.
    # It provides a bunch of methods to get excited about and one of them is the Dispatch
    # method of the library. Dispatch method when passed with the argument of SAPI.SpVoice
    # It interacts with the Microsoft Speech SDK to speak what you type in from the keyboard.
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    speak("News is going to start")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=**********************"
    # url contains the url of and api key of the news REST API
    news = requests.get(url).text  # It will get the the text of the url
    news_dict = json.loads(news)  # it will convert json string to python dictionary object
    arts = news_dict["articles"]  # it will take the values corresponding to "articles" key from dictionary
    for articles in arts:  # this loop will iterate over the values corresponding to keys
        speak(articles['title'])  # it will speak out the "title" keys values.
        print(articles['title'])
        speak("Moving on to the next news ")

    speak("Thanks for listening...")

# At the place of '*' you have to enter your api key obtained from 'newsapi.org' site using get api key option


