import bentoml

from sklearn import svm
from sklearn import datasets

#load training dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

#train the model
clf = svm.SVC(gamma='scale')
clf.fit(X,y)

#save model to bentoml local model store
saved_model = bentoml.sklearn.save_model("iris_clf", clf)
print(f"model saved : {saved_model}")

