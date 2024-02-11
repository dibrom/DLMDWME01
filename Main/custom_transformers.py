from sklearn.base import BaseEstimator, TransformerMixin

# Definieren Sie die 'extract_time_features' Funktion
def extract_time_features(df):
    # df['tmsp'] = pd.to_datetime(df['tmsp'])
    df['hour'] = df['tmsp'].dt.hour
    df['minute'] = df['tmsp'].dt.minute
    df['second'] = df['tmsp'].dt.second
    df['weekday'] = df['tmsp'].dt.weekday
    return df[['hour', 'minute', 'second', 'weekday']]

class TimeFeaturesExtractor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return extract_time_features(X)