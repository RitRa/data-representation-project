# export FLASK_APP=application.py
# python -m flask run
# use week 5 as a reference
from flask import Flask, jsonify, request, abort, make_response, render_template, redirect, url_for
from zfilmDAO import filmDAO
#from zUserDAO import userDAO
from zfilmdatabaseDAO import filmdatabaseDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def hello_world():
    return 'Hello, Rita!'

# checking if the user exsits in the database
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != '' or request.form['password'] != '':
            # passing the email and password to the DAO
            email = request.form['email']
            password = request.form['password']
            foundUser = filmDAO.checkUser(email, password)
            # if the user is not in the database, throw the error
            if not foundUser:
                error = 'Invalid Credentials. Please try again.'
            # if the user exists then navigate to the films page    
            else:
                return redirect(url_for('filmviewer'))
        else:
            return error
    return render_template('login.html', error=error)


@app.route('/filmviewer', methods=['GET', 'POST'])
def filmviewer():
        return render_template('filmviewer.html')


# @app.route('/films/<int:id>', methods=['GET', 'POST'])
# def filmdetail(id):
#     if request.method == 'GET':
#         foundFilm = filmDAO.findByID(id)
#         if not foundFilm:
#             abort(400)
#         else:
#             #print("Hello")
#             print("found film", foundFilm)
#             return render_template('filmdetail.html',title='filmdetail', result=jsonify(foundFilm))
#         # Failure to return a redirect or render_template
#     else:
#         return render_template('filmdetail.html')


# @app.route('/filmdetail', methods=['GET', 'POST'])
# def viewerdetail():
#         return render_template('filmviewer.html')


@app.route('/films')
# curl "http://127.0.0.1:5000/films"
def getAll():
    results = filmDAO.getAll()
    return jsonify(results)


# curl "http://127.0.0.1:5000/films/2"
# finding a film
@app.route('/films/<int:id>')
def findById(id):
    foundFilm = filmDAO.findByID(id)
    if not foundFilm:
        abort(400) 

    return jsonify(foundFilm)

# creating a new film
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


# updating a film
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

# delete film
# curl -X DELETE http://127.0.0.1:5000/films/4
@app.route('/films/<int:id>',methods=['DELETE'])
def delete(id):
    filmDAO.delete(id) 
    return jsonify({"done":True})


# searching for a film using the api from www.omdbapi.com
@app.route('/film/search/<expr>', methods=('GET', 'POST'))
def search_film(expr):
    search = { 'expr': expr }
    expr = '%' + expr + '%';
  
    searchfilm = filmdatabaseDAO.findByexpr(expr) 
    if not searchfilm:
        abort(404)
    print(searchfilm)
    #return jsonify(searchfilm)
    return render_template('filmsearch.html', search=search,searchfilm=searchfilm)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)    