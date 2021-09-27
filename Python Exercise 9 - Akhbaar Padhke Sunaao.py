# Akhbaar Padhke Sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Welcome to worlds best news channel, Namaste India!")
    speak("Latest News Headlines.. Lets Begin")
    url = "https://saurav.tech/NewsAPI/top-headlines/category/health/in.json"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")