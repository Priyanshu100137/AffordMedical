from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

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
            pass

    return jsonify({'numbers': result})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8008)
