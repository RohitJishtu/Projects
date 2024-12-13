# Chi Square Test 

from sklearn.feature_selection import chi2
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np

def chi_square_feature_selection(data, categorical_features, target, min_category_count=3, significance_level=0.05):
    """
    Perform Chi-Square test between categorical features and target after filtering sparse categories.

    Parameters:
        data (pd.DataFrame): The input DataFrame.
        categorical_features (list): List of categorical feature column names.
        target (str): The target column name.
        min_category_count (int): Minimum count for each category to be included in the analysis.
        significance_level (float): The p-value threshold for significance.

    Returns:
        pd.DataFrame: Chi-Square scores and p-values for each feature with p-value above the significance level.
    """
    filtered_features = []

    # Filter sparse categories
    for feature in categorical_features:
        value_counts = data[feature].value_counts()
        valid_categories = value_counts[value_counts >= min_category_count].index
        if len(valid_categories) > 1:
            filtered_features.append(feature)
            # Keep only valid categories, assign others to 'Other'
            data[feature] = data[feature].apply(lambda x: x if x in valid_categories else 'Other')

    if not filtered_features:
        raise ValueError("No categorical features with sufficient category counts.")

    # One-hot encode the filtered categorical features
    encoder = OneHotEncoder(drop='first')
    encoded_features = encoder.fit_transform(data[filtered_features])
    encoded_feature_names = encoder.get_feature_names_out(filtered_features)

    # Perform Chi-Square test
    chi_scores, p_values = chi2(encoded_features, data[target])

    # Combine results into a DataFrame
    results = pd.DataFrame({
        'Feature': encoded_feature_names,
        'Chi-Square Score': chi_scores,
        'p-Value': p_values
    }).sort_values(by='Chi-Square Score', ascending=False)

    # Filter results by significance level
    significant_results = results[results['p-Value'] > significance_level]


    return  encoded_features[significant_results]

