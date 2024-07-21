import asyncio
from aiohttp import ClientError, ClientSession
from flask import Flask, jsonify

app = Flask(__name__)

async def fetch_with_retry(session, url, max_retries=3):
   for attempt in range(max_retries):
       try:
           async with session.get(url) as response:
               response.raise_for_status()
               data = await response.json()
               return data
       except ClientError as e:
           if attempt == max_retries - 1:
               raise
           await asyncio.sleep(2 ** attempt)  # Exponential backoff

async def fetch_jokes():
   async with ClientSession() as session:
       tasks = [fetch_with_retry(session, 'https://api.chucknorris.io/jokes/random') for _ in range(10)]
       return await asyncio.gather(*tasks)

@app.route('/getJokes', methods=['GET'])
async def get_jokes():
   try:
       jokes = await fetch_jokes()
       jokes = [joke['value'] for joke in jokes if joke]
       return jsonify(jokes)
   except Exception as e:
       return jsonify({"error": f"Error fetching jokes: {str(e)}"}), 500

if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True, use_reloader=False)
