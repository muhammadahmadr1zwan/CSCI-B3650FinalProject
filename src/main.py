from src.data_preprocessing import load_data, clean_data, normalize_data
from src.eda import plot_correlation_heatmap, plot_outliers, plot_histogram
from src.model_training import train_decision_tree, train_svm
from src.evaluation import evaluate_model
from sklearn.model_selection import train_test_split

# Load Data
original_data = load_data('data/nba_original.csv')
updated_data = load_data('data/nba_updated.csv')
normalized_data = load_data('data/nba_normalized.csv')

# Preprocessing
cleaned_data = clean_data(original_data)
numerical_features = ['PTS', 'TRB', 'AST', 'MP', 'Salary']
cleaned_data = normalize_data(cleaned_data, numerical_features)

# EDA
plot_correlation_heatmap(cleaned_data)
plot_outliers(cleaned_data, 'Salary')
plot_histogram(cleaned_data, 'PTS')

# Feature and Target Separation
X = cleaned_data[['PTS', 'TRB', 'AST', 'MP']]
y = cleaned_data['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
dt_model = train_decision_tree(X_train, y_train)
svm_model = train_svm(X_train, y_train)

# Evaluation
dt_mse, dt_r2 = evaluate_model(dt_model, X_test, y_test)
svm_mse, svm_r2 = evaluate_model(svm_model, X_test, y_test)

print(f'Decision Tree - MSE: {dt_mse}, R²: {dt_r2}')
print(f'SVM - MSE: {svm_mse}, R²: {svm_r2}')
