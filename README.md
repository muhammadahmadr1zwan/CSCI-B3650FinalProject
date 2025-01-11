# **NBA Salaries Analysis 2022-2023: Data Mining Insights**

This project explores the relationships between NBA player performance metrics and salaries for the 2022-2023 season using data mining techniques. It highlights key patterns, correlations, and outliers while leveraging machine learning models for predictive analysis.

---

## **Directory Structure**

- **`data/`**: Contains datasets:
  - `nba_original.csv`: Original dataset with player stats and salaries.
  - `nba_updated.csv`: Cleaned and updated dataset.
  - `nba_normalized.csv`: Dataset normalized for modeling.

- **`src/`**: Modular scripts:
  - `data_preprocessing.py`: Data loading, cleaning, and normalization.
  - `eda.py`: Exploratory data analysis.
  - `model_training.py`: Machine learning models (Decision Tree and SVM).
  - `evaluation.py`: Metrics and model comparison.

- **`main.py`**: Script orchestrating the entire pipeline.

---

## **How to Run the Project**

1. **Install Required Libraries**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. **Execute the Main Script**:
   ```bash
   python main.py
   ```

---

## **Workflow**

### **1. Data Preprocessing**
- **Challenges**:
  - Missing values in features like FG%, TS%.
  - Outliers in Salary, Blocks, and Assists.
  - High skewness in numerical data.
- **Solutions**:
  - Imputed missing values or removed rows with critical gaps.
  - Preserved outliers for context but tracked their impact on models.
  - Standardized numerical features for consistency.

---

### **2. Exploratory Data Analysis (EDA)**

#### **Dataset Overview**
- Rows: 467  
- Columns: 52  
- Key Statistics:
  - Mean Salary: $8.42M
  - Max Salary: $48.07M
  - Mean Points per Game: 9.13

#### **Correlation Heatmap**
- Shows relationships between features like Salary, PTS, and MP:
  ![Screenshot 2025-01-10 184911](https://github.com/user-attachments/assets/122dbe10-f51e-470b-b947-52cafc370019)

#### **Box Plot: Salary Outliers**
- Highlights salary outliers exceeding $40M:
  ![image](https://github.com/user-attachments/assets/47345011-d387-4657-ac28-a20408e8e921)

#### **Skewness in Data**
Visualizes the distributions of key features:
- **Positively Skewed**: Salary, Free Throws, Blocks.
- **Symmetrical**: Games Played (GP), Personal Fouls (PF).
- **Negatively Skewed**: FG%, TS%.

  ![image](https://github.com/user-attachments/assets/603d5468-5e76-479c-8a98-7531e0ec930c)

#### **Outliers**
Outliers in key features:
- Salary: 48 extreme data points.
- Free Throws: 41 outliers.
- Blocks: 22 outliers.

  ![image](https://github.com/user-attachments/assets/0ab39f0e-e18c-48f3-8771-8b4b08a97b78)

---

### **3. Model Training**
- **Decision Tree**:
  - Interpretable and efficient for small datasets.
  - Handles non-linear relationships.
- **Support Vector Machine (SVM)**:
  - Superior accuracy for high-dimensional datasets.
  - Robust with regularization and kernel functions.

---

### **4. Model Evaluation**

| Model              | Split | MSE   | \(R^2\)    |
|--------------------|-------|-------|-----------|
| **Decision Tree**  | 80-20 | 0.092 | 0.936     |
| **SVM**            | 80-20 | 0.052 | 0.964     |

#### **Decision Tree Visualization**
Displays interpretable decision-making rules.

---

### **5. Insights**

#### **Key Takeaways**:
- Strong correlation between Salary and performance metrics like Points Per Game (PTS) and Minutes Played (MP).
- Guards display the most variability due to diverse roles.

#### **Applications**:
- **Salary Optimization**: Align contracts with player contributions.
- **Draft Strategy**: Predict high-potential players using metrics.
- **Fan Engagement**: Provide interpretable analytics for better transparency.

---

## **Conclusion**
- **Best Model**: Support Vector Machine (SVM)
  - Excels in accuracy and robustness.
  - Suitable for predictive analytics and salary forecasting.
- **Decision Tree**:
  - Valuable for interpretability and quick insights.
