import numpy as np
import pandas

filename = 'monthly-prediction-data-without-headers.csv'
names = ["2 Day Net Diff FTSE","10 Day Av FTSE", "50 Day Av FTSE", "Volume FTSE", "2 Day Net Diff GBP","Label Class"]
dataset = pandas.read_csv(filename, names=names)
array = dataset.values
X = array[:,0:5]
y = array[:,5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=41)

from sklearn.svm import SVC
clf = SVC()
clf.fit(X_train, y_train)
SVC(C=1.0, cache_size=1000000, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print('Accuracy')
print(accuracy_score(y_test, predictions))
