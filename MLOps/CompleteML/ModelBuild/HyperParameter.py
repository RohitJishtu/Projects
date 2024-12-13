from sklearn.model_selection import GridSearchCV

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 5, 6, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [None, 'sqrt', 'log2']
}

def GridSerach(Model,X_test,p_class,CV=5,scoring='f1',verbose=1, n_jobs=-1):
    grid_search = GridSearchCV(estimator=Model, param_grid=param_grid, cv=CV, scoring=scoring, verbose=verbose, n_jobs=-n_jobs)
    grid_search.fit(X_test, p_class)
    best_params = grid_search.best_params_
    best_classifier = grid_search.best_estimator_

    return best_classifier