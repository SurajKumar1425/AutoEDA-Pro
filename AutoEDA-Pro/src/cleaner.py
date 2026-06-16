
import pandas as pd


class DataCleaner:

    def __init__(self, df):
        self.df = df.copy()
        self.logs = []


    def add_log(self, message):
        self.logs.append(message)


    def handle_missing(self):

        for col in self.df.columns:

            if self.df[col].dtype in ["int64", "float64"]:
                value = self.df[col].median()
                self.df[col] = self.df[col].fillna(value)

                self.add_log(
                    f"{col}: Missing values filled with median ({value})"
                )

            else:
                value = self.df[col].mode()[0]
                self.df[col] = self.df[col].fillna(value)

                self.add_log(
                    f"{col}: Missing values filled with mode ({value})"
                )


    def remove_duplicates(self):

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        removed = before - len(self.df)

        self.add_log(
            f"Removed {removed} duplicate rows"
        )


    def clean_text(self):

        text_columns = self.df.select_dtypes(
            include="object"
        ).columns


        for col in text_columns:

            self.df[col] = (
                self.df[col]
                .str.strip()
                .str.lower()
            )

            self.add_log(
                f"{col}: Text standardized"
            )


    def detect_outliers(self):

        result = {}

        numeric_columns = self.df.select_dtypes(
            include="number"
        ).columns


        for col in numeric_columns:

            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr


            count = (
                (self.df[col] < lower)
                |
                (self.df[col] > upper)
            ).sum()

            result[col] = count


        return pd.DataFrame(
            result.items(),
            columns=[
                "Column",
                "Outlier Count"
            ]
        )


    def clean(self):

        self.handle_missing()
        self.remove_duplicates()
        self.clean_text()

        return self.df


    def get_logs(self):

        return self.logs
