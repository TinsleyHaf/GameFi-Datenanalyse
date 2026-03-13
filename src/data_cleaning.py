def clean_data(df):
    # Remove missing values
    df = df.dropna()
    # Remove duplicate rows
    df = df.drop_duplicates()
    return df


def feature_engineering(df):
    # One-hot encode categorical variables
    df = pd.get_dummies(df)
    # Scale numerical features
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    return df

# Example usage:
# cleaned_df = clean_data(original_df)
# engineered_df = feature_engineering(cleaned_df)