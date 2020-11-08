
# data
TRAINING_DATA_FILE = "../train.csv"
PIPELINE_NAME = 'random_forest_regressor'

TARGET = 'SalePrice'

# input variables 
# FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
#             'OverallQual', 'OverallCond', 'YearRemodAdd',
#             'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
#             'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
#             'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
#             'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
#             'LotFrontage',
#             # this one is only to calculate temporal variable:
#             'YrSold']

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

# numerical variables with NA in train set (this should be auto implemented as required)
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

# categorical variables with NA in train set
# CATEGORICAL_VARS = ['MasVnrType', 'BsmtQual', 'BsmtExposure',
#                             'FireplaceQu', 'GarageType', 'GarageFinish']
CATEGORICAL_VARS = ['ExterQual', 'KitchenQual', 'BsmtQual', 'BsmtFinType1', 
                    'Neighborhood', 'RoofStyle','PavedDrive']

TEMPORAL_VARS = 'YearRemodAdd'

# variables to log transform
NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# categorical variables to encode
# CATEGORICAL_VARS = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType',
#                     'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
#                     'KitchenQual', 'FireplaceQu', 'GarageType', 'GarageFinish',
#                     'PavedDrive']




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


