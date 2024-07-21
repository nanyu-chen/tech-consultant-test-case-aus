from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/getJokes', methods=['GET'])
def get_jokes():
    jokes = []
    try:
        for _ in range(10):
            response = requests.get('https://api.chucknorris.io/jokes/random')
            print("API Response:", response.text)
            print("Response Status Code:", response.status_code)
            
            try:
                data = response.json()
                print("Parsed JSON data:", data)
                
                if isinstance(data, dict):
                    joke = data.get('value')
                    if joke:
                        jokes.append(joke)
                else:
                    print("Unexpected data format:", data)
            except json.JSONDecodeError:
                print("Failed to parse JSON. Raw response:", response.text)
            
        return jsonify(jokes)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": f"Error fetching jokes: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)