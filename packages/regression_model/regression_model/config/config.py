from pathlib import Path
import os



PACKAGE_ROOT =Path(os.getcwd())
TRAINED_MODEL_DIR = os.path.join(PACKAGE_ROOT,"regression_model","trained_models")
DATASET_DIR = os.path.join(PACKAGE_ROOT,"regression_model","datasets") 


# data
TRAINING_DATA_FILE = "train.csv"
TESTING_DATA_FILE = "test.csv"


TARGET = 'SalePrice'

# input variables 
FEATURES = ['OverallQual','GrLivArea','GarageCars','TotalBsmtSF',
            'ExterQual','BsmtFinSF1','2ndFlrSF','LotArea',
            'FullBath','KitchenQual','YearBuilt','BsmtQual',
            'YearRemodAdd','MasVnrArea','BsmtUnfSF','LotFrontage',
            'OpenPorchSF','WoodDeckSF','Fireplaces','BsmtFinType1',
            # add variables beside 
            'Neighborhood','1stFlrSF','RoofStyle','PavedDrive',
            'YrSold']


# this variable is to calculate the temporal variable,
# must be dropped afterwards
DROP_FEATURES = 'YrSold'

# numerical variables
NUMERICAL_VARS = ['OverallQual',
                'GrLivArea',
                'GarageCars',
                'TotalBsmtSF',
                'BsmtFinSF1',
                '2ndFlrSF',
                'LotArea',
                'FullBath',
                'YearBuilt',
                'YearRemodAdd',
                'MasVnrArea',
                'BsmtUnfSF',
                'LotFrontage',
                'OpenPorchSF',
                'WoodDeckSF',
                'Fireplaces',
                '1stFlrSF']

# categorical variable

CATEGORICAL_VARS = ['ExterQual', 'KitchenQual', 'BsmtQual', 'BsmtFinType1', 
                    'Neighborhood', 'RoofStyle','PavedDrive']

TEMPORAL_VARS = 'YearRemodAdd'

# variables to log transform
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']


# model parameters
MODEL_PARAMS = {
    "n_estimators":410,
    "min_samples_leaf":1,
    "min_samples_split":10,
    "max_features":0.5,
    "n_jobs":-1,
    "max_depth" :10,
    "bootstrap": False
}


