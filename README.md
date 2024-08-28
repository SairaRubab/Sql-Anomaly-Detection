# SQL_QUERY_ANOMALY_DETECTION

This is the code that supplements our Research Paper for a course project. We explored ensemble
learning of state-of-the-art unsupervised models for SQL query anomaly detection to detect various types of anomalies.

## Data

- We used [Kaggle SQL Injection Dataset](https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset)

- We also generated a new dataset of query processing times

## Quick Start Tutorial

### Clone the repository

```
git clone https://github.com/DawarWaqar/sql_query_anomaly_detection.git
```

```
cd sql_query_anomaly_detection
```

### Set up virtual environment

```
python -m venv anomaly_detection_venv
```

```
source anomaly_detection_venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Setup Jupyter

```
pip install jupyter
```

### Run the notebook

```
jupyter notebook
```
