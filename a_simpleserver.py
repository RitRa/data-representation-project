# export FLASK_APP=a_simpleserver.py
#  python -m flask run
# use week 5 as a reference
from flask import Flask, jsonify,  request, abort, make_response






app = Flask(__name__, static_url_path='', static_folder='.')

films=[{"id":1, "Title": "Harry Potter", "Director": "JK", "Price": 1000},
{"id":2, "Title": "The Quiet American", "Director": "Greene", "Price": 800},
{"id":3, "Title": "Something Steamy", "Director": "Jackie Collins", "Price": 1100}]

NextId = 4

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

# curl "http://127.0.0.1:5000/films/124"


@app.route('/films')

# curl "http://127.0.0.1:5000/films"
def getAll():
    return jsonify(films)

@app.route('/films/<int:id>')
def findById(id):
    foundfilms = list(filter(lambda b:b['id']==id, films))
    if len(foundfilms) == 0:
        return jsonify ({}) , 204
    return jsonify (foundfilms[0])

# curl -X POST  "http://127.0.0.1:5000/films"

## curl -i -H "Content-Type:application/json" -X PUT -d '{"Title": "Harry Potter2", "Director": "JK", "Price": 1000}' http://127.0.0.1:5000/films
@app.route('/films',methods=['POST'])
def create():
    global NextId
    if not request.json:
        abort(400)
    #other checking that it is correct formatted for more marks
    film = {
        "id": NextId,
        "Title": request.json['Title'],
         "Director": request.json['Director'],
          "Price": request.json['Price']
    }
    NextId += 1
    films.append(film)
    return jsonify(film)

    return "in create"

#curl -X PUT "http://127.0.0.1:5000/films/124"

# curl -i -H "Content-Type:application/json" -X PUT -d  '{ "Title":"me" }' http://127.0.0.1:5000/films/1
    
# curl -i -H "Content-Type:application/json" -X PUT -d  '{"Title":"ritt","Director":"Ruta", "Price":34 }' http://127.0.0.1:5000/films/1
@app.route('/films/<int:id>',methods=['PUT'])
def update(id):
    foundfilms = list(filter(lambda t:t['id']==id, films))
    if (len(foundfilms) == 0):
        abort(404)
    foundfilm = foundfilms[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if "Title" in reqJson:
        foundfilm["Title"] =reqJson['Title']
    if 'Director' in reqJson:
        foundfilm['Director'] = reqJson['Director']
    if "Price" in reqJson:
        foundfilm["Price"] =reqJson['Price']

    return jsonify(foundfilm)



    return "in update for id" +str(id)

#  curl -X DELETE http://127.0.0.1:5000/films/1

@app.route('/films/<int:id>',methods=['DELETE'])
def delete(id):
    foundfilms = list(filter(lambda t:t['id']==id, films))
    if (len(foundfilms) == 0):
        abort(404)
    films.remove(foundfilms[0])
    return jsonify({"done":True})

    return "in delete for id" +str(id)

if __name__ == '__main__':
    app.run(debug=True)    