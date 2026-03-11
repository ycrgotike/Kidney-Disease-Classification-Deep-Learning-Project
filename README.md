# Kidney Disease Classification MLFlow DVC Project

This project implements an end-to-end machine learning pipeline to classify kidney disease using deep learning models. The trained model is served through a Flask-based web application with MLflow experiment tracking and DVC pipeline orchestration.

## 📋 Overview

This project is a Python-based deep learning application that trains a kidney disease classification model and serves it through a Flask web API. The project incorporates MLflow for experiment tracking, DVC for pipeline orchestration, and is structured for deployment to cloud environments like Render.com.

## 🎯 Project Structure

```
Kidney-Disease-Classification-Deep-Learning-Project/
├── app.py                      # Flask application entry point
├── main.py                     # Main pipeline execution script
├── setup.py                    # Package setup and configuration
├── requirements.txt            # Python dependencies
├── params.yaml                 # Model hyperparameters
├── dvc.yaml                    # DVC pipeline definition
├── Dockerfile                  # Docker containerization
├── .github/workflows/          # GitHub Actions CI/CD
├── src/                        # Source code for ML pipeline
├── research/                   # Jupyter notebooks for development
├── templates/                  # HTML templates for web interface
├── model/                      # Trained model artifacts
├── mlruns/                     # MLflow runs directory
├── config/                     # Configuration files
├── logs/                       # Training logs
├── dvc.lock                    # DVC lock file
├── mlflow.db                   # MLflow database
├── scores.json                 # Model evaluation metrics
└── .gitignore                  # Git ignore rules
```

## 🔧 Technology Stack

- **Python 3.11**
- **TensorFlow** - Deep learning framework
- **Flask** - Web framework for serving the ML model
- **MLflow** - Experiment tracking and model management
- **DVC** - Pipeline orchestration and data versioning
- **Additional libraries** - Scikit-learn, Pandas, NumPy (see requirements.txt)
- **Render.com** - Cloud deployment platform
- **GitHub Actions** - CI/CD automation


## 🚀 Getting Started

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project.git
   ```

2. **Create conda environment:**
   ```bash
   conda create -n kidney python=3.11 -y
   conda activate kidney
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the pipeline:**
   ```bash
   python main.py
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

   The Flask app will start and be accessible at `http://localhost:5000`


## 🔄 Development Workflow

### Steps for Model Development:

1. Update `config/` config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml with hyperparameters
4. Update the entity.py in `src/entity/`
5. Update the configuration manager in `src/config/configuration.py`
6. Update the components in `src/components/`
7. Update the pipeline `src/pipeline/`
8. Update the main.py to execute the complete pipeline
9. Update the dvc.yaml with pipeline stages
10.Run training with `python main.py` or `dvc repro`
11.Monitor experiments with MLflow UI.

## 🤖 MLflow: Experiment Tracking

MLflow enables tracking of all experiments, metrics, and model versions.

### Local MLflow UI

```bash
mlflow ui
```

Access at `http://localhost:5000`

**Features:**
- Track all training experiments
- Log metrics and parameters automatically
- Compare different model runs
- Store model artifacts and versions


### DagsHub Integration 

Connect MLflow to DagsHub for centralized experiment management:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project.mlflow

export MLFLOW_TRACKING_USERNAME=<your_dagshub_username> 

export MLFLOW_TRACKING_PASSWORD=<your_dagshub_access_token>

```
## 📊 DVC: Pipeline Orchestration

DVC provides lightweight pipeline orchestration and data versioning.

### Basic DVC Commands

```bash
# Initialize DVC (already done)
dvc init

# Execute the pipeline
dvc repro

# View pipeline DAG
dvc dag

# Check pipeline status
dvc status
```

**Features:**
- Define reproducible ML pipelines
- Track data and model versions
- Generate pipeline visualizations
- Integrate with Git for version control


## 🌐 Web Application

The Flask application provides a user-friendly interface for kidney disease classification.

### Running Locally

```bash
python app.py
```

Access at `http://localhost:5000`

# Deployment
- This project can be deployed using:
	- Render
	- AWS EC2 + Docker
	- Heroku
	- HuggingFace Spaces

## 📚 Project Components

- **app.py** - Flask application with prediction routes
- **main.py** - Main pipeline execution script
- **src/components/** - Pipeline components (data ingestion, training, evaluation)
- **src/config/** - Configuration manager for loading YAML files
- **research/** - Jupyter notebooks for EDA and model development
- **templates/** - HTML templates for the web interface
- **model/** - Saved trained model artifacts
- **mlruns/** - MLflow experiment tracking data

## 📖 Documentation & Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [TensorFlow Documentation](https://www.tensorflow.org/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👤 Author

**Yashwanth C Reddy**
- Email: gycrgotike@gmail.com
- GitHub: [ycrgotike](https://github.com/ycrgotike)
- Version: 1.0.0

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

For more information, visit: [GitHub Repository](https://github.com/ycrgotike/Kidney-Disease-Classification-Deep-Learning-Project)
