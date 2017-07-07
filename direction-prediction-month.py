import numpy as np
import pandas

filename = 'month-prediction-data-without-headers.csv'
names = ["2 Day Net Diff FTSE","10 Day Av FTSE", "20 Day Av FTSE", "50 Day Av FTSE", "Volume FTSE", "2 Day Net Diff GBP", "50 Day Av GBP", "10 Day Av GBP", "20 Day Mv GBP","Label Class"]
dataset = pandas.read_csv(filename, names=names)
array = dataset.values
X = array[:,0:9]
y = array[:,9]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=30)

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

print('Prediction')
print(clf.predict([[-84.1000969999996, 5206.8499025, 5233.8649415, 4880.5259961,	930392000, 0.00697100000000006, 1.04851828, 0.8955676, -167.400390000001]]))
