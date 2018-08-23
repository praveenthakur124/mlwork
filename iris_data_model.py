from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

dict = {0: "setosa", 1: "versicolor", 2: "virginica"}
# train with KNeighborsClassifier
def iris_train(mylist):
    iris = load_iris()
    x = iris.data
    y = iris.target

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x, y)
    result = knn.predict(mylist)

    for k, v in dict.items():
        if k in result:
            print(v)
    y_pred = knn.predict(x)
    print(metrics.accuracy_score(y, y_pred))

# train with LogisticRegression
def iris_tain_log(mylist):
    iris = load_iris()
    x = iris.data
    y = iris.target

    logreg = LogisticRegression()
    logreg.fit(x, y)
    result = logreg.predict(mylist)
    for k, v in dict.items():
        if k in result:
            print(v)
    y_pred = logreg.predict(x)
    print(metrics.accuracy_score(y, y_pred))



mylist = [[2, 3, 1, 4]]
iris_train(mylist)
iris_tain_log(mylist)
