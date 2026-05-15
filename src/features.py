def create_features(train_df, test_df):

    train_df["TotalArea"] = train_df["GrLivArea"] + train_df["TotalBsmtSF"]
    test_df["TotalArea"] = test_df["GrLivArea"] + test_df["TotalBsmtSF"]

    train_df["HouseAge"] = 2026 - train_df["YearBuilt"]
    test_df["HouseAge"] = 2026 - test_df["YearBuilt"]

    train_df["BathPerRoom"] = train_df["FullBath"] / train_df["TotRmsAbvGrd"]
    test_df["BathPerRoom"] = test_df["FullBath"] / test_df["TotRmsAbvGrd"]

    train_df["HasGarage"] = (train_df["GarageCars"] > 0).astype(int)
    test_df["HasGarage"] = (test_df["GarageCars"] > 0).astype(int)

    return train_df, test_df