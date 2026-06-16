
import pandas as pd


class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath


    def load_csv(self):
        try:
            df = pd.read_csv(self.filepath)
            print("CSV loaded successfully")
            return df

        except FileNotFoundError:
            raise Exception(
                f"File not found: {self.filepath}"
            )


    def dataset_info(self, df):

        info = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "column_names": df.columns.tolist(),
            "data_types": df.dtypes.to_dict()
        }

        return info
