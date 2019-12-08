# export FLASK_APP=a_simpleserver.py
#  python -m flask run
# use week 5 as a reference
from flask import Flask, jsonify,  request, abort, make_response
from zfilmDAO import filmDAO

app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def hello_world():
    return 'Hello, Rita!'

# curl "http://127.0.0.1:5000/films/124"


@app.route('/films')

# curl "http://127.0.0.1:5000/films"
def getAll():
    results = filmDAO.getAll()
    return jsonify(results)


# curl "http://127.0.0.1:5000/films/2"
@app.route('/films/<int:id>')
def findById(id):
    foundFilm = filmDAO.findByID(id) 

    return jsonify(foundFilm)


# curl -X POST  "http://127.0.0.1:5000/films"

## curl -i -H "Content-Type:application/json" -X POST -d '{"Title": "Memento", "Director": "Christopher Nolan", "Year": 2000}' http://127.0.0.1:5000/films
@app.route('/films',methods=['POST'])
def create():
    if not request.json:
        abort(400)
    # other checking that it is correct formatted for more marks
    film = {
        "title": request.json['title'],
         "director": request.json['director'],
          "year": request.json['year']
    }
    values = (film['title'], film['director'], film['year'])
    newId = filmDAO.create(values)
    film['id'] = newId 
    return jsonify(film)


#curl -X PUT "http://127.0.0.1:5000/films/124"

# curl -i -H "Content-Type:application/json" -X PUT -d  '{ "Title":"me" }' http://127.0.0.1:5000/films/1


# not working video  finish server to DB 8mins   
# curl -i -H "Content-Type:application/json" -X PUT -d  '{"year":1999}' http://127.0.0.1:5000/films/4
@app.route('/films/<int:id>',methods=['PUT'])
def update(id):
 
    foundFilm = filmDAO.findByID(id) 
    if not foundFilm:
        abort(404)

    if not request.json:
        abort(400)

    reqJson = request.json
    #if 'price' in reqJson and type(reqJson['price']) is not int:
      #  abort(400)

    if "title" in reqJson:
        foundFilm["title"]= request.json["title"]
    
    if 'director' in reqJson:
        foundFilm["director"]= request.json["director"]
    
    if "year" in reqJson:
        foundFilm["year"]= request.json['year']
    values = (foundFilm["title"], foundFilm["director"], foundFilm["year"], foundFilm["id"])
    
    filmDAO.update(values)

    return jsonify(foundFilm)




#  curl -X DELETE http://127.0.0.1:5000/films/4

@app.route('/films/<int:id>',methods=['DELETE'])
def delete(id):
    filmDAO.delete(id) 
    return jsonify({"done":True})


if __name__ == '__main__':
    app.run(debug=True)    