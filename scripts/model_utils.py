"""Common metrics wrappers for modelling notebooks/tests."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, roc_auc_score, f1_score

__all__ = ["rmse", "regression_metrics", "classification_metrics"]


def rmse(y_true, y_pred) -> float:
    """Compute Root Mean Squared Error independent of sklearn `squared` kw."""
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def regression_metrics(y_true, y_pred) -> dict[str, float]:
    return {"rmse": rmse(y_true, y_pred), "r2": r2_score(y_true, y_pred)}


def classification_metrics(y_true, proba, threshold: float = 0.5) -> dict[str, float]:
    y_pred = (proba >= threshold).astype(int)
    return {"roc_auc": roc_auc_score(y_true, proba), "f1": f1_score(y_true, y_pred)}
