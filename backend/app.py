import sqlite3
from unittest import result
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        pass  # Handle GET all Request. Pass is that will be implemented later
    elif request.method == 'POST':
        data = request.json
        #data = request.form
        print(data)
        result = ""
        #result = add_song(data['artist'], data['title'], data['rating'])
        return jsonify(result)


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(song_id):
    if request.method == 'GET':
        pass  # Handle GET single request
    elif request.method == 'PUT':
        pass  # Handle UPDATE request
    elif request.method == 'DELETE':
        pass  # Handle DELETE request


if __name__ == '__main__':
    app.debug = True
    app.run()

# helper functions

def add_song(artist, title, rating):
    try:
        with sqlite3.connect('backend/db/songs.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO songs (artist, title, rating) values (?, ?, ?);
                """, (artist, title, rating,))
            result = {'status': 1, 'message': 'Song Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result
