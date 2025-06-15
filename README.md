# End-to-End Insurance Risk Analytics & Predictive Modeling

Notebook-driven project for analysing motor-insurance risk, testing hypotheses, and building predictive models for risk-based pricing.

---

## Repository Structure

```
.
├── data/                 # DVC-tracked raw dataset
├── notebooks/            # Jupyter notebooks (EDA → Hypothesis → Modeling)
├── scripts/              # Helper scripts (placeholder)
├── test/                 # Pytest tests
├── requirements.txt      # Python deps
└── README.md             # Project overview (this file)
```

### Key Notebooks
| Notebook | Task | Purpose |
|----------|------|---------|
| `task1_eda.ipynb`        | 1 | Exploratory data analysis. |
| `hypothesis_testing.ipynb` | 3 | Non-parametric tests on Loss Ratio (control vs test segmentation). |
| `modeling.ipynb`         | 4 | Severity & frequency models, SHAP interpretation, risk-based premium demo. |

*(Task-2 data preparation & feature engineering are included in the **task1_eda.ipynb** notebook.)*

---

## Quick-Start

```bash
# clone repo & pull data
git clone https://github.com/<org>/<repo>.git
cd End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
dvc pull                        # downloads dataset (~35 MB)

# create env on supported python (≤ 3.12) and install deps
python -m venv .venv
.\.venv\Scripts\activate        # Windows – adjust for macOS / Linux
python -m pip install -r requirements.txt

# launch jupyter
jupyter lab
```
Run notebooks in order: **task1_eda → hypothesis_testing → modeling**.

---

## Branch Workflow

* `main`   – Stable, production-ready code.
* `task-1` – Exploratory Data Analysis.
* `task-2` – Data preparation & feature engineering.
* `task-3` – Hypothesis testing (single KPI).
* `task-4` – Predictive modeling & pricing framework.

Open PRs from task branches into `main` once the task is complete.

---

## Dependencies (excerpt)

* pandas, numpy, matplotlib, seaborn
* scikit-learn ≥ 1.4 (requires Python ≤ 3.12 at time of writing)
* xgboost, shap
* dvc – data version control

> Using Python 3.13? scikit-learn wheels are not yet published; use 3.12 or build from source.

---

## Testing

```bash
pytest -q
```
Add tests under `test/` as scripts are refactored from notebooks.

---

## Contributing

1. Fork & create feature branch off the relevant `task-*` branch.
2. Ensure notebooks run end-to-end (`Kernel → Restart & Run All`).
3. Commit with meaningful messages (`feat: add tweedie GLM`).
4. Open a pull request; CI will run lint & tests.

---

© 2025 Windsurf Analytics – MIT License.
