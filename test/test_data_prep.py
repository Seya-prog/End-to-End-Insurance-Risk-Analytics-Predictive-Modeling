import pandas as pd
from scripts.data_prep import basic_feature_engineering

def test_basic_feature_engineering():
    df = pd.DataFrame(
        {
            "TotalClaims": [0, 1500],
            "TotalPremium": [1000, 2000],
            "RegistrationYear": [2020, 2018],
            "SumInsured": [10000, 20000],
        }
    )
    engineered = basic_feature_engineering(df)
    assert "HasClaim" in engineered.columns
    assert engineered["HasClaim"].tolist() == [0, 1]
    assert "LossRatio" in engineered.columns
    # First row 0/1000 -> 0, second 1500/2000=0.75
    assert engineered["LossRatio"].iloc[1] == 0.75
