# Feature Engineering Random Forest

def feature_engineering(X):
    df_rf = X.copy()
    df_rf["International plan"] = df_rf["International plan"].map({"Yes": 1, "No": 0})
    df_rf["Voice mail plan"] = df_rf["Voice mail plan"].map({"Yes": 1, "No": 0})
    df_rf['Total Usage'] = df_rf[['Total day minutes','Total eve minutes','Total night minutes','Total intl minutes']].sum(axis=1)
    df_rf['Total Charge'] = df_rf[['Total day charge','Total eve charge','Total night charge','Total intl charge']].sum(axis=1)
    df_rf.drop(columns=[
        'Total day minutes','Total eve minutes','Total night minutes','Total intl minutes',
        'Total day charge','Total eve charge','Total night charge','Total intl charge'
    ], inplace=True)
    return df_rf