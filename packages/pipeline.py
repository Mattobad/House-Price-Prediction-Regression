from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


import preprocessors as pp
import config

price_pipe = Pipeline(
    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
         
        ('numerical_inputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
         
        ('temporal_variable',
            pp.TemporalVariableEstimator(
                variables=config.TEMPORAL_VARS,
                reference_variable=config.DROP_FEATURES)),
         
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=config.CATEGORICAL_VARS)),
         
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
         
        ('log_transformer',
            pp.LogTransformer(variables=config.NUMERICALS_LOG_VARS)),
         
        ('drop_features',
            pp.DropUnecessaryFeatures(variables_to_drop=config.DROP_FEATURES)),

        
        ('std_scaler',StandardScaler()),
        ('random_forest_model', RandomForestRegressor(n_estimators=config.MODEL_PARAMS["n_estimators"],
                                   min_samples_leaf=config.MODEL_PARAMS["min_samples_leaf"],
                                   min_samples_split=config.MODEL_PARAMS["min_samples_split"],
                                   max_features=config.MODEL_PARAMS["max_features"],
                                   n_jobs=config.MODEL_PARAMS["n_jobs"],
                                    max_depth =config.MODEL_PARAMS["max_depth"],
                                    bootstrap= config.MODEL_PARAMS["bootstrap"],
                                   random_state=42) # so our results are reproducible
                                   )
    ]
)