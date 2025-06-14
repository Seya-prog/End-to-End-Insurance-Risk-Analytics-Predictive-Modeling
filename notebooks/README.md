# Notebooks Overview

| Notebook | Task | Description |
|----------|------|-------------|
| `task1_eda.ipynb` | 1 | Initial exploration: delimiter detection, sampling, descriptive stats, visualisation of numeric & categorical variables. |
| `hypothesis_testing.ipynb` | 3 | Hypothesis tests on Loss Ratio. Multi-group Kruskal-Wallis + control vs test Mann-Whitney; prints decisions & business interpretations. |
| `modeling.ipynb` | 4 | Severity regression (RF best) + claim-probability classification (XGB best). SHAP explanations and risk-based premium demo. |

Run notebooks sequentially – each writes variables consumed by the next.

> All notebooks assume the dataset is available at `data/MachineLearningRating_v3.txt`. Pull via `dvc pull` before execution.