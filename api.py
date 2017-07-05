from flask import Flask, jsonify

api = Flask(__name__)

result = [
    {
        'id': 1,
        "date": '2017-06-20',
        "gbp": 1.234,
        "ftse": 7.7123,
        "raise": False,
    }
]

@api.route('/makeitrain/api/result', methods=['GET'])
def get_results():
    return jsonify({'result': result})


if __name__ == '__main__':
    api.run(debug=True)
