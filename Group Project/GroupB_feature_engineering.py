def feature_engineering_rf(X):
    X = X.copy()

    # Binary columns encoding
    columns_to_transform = ["Smoking", "Family_History_of_Anxiety", "Medication", "Dizziness", "Recent_Major_Life_Event"]
    mapping = {"yes": 1, "no": 0}  # Convert the values: "yes" becomes 1 and "no" becomes 0
    for col in columns_to_transform:
        X[col] = X[col].str.lower().map(mapping)

    # Create dummies for occupation
    X = pd.get_dummies(X, columns=['Occupation'], drop_first=True)
    occupation_dummy_cols = [col for col in X.columns if 'Occupation_' in col]
    X[occupation_dummy_cols] = X[occupation_dummy_cols].astype(int)

    # Gender encoding: 1 for Female, 0 for others
    X['Gender'] = X['Gender'].apply(lambda x: 1 if x.lower() == 'female' else 0)

    # Drop unnecessary columns
    return X.drop(columns=['ID', 'Heart_Rate_(bpm_during_attack)','Severity_of_Anxiety_Attack_(1-10)'], errors='ignore')