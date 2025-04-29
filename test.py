import bentoml

iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()
iris_clf_runner.init_local()
#this will take the latest model that got saved and run it.
#once the model is read, now we can predict the values of it.
out_put = iris_clf_runner.predict.run([[5.9,3,5.1,1.8]])
print(out_put)

