# Water Quality Predictor

**Environmental machine learning · Multi-output regression · Flask dashboard**

Estimate nine water quality parameters from a monitoring station and year, explore the predictions in a chart, and export a report.

[Getting started](#getting-started) · [Model and data](#model-and-data) · [Project structure](#project-structure)

## What it does

- Predicts NH4, BSK5, suspended solids, O2, NO3, NO2, SO4, PO4, and chloride.
- Compares predictions with the thresholds configured in the application.
- Displays pollutant values and status in a browser dashboard with a dark-mode toggle.
- Exports the latest prediction as CSV or PDF.

## Technology

| Layer | Tools |
| --- | --- |
| Model | XGBoost with scikit-learn MultiOutputRegressor |
| Application | Python, Flask, pandas, joblib |
| Interface | HTML, CSS, JavaScript, Chart.js |
| Reports | CSV and xhtml2pdf |

## Getting started

Clone the project and create a Python virtual environment:

```bash
git clone https://github.com/Praveenraj1618/Water-Quality-Predictor.git
cd Water-Quality-Predictor
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in Windows PowerShell, or `source .venv/bin/activate` on macOS/Linux.

```bash
python -m pip install flask pandas joblib xhtml2pdf scikit-learn xgboost
```

Download [pollution_model.pkl](https://drive.google.com/file/d/1fzg02RD50EbjwT_-xIBFxZQqszbU59w6/view?usp=sharing) from the project's existing model link and place it in the repository root beside `model_columns.pkl`. The trained model is required at startup and is not committed here. Download availability and model compatibility must be checked in your environment.

```bash
python app.py
```

Open http://127.0.0.1:5000, select a station and year, and generate a prediction before exporting.

## Model and data

The [training notebook](water_qual_pred_.ipynb) contains the modeling work; [dataset.csv](dataset.csv) contains the committed data. The notebook is the starting point for inspecting preprocessing and evaluation. No independently reproduced performance score is claimed here.

The dashboard's “Safe,” “Clean,” and “Polluted” labels are comparisons against application-defined thresholds. They are model outputs, not laboratory measurements or certification. The current export implementation stores the latest prediction in process-wide memory, so this version is best demonstrated locally by one user at a time.

## Project structure

| Path | Purpose |
| --- | --- |
| `app.py` | Prediction routes, thresholds, CSV/PDF export |
| `templates/` | Dashboard and PDF templates |
| `static/` | Styles and dark-mode behavior |
| `water_qual_pred_.ipynb` | Model development notebook |
| `dataset.csv` | Committed dataset |
| `model_columns.pkl` | Expected encoded feature columns |

## Project context

Developed during the June 2025 AICTE virtual internship with Edunet Foundation, sponsored by Shell, focused on AI and ML for green technology and environmental monitoring.
