# Understanding of BentoML

## BentoML: A Simple Guide
BentoML is an open-source framework that helps you package, deploy, and manage machine learning models. It makes it easy to take your trained models and turn them into APIs (Application Programming Interfaces) that can be used in applications or services.

## Why Use BentoML?
### Easy Packaging: 
BentoML allows you to package your model along with its dependencies, so you don't have to worry about missing libraries or files when deploying.
### Flexible Deployment: 
You can deploy your model as a REST API, a gRPC service, or even as a serverless function.
### Version Control: 
BentoML helps you manage different versions of your models, making it easy to update or roll back if needed.
### Integration: 
It works well with popular machine learning libraries like TensorFlow, PyTorch, and Scikit-learn.

## Basic Concepts
### Bento: 
A Bento is a packaged model that includes the model itself, any necessary code, and configuration files.
### Service: 
A service is how you expose your model to the outside world, usually as an API.

## Project undersatnding : 
- Install package bentoml and use it.
- in train.py we can see:
    ```python
    bentoml.sklearn.save_model("iris_clf", clf)
  This is how we are going to save the model using BentoML.
- once you run the code, you are going to save the model using bentoml and you will get model tag like below:
    ```python
    - model saved : Model(tag="iris_clf:dzqxbvbfasd5pjk7")
    - this is the unique tag -> dzqxbvbfasd5pjk7
- if you use command "bentoml models list" then you will list out all the models with their tags like below:(as of now we have only one model)
    ```python
    Tag                        Module           Size      Creation Time       
    iris_clf:dzqxbvbfasd5pjk7  bentoml.sklearn  6.03 KiB  2025-04-29 19:43:26
- physically this stores the models in local storage now.
- It stores in the location --> C:\Users\ZE634LD\bentoml\models\iris_clf\dzqxbvbfasd5pjk7
- under this you will have model.yaml and saved_model.pkl files.
- test.py is the file that runs and predicts the values using the saved model from local.
- now you dont need to create flask api's ect.., in bentoml. for that you need to create ```service.py```
- here we are creating api for prediction likewise we can create multiple api's for multiple requirements.
- ```bentoml serve service.py:svc --reload``` by using this command we are going to run bentoml service.
- This service will create api and we can access it to predict the data.
- we can create a package of whole project into ```bento``` so that we can pick this file up and deploy it anywhere.
- for the creation of bento we created a file called ```bentofile.yaml```
- when you run ```bentoml build``` then it will create whole package of this project.
- this will create folder called ```bentos``` in the location and build this package.
    ```python
    C:\Users\ZE634LD\bentoml\bentos\iris_classifier\h7bfqdbfbktk3jk7
- we can list all the bentos using the command ```bentoml list```.
- now you can simply take this project and deploy it anywhere. let it be cloud services or anywhere.
