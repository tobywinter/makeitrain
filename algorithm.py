import numpy as np
import pandas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class Algorithm:

    def __init__(self, file):
        self.dataset = pandas.read_csv(file)
        self.features = self.dataset.values[ : , 0:len(self.dataset.columns) - 1 ]
        self.label = self.dataset.values[ :, len(self.dataset.columns) - 1 ]
        self.features_train = None
        self.features_test = None
        self.label_train = None
        self.label_test = None
        self.clf = None

    def split_data(self):
        self.features_train, self.features_test, self.label_train, self.label_test = train_test_split(self.features, self.label, test_size=0.25, random_state=42)

    def svc(self, ftse_trade_volume, ten_day_moving_av,fifty_day_moving_av, two_day_netprice_diff, gbp_diff):
        self.split_data()

        self.clf = SVC(C=1.0, cache_size=1000000, class_weight=None, coef0=0.0,
            decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
            max_iter=-1, probability=False, random_state=None, shrinking=True,
            tol=0.001, verbose=False)

        # train algorithm
        self.clf.fit(self.features_train, self.label_train)

        # calculate prediction
        return self.clf.predict([[ftse_trade_volume, ten_day_moving_av,fifty_day_moving_av, two_day_netprice_diff, gbp_diff]])

    def accuracy(self):
        predictions = self.clf.predict(self.features_test)
        return accuracy_score(self.label_test, predictions)


if __name__ == '__main__':
    alg = Algorithm('data_extracted_features_without_headers.csv')
    print(alg.svc(1037654500,5543.3100097,5810.04599608,0.346375000000003,-0.005397))
    print(alg.accuracy())
