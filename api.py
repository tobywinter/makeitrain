from flask import Flask
from algorithm import Algorithm
from flask import render_template

api = Flask(__name__)

@api.route("/")
def welcome():
    alg = Algorithm('data_extracted_features_without_headers.csv')
    result = alg.svc(1037654500,5543.3100097,5810.04599608,0.346375000000003,-0.005397)
    accuracy = alg.accuracy()
    return render_template('index.html', result=result, accuracy=accuracy)

@api.route('/api/result', methods=['GET'])
def get_results():
    return render_template('index.html')

if __name__ == '__main__':
    api.run(debug=True)
