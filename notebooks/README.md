
# Notebooks Guide

| Notebook | Task | Description |
|----------|------|-------------|
| `task1_eda.ipynb` | 1 & 2 | Exploratory analysis **and** data preparation / feature engineering (adds HasClaim, LossRatio, etc.). |
| `hypothesis_testing.ipynb` | 3 | Non-parametric hypothesis tests on Loss Ratio. Includes multi-group (province, zip) and control-vs-test segmentation. |
| `modeling.ipynb` | 4 | Claim-severity regression, claim-probability classification, SHAP interpretation, risk-based premium illustration. |

Run notebooks in sequential order; each one relies on variables or processed data produced by the previous.

Dataset expected at `data/MachineLearningRating_v3.txt` (pull via `dvc pull`).
