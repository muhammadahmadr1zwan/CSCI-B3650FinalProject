from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

def train_decision_tree(X_train, y_train, max_depth=10):
    dt_model = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    dt_model.fit(X_train, y_train)
    return dt_model

def train_svm(X_train, y_train):
    svm_model = SVR(kernel='rbf')
    svm_model.fit(X_train, y_train)
    return svm_model
