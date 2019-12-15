import requests
import json

def movie():
    try:
        movie_name = input("please enter the movie name: ")
        if movie_name == "":
            print('\ndo not enter empty string for movie name', 'red', attrs=['blink'])
        movie_database = "www.omdbapi.com"
        movie_apikey = "59a1bcba"
        movie_url = "http://{}/?apikey={}&t={}&y={}&plot=full&r=json".format(movie_database, movie_apikey, movie_name, movie_year)
        response = requests.get(movie_url)
        json_data = json.loads(response.text)
        x = json_data
        print('\n')
        print("################################# Final Result #################################")
        print('\n')
        print("Name : " + x['Title'])
        print("Year :" + x['Year'])
        print("Director :" + x['Director'])
        print("Cast :" + x['Actors'])
        print("Writer :" + x['Writer'])
        print("Poster :" + x['Poster'])
        print("Plot :" + x['Plot'])
        print("Genre :" + x['Genre'])
        print("Runtime : " + x['Runtime'])
        print("Internet Movie Database : " + x['Ratings'][2]['Value'])
        print('\n')
        print('\n')
        return 0;
        quit()
    except (KeyError, KeyboardInterrupt, NameError, EOFError) as error:
        print('Could not get in the database please try again')
    except IndexError as error:
        print('something wrong while fetching the details')

def main():
    movie()


if __name__ == "__main__":
    main()

