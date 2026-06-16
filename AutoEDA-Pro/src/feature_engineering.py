
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


class FeatureEngineer:

    def __init__(self, df):
        self.df = df.copy()
        self.logs = []


    def add_log(self, message):
        self.logs.append(message)


    def encode_categorical(self):

        encoders = {}

        cat_cols = self.df.select_dtypes(
            include="object"
        ).columns


        for col in cat_cols:

            encoder = LabelEncoder()

            self.df[col] = encoder.fit_transform(
                self.df[col]
            )

            encoders[col] = dict(
                zip(
                    encoder.classes_,
                    encoder.transform(
                        encoder.classes_
                    )
                )
            )

            self.add_log(
                f"{col} encoded using LabelEncoder"
            )


        return encoders


    def scale_numerical(self):

        numeric_cols = self.df.select_dtypes(
            include="number"
        ).columns


        scaler = StandardScaler()

        self.df[numeric_cols] = scaler.fit_transform(
            self.df[numeric_cols]
        )


        self.add_log(
            "Numerical features scaled using StandardScaler"
        )


    def extract_date_features(self, column):

        self.df[column] = pd.to_datetime(
            self.df[column]
        )


        self.df[f"{column}_year"] = (
            self.df[column].dt.year
        )

        self.df[f"{column}_month"] = (
            self.df[column].dt.month
        )

        self.df[f"{column}_day"] = (
            self.df[column].dt.day
        )

        self.df[f"{column}_weekday"] = (
            self.df[column].dt.day_name()
        )


        self.add_log(
            f"Date features extracted from {column}"
        )


    def get_data(self):
        return self.df


    def get_logs(self):
        return self.logs
