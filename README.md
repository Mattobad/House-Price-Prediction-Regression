### House price prediction 

Initially, the repo was started as House Regression prediction submission containing experimental jupyter notebooks which 
can be found in the jupyter_notebooks submodule.
- [Model buidling without Feature Selection Technique: Base Model](https://github.com/Mattobad/House-Price-Prediction-Regression/blob/master/jupyter_notebooks/End-to-End-Housing-Price-Prediction-without-feature-selection.ipynb)
- [Model buidling with Feature Selection Technique](https://github.com/Mattobad/House-Price-Prediction-Regression/blob/master/jupyter_notebooks/End-to-End%20ML%20project%20with%20Feature%20Selection%20techniques.ipynb)

Now, expanded the repo with following steps for deploying the model in production:

:white_check_mark: Exploratory Analysis(Feature Engineering, Feature Selection, Hyperparameter optimization, Model development)

:white_check_mark: Building Machine Learning Pipeline(Scikit-learn pipeline Architecture)

:white_check_mark: Model API development(Serving model through RESTful API)

:white_check_mark: Deploying to production(Web App)

If you want reproduce the project, you can use requirements text file to setup a conda environment in the local machine.

App is live in the link [here.][applink]

Note: Checkout the publishingApp branch to see the code used for deployment of the project. Project is live through free tier from PythonAnywhere. Only the end-point of API is deployed in the PythonAnywhere server.


## Code and Resources Used
**Python Version:** 3.7

**Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, randomforest-regressor, RandomizedSearchCV, scikit-learn pipeline, pytest

**Backend:** Flask

**Frontend:** HTML,CSS,JS

**Resources:** [Udemy: Deployment of Machine Learning Models][course1]

[course1]:https://www.udemy.com/course/deployment-of-machine-learning-models/
[applink]:https://bit.ly/house-project-live

