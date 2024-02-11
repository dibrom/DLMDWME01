from sklearn.base import BaseEstimator, TransformerMixin

class TimeFeaturesExtractor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def extract_time_features(df):
        #df['tmsp'] = pd.to_datetime(df['tmsp'])
        df['hour'] = df['tmsp'].dt.hour
        df['minute'] = df['tmsp'].dt.minute
        df['second'] = df['tmsp'].dt.second
        df['weekday'] = df['tmsp'].dt.weekday
        return df[['hour', 'minute', 'second', 'weekday']]