import numpy as np
import pandas

filename = 'data_extracted_features_without_headers.csv'
names = ["FTSE Trade Volume","10 Day Moving Av","50 Day Moving Av","2-Day NetPrice DIFF","GBP DIFF","Label Class"]
dataset = pandas.read_csv(filename, names=names)
array = dataset.values
X = array[:,0:5]
y = array[:,5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.svm import SVC
clf = SVC()
clf.fit(X_train, y_train)
SVC(C=1.0, cache_size=1000000, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)




predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
