# import the packages
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
import pickle

# load the data
def load_data():
    df = pd.read_csv("../../data/water_potability.csv")
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.dropna()
    return df

# train the model
def train_model(df):
    numerical_cols = ['ph', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity',
       'organic_carbon', 'trihalomethanes', 'turbidity']
    
    xgb_params = {
    'eta': 1.0, 
    'max_depth': 10,
    'min_child_weight': 3,
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
    }

    dv = DictVectorizer(sparse=False)

    train_dict = df[numerical_cols].to_dict(orient='records')
    y_train = df.potability
    X_full_train = dv.fit_transform(train_dict)
    dtrain = xgb.DMatrix(X_full_train, label=y_train, feature_names=list(dv.get_feature_names_out()))
    model = xgb.train(xgb_params, dtrain, num_boost_round=30)
    
    return (dv, model)

# save the model
def save_model(pipeline, filename):
    (dv, model) = pipeline
    with open(filename, 'wb') as f_out:
        pickle.dump((dv,model), f_out)

if __name__ == "__main__": 
    df = load_data()
    pipeline = train_model(df)
    save_model(pipeline, '../../models/model.bin')
    print('Model saved to model.bin')