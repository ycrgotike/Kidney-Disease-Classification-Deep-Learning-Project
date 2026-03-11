# Kidney Disease Classification MLFlow DVC Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.11 -y
```

```bash
conda activate kidney
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project.mlflow \
MLFLOW_TRACKING_USERNAME=<your_dagshub_username> \
MLFLOW_TRACKING_PASSWORD=<your_dagshub_access_token> \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project.mlflow

export MLFLOW_TRACKING_USERNAME=<your_dagshub_username> 

export MLFLOW_TRACKING_PASSWORD=<your_dagshub_access_token>

```

### DVC cmd

1.dvc init
2.dvc repro
3.dvc dag

## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# Deployment
- This project can be deployed using:
	- Render
	- AWS EC2 + Docker
	- Heroku
	- HuggingFace Spaces

-Example start command for deployment:gunicorn app:app

# Tech Stack
- Python
- TensorFlow
- Flask
- MLflow
- DVC
- Scikit-learn
- Pandas
- NumPy