from flask import Flask, request, jsonify
import requests
from string import Template

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    result = []

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'numbers' in data:
                    result.extend(data['numbers'])
        except Exception as e:
            # Handle invalid or inaccessible URLs gracefully
            pass

    return jsonify({'numbers': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)