"""Utility functions for loading and preparing the insurance dataset.

Placed in scripts/ so they can be imported by notebooks and tests:
    from scripts.data_prep import read_dataset, basic_feature_engineering
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

__all__ = ["read_dataset", "basic_feature_engineering"]


def read_dataset(path: str | Path) -> pd.DataFrame:
    """Read raw txt/csv file using automatic delimiter detection (|, comma, tab).

    Returns a DataFrame; raises ValueError if delimiter cannot be inferred.
    """
    path = Path(path)
    for sep in ("|", ",", "\t"):
        try:
            df_tmp = pd.read_csv(path, sep=sep, low_memory=False)
            # heuristic: if we get more than one column, delimiter is correct
            if df_tmp.shape[1] > 1:
                return df_tmp
        except Exception:
            continue
    raise ValueError(f"Unable to read {path}. Unknown delimiter.")


def basic_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Add common engineered columns used by notebooks/tests.

    Adds:
        HasClaim   – 1 if TotalClaims > 0 else 0
        LossRatio  – TotalClaims / TotalPremium (NaN if premium is 0)

    Returns a copy of the input DataFrame with new columns.
    """
    df = df.copy()
    df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"].replace(0, pd.NA)
    return df
