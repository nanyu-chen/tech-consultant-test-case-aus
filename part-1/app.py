from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/getJokes', methods=['GET'])
def get_jokes():
   jokes = []
   try:
       for _ in range(10):
           response = requests.get('https://api.chucknorris.io/jokes/random')
           data = response.json()
           joke = data.get('value')
           if joke:
               jokes.append(joke)
       return jsonify(jokes)
   except Exception as e:
       return jsonify({"error": f"Error fetching jokes: {str(e)}"}), 500

if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True)