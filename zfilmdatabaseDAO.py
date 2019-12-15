import requests
import json

class FilmdatabaseDAO:

    def __init__(self):
        self.film_database = "www.omdbapi.com"
        self.film_apikey = "59a1bcba"
        

    def findByexpr(self, expr):
        film_name = expr
        self.film_database = "www.omdbapi.com"
        self.film_apikey = "59a1bcba"
        film_url = "http://{}/?apikey={}&t={}&plot=full&r=json".format(self.film_database, self.film_apikey, film_name)
        response = requests.get(film_url)
        json_data = json.loads(response.text)
        return json_data
        #x = json_data
        #return x
        # print('\n')
        # print("################################# Final Result #################################")
        # print('\n')
        # print("Name : " + x['Title'])
        # print("Year :" + x['Year'])
        # print("Director :" + x['Director'])
        # print("Cast :" + x['Actors'])
        # print("Writer :" + x['Writer'])
        # print("Poster :" + x['Poster'])
        # print("Plot :" + x['Plot'])
        # print("Genre :" + x['Genre'])
        # print("Runtime : " + x['Runtime'])
        # print("Internet Movie Database : " + x['Ratings'][2]['Value'])
        # print('\n')
        # print('\n')
        # return 0;
        quit()


filmdatabaseDAO = FilmdatabaseDAO()

