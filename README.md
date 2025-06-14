# End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains an end-to-end, notebook-driven workflow for analysing South-African motor-insurance risk factors, performing statistical hypothesis tests, and building predictive models to support risk-based pricing.

---

## Repository Structure

```
.
├── data/                       # DVC-tracked raw dataset (MachineLearningRating_v3.txt)
├── notebooks/                  # Jupyter notebooks (EDA, hypothesis testing, modelling)
├── scripts/                    # Helper scripts / utilities (placeholder)
├── test/                       # Unit / integration tests (pytest)
├── requirements.txt            # Python dependencies
└── README.md                   # You are here
```

### Key Notebooks
| Notebook | Task | Purpose |
|----------|------|---------|
| `notebooks/task1_eda.ipynb` | **Task-1** | Exploratory Data Analysis – distributions, correlations, missing-values. |
| `notebooks/hypothesis_testing.ipynb` | **Task-3** | Non-parametric hypothesis tests on Loss Ratio (single KPI) with control / test segmentation. |
| `notebooks/modeling.ipynb` | **Task-4** | Claim-severity regression, probability-of-claim classification, SHAP interpretation & risk-based pricing illustration. |

>  *Tasks 2 & 3 are combined in the hypothesis-testing notebook, while Task-4 introduces the advanced modelling pipeline.*

---

## Quick-start

1. **Clone the repository & initialise DVC data**
   ```bash
   git clone https://github.com/<org>/<repo>.git
   cd End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
   dvc pull               # downloads the ~35 MB dataset from remote storage
   ```

2. **Create a Python ≥ 3.11 virtual environment** (scikit-learn ≥ 1.4 wheels not yet available for 3.13).
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate    # Windows – on Linux/Mac: source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

3. **Launch JupyterLab**
   ```bash
   jupyter lab
   ```
   Run the notebooks in order (`task1_eda → hypothesis_testing → modeling`).

---

## Branch Workflow

* `main` – Production-ready code / notebooks.
* `task-3` – Hypothesis-testing development (merged).
* `task-4` – Predictive modelling & pricing (active).

Use feature branches off `task-4` for further modelling tweaks; open pull-requests towards `task-4`, then PR into `main` once complete.

---

## Dependencies

See `requirements.txt`.  Key packages:
* pandas, numpy, matplotlib, seaborn
* scikit-learn ≥ 1.4 (classification & regression)
* xgboost
* shap (model interpretability)
* dvc (data version control)

> **Note:** If you need to work on Python 3.13, scikit-learn wheels are not yet published – use Python 3.12 or below, or build scikit-learn from source.

---

## Running the Tests

Pytest is configured in CI.  From the project root:
```bash
pytest -q
```
Add tests in `test/` as you enhance scripts.

---

## Contributing

1. Fork the repo & create a feature branch.
2. Commit descriptive messages (e.g. `feat: add Tweedie GLM severity model`).
3. Ensure notebooks run end-to-end without errors (`Kernel → Restart & Run All`).
4. Submit a pull request; the CI pipeline will run lint & tests.

---

## Maintainers

Project maintained by the Analytics Engineering team.

---

© 2025 Windsurf Analytics. Licensed under the MIT License.
