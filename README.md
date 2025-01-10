# NBA Salaries Analysis 2022-2023: Uncovering Performance Insights with Data Mining

This project analyzes NBA player salaries for the 2022-2023 season using data mining techniques. It includes preprocessing, exploratory data analysis (EDA), and model training.

## Directory Structure

- `data/`: Contains the datasets.
  - `nba_original.csv`: The original dataset with all player stats and salaries.
  - `nba_updated.csv`: The updated dataset after initial cleaning.
  - `nba_normalized.csv`: The normalized dataset for model training.
  
- `src/`: Modularized scripts for different components of the analysis.
  - `data_preprocessing.py`: Handles data loading, cleaning, and normalization.
  - `eda.py`: Contains functions for exploratory data analysis, including visualizations.
  - `model_training.py`: Implements Decision Tree and SVM models.
  - `evaluation.py`: Provides evaluation metrics for trained models.

- `main.py`: The main script to orchestrate the entire pipeline, from data loading to model evaluation.

## How to Run the Project

1. **Install Required Libraries**:
   Ensure the following Python libraries are installed:
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `seaborn`
   - `scikit-learn`

   You can install these using:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. **Run the Main Script**:
   Execute `main.py` to run the full pipeline:
   ```bash
   python main.py
   ```

   This will:
   - Load and preprocess the dataset.
   - Perform exploratory data analysis (EDA).
   - Train models (Decision Tree and SVM).
   - Evaluate models and display results.

## Project Workflow

1. **Data Preprocessing**:
   - Handles missing values.
   - Normalizes numerical features like `PTS`, `TRB`, and `Salary`.

2. **Exploratory Data Analysis (EDA)**:
   - Visualizes correlations between variables using heatmaps.
   - Highlights outliers in salary and key performance metrics.
   - Explores distributions of player stats like `PTS` and `AST`.

3. **Model Training**:
   - Trains two models:
     - **Decision Tree**: For interpretable rules and non-linear relationships.
     - **SVM**: For accuracy and robustness in high-dimensional data.

4. **Evaluation**:
   - Measures model performance using metrics like:
     - Mean Squared Error (MSE)
     - \(R^2\) Score

## Results Summary

| Model              | MSE   | \(R^2\)    |
|--------------------|-------|-----------|
| **Decision Tree**  | 0.092 | 0.936     |
| **SVM**            | 0.052 | 0.964     |

## Insights

- **Key Factors**:
  - Player performance metrics (`PTS`, `MP`) strongly correlate with salary.
  - Guards exhibit the most variability due to diverse roles.

- **Applications**:
  - Optimize player contracts based on performance metrics.
  - Predict draft success and future salaries.
  - Engage fans with interpretable salary insights.
