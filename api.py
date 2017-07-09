from flask import Flask
import data_processor
from algorithm import Algorithm
from flask import render_template

api = Flask(__name__)

@api.route("/")

def welcome():
    ten_day_moving_av = data_processor.get_moving_average(10)
    fifty_day_moving_av = data_processor.get_moving_average(50)
    two_day_netprice_diff = data_processor.get_2day_net_price_difference()
    gbp_diff = data_processor.get_gbp_difference()

    alg = Algorithm('daily_prediction_data.csv')
    result = alg.svc(1037654500,ten_day_moving_av,fifty_day_moving_av,two_day_netprice_diff,gbp_diff)
    accuracy = alg.accuracy()

    alg_long = Algorithm('monthly_prediction_data.csv')
    result_long = alg_long.svc(1037654500,ten_day_moving_av,fifty_day_moving_av,two_day_netprice_diff,gbp_diff)
    accuracy_long = alg_long.accuracy()

    return render_template('index.html', result=result, accuracy=accuracy, result_long=result_long, accuracy_long=accuracy_long)


if __name__ == '__main__':
    api.run(debug=True)
