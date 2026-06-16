
import pandas as pd


class DataValidator:

    def __init__(self, df):
        self.df = df


    def check_shape(self):
        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1]
        }


    def check_missing(self):
        missing = self.df.isnull().sum()
        percentage = (missing / len(self.df)) * 100

        report = pd.DataFrame({
            "Missing Values": missing,
            "Percentage": percentage
        })

        return report[report["Missing Values"] > 0]


    def check_duplicates(self):
        return self.df.duplicated().sum()


    def check_datatypes(self):
        return self.df.dtypes


    def unique_values(self):
        return pd.DataFrame({
            "Column": self.df.columns,
            "Unique Values": [
                self.df[col].nunique()
                for col in self.df.columns
            ]
        })


    def data_quality_score(self):

        total_cells = (
            self.df.shape[0] *
            self.df.shape[1]
        )

        missing_cells = (
            self.df.isnull().sum().sum()
        )

        duplicate_rows = (
            self.df.duplicated().sum()
        )

        score = 100 - (
            (missing_cells / total_cells) * 100
            +
            (duplicate_rows / len(self.df)) * 100
        )

        return round(max(score, 0), 2)


    def generate_report(self):

        return {
            "Shape": self.check_shape(),
            "Missing": self.check_missing(),
            "Duplicates": self.check_duplicates(),
            "Data Types": self.check_datatypes(),
            "Unique Values": self.unique_values(),
            "Quality Score": self.data_quality_score()
        }
