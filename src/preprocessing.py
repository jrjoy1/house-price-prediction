import numpy as np

def preprocess(train_df, test_df):

    # Fill missing values
    train_df.fillna(train_df.mean(numeric_only=True), inplace=True)
    test_df.fillna(test_df.mean(numeric_only=True), inplace=True)

    # Remove infinities
    train_df.replace([np.inf, -np.inf], 0, inplace=True)
    test_df.replace([np.inf, -np.inf], 0, inplace=True)

    return train_df, test_df