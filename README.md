
# Water Potability Prediction


## Problem Statement
Due to insufficient access to safe drinking water, caused by factors like microbial and chemical contamination, pollution from industrial and agricultural sources, and inadequate infrastructure, there have been widespread health problems, economic losses, and social disparities. Particularly, in developing countries such as India, water is not properly utilised for its quality. This project applies various machine learning techniques to predict the water quality. It focuses on finding water potability in a binary output(yes/no) when provided with the key factors used to calculate the water quality index for the water sample, like pH value, electrical conductivity, total organic carbon, hardness, turbidity, total dissolved solids and other salts concentration. Determining or predicting the potability of water would not only ensure access to safe drinking-water but also provide a component of effective policy for health protection.


## Dataset Description
The dataset is taken or can be downloaded from this [link](https://www.kaggle.com/datasets/adityakadiwal/water-potability). A copy of the dataset ([_water_potability.csv_](https://github.com/soumen7saha/water-potability-prediction/blob/main/data/water_potability.csv)) is added in the repository. It has a total 10 features with _Potability_ as the target feature consisting of only 2 values (1 for Potable and 0 for Not Potable). The columns are described and represented as:

- pH: The pH value of the water sample, evaluating its acid-base balance 
- Hardness: Concentration of potassium and magnesium salts in water in terms of ppm(parts per million)
- Solids/TDS (Total Dissolved Solids): Concentration of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc in mg/L or ppm
- Chloramines: Concentration of chemical disinfectants used in drinking water, created by adding ammonia to chlorine in ppm
- Sulfate: Sulfate concentration of the water in mg/L
- Conductivity: Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current, given in μS/cm
- Organic_carbon: Total Organic Carbon (TOC) in water comes from decaying natural organic matter (NOM) as well as synthetic sources, measured in gm/L
- Trihalomethanes(THMs): THMs are chemicals which may be found in water treated with chlorine, given as units of mg/L
- Tubidity: Measure of light emitting properties of water, indicating the quality of waste discharge with respect to colloidal matter in terms of NTU (Nephelometric Turbidity Unit)
- Potability: Indicates if the water is safe for human consumption, ∈ {1,0}


## EDA Summary
- Data Cleaning and Preprocessing:
    Handling Missing Values: All the rows containing any null values are dropped and the dataset has been reduced to 2011 rows. The dataset is split into train/val/test datasets at 60%/20%/20%. The EDA is performed on the full training dataset (80%) 
- Univariate Analysis: 
    The dataset has around 1200 (around 60%) rows with Potability value 0 and 811 (40%) rows with value 1. The mutual information score for all the features with respect to the target variable is equal and independently correlated with it. The distribution of all the features are normal and not highly skewed, hence the outliers are kept intact.
- Bivariate Analysis:
    No two feature columns are correlated to each other, all are independent to each other. The correlation value ranges from 0 to 0.1
- Visualizations:
     
    a. Heat Map
    ![](/images/heat_map.png)

    b. Scatter Plot
    ![](/images/scatter_plot.png)


## Modelling Approach & Metrics
| Model | Hyperparameters | Accuracy Score | ROC_AUC_Score |
| --- | --- | --- | --- |
| Logistic Regression | solver='liblinear', C=0.0001, max_iter=1000, random_state=28 | 0.637 | 0.503 |
| Decision Tree Classifier | max_depth=6, min_samples_leaf=20 | 0.612 | 0.572 |
| Random Forest Classifier | max_depth=10, n_estimators=150, random_state=28, n_jobs=-1 | 0.634 | 0.585 |
| XGBoost | eta': 1.0, 'max_depth': 10, 'min_child_weight': 3, 'objective': 'binary:logistic', 'eval_metric': 'auc', 'nthread': 8, 'seed': 1, 'verbosity': 1 | 1.0 | 0.62 |

Different classification based ML models are trained and evaluated on the basis of accuracy and its performance on the validation set. The model with the maximum roc_auc_score is selected as final best model, re-trained on full train dataset and exported to [models/model.bin](https://github.com/soumen7saha/water-potability-prediction/blob/main/models/model.bin)


## How to run locally?
- Clone the Project from git
    
        git clone https://github.com/soumen7saha/water-potability-prediction.git

- Make sure you have the python version specified in [pyproject.toml](https://github.com/soumen7saha/water-potability-prediction/blob/main/pyproject.toml) and pip (pip installs packages) in the local system

- Install uv using pip

        pip install uv

- Go to the project directory, open terminal & run

        uv sync

- Activate the uv environment
    
        source .venv/bin/activate

- Make sure the port _9696_ is not allocated to any process
    
- Run
    
        python ./main.py


## How to run via Docker?
-   Go to the project directory in terminal and run the following commands:

        cat Dockerfile
	    docker build -t water-potability-prediction .
	    docker run -it --rm -p 9696:9696 water-potability-prediction


## API Usage Examples
- Move to the project directory and open terminal
- Run the following commands in terminal (in separate tabs/windows)

        python ./src/scripts/predict.py
	
		python ./tests/test.py
		
        curl -X 'POST' \
        'http://0.0.0.0:9696/predict' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "ph": 8.3,
        "hardness": 183.6,
        "solids": 20316,
        "chloramines": 7.0,
        "sulfate": 322,
        "conductivity": 295,
        "organic_carbon": 13,
        "trihalomethanes": 62.4,
        "turbidity": 4.2
        }'


## User Interface
- User Input

    ![](/images/input.png)

- Prediction Output

    ![](/images/output.png)


## Architecture Diagram
![](/images/Diagram1.png)


## Known Limitations & Next Steps
Despite the achievements outlined in this project, there remain opportunities for enhancement. For instance, we could gather additional training samples to enhance the model's stability, and further advancements in the prediction model are feasible. These challenges could be addressed in subsequent research, potentially through the application of alternative algorithms like neural networks.