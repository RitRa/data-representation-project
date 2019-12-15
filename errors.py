from flask import Flask, jsonify, request, abort, make_response, render_template, redirect, url_for
from zfilmDAO import filmDAO
from zUserDAO import userDAO
from application import app

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
