# app.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

def is_valid_zip(zip_code):
    # Very basic zip code validation
    return zip_code.isdigit() and len(zip_code) == 5

@app.route('/api/v1/weather/<zip_code>', methods=['GET'])
def get_weather(zip_code):
    # Check if the zip code is valid
    if not is_valid_zip(zip_code):
        return jsonify({'error': 'Invalid zip code format'}), 400

    # For simplicity, generate random high and low temperatures
    high_temp = random.randint(70, 100)
    low_temp = random.randint(40, 70)

    # Create a JSON response
    response = {
        'zip_code': zip_code,
        'high_temp': high_temp,
        'low_temp': low_temp
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
