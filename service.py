import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()
# This is how we are calling the model. likewise you can call multiple models.

svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner])
# This is how we are creating service and listing out all the models inside runners as a list.
# (as of now we have only one runner(model))

# Now we create a svc service decorator and flask like function inside it.
@svc.api(input=NumpyNdarray(),output=NumpyNdarray())
def classify(input_series:np.ndarray)->np.ndarray:
    result = iris_clf_runner.predict.run(input_series)
    return result

