
from src.loader import DataLoader
from src.validator import DataValidator
from src.cleaner import DataCleaner
from src.analyzer import EDAAnalyzer
from src.feature_engineering import FeatureEngineer
from src.report_generator import ReportGenerator


class AutoEDA:

    def __init__(self, filepath):
        self.filepath = filepath


    def run(self):

        print("=" * 60)
        print("AUTO EDA PIPELINE STARTED")
        print("=" * 60)


        # Load Data
        loader = DataLoader(self.filepath)
        df = loader.load_csv()


        # Validate Data
        print("\n[1] Data Validation")

        validator = DataValidator(df)

        validation_report = validator.generate_report()

        print(validation_report)


        # Data Cleaning
        print("\n[2] Data Cleaning")

        cleaner = DataCleaner(df)

        clean_df = cleaner.clean()

        print(cleaner.get_logs())


        # EDA Analysis
        print("\n[3] EDA Analysis")

        analyzer = EDAAnalyzer(clean_df)

        print(
            analyzer.numerical_analysis()
        )


        print(
            analyzer.generate_insights()
        )


        # Feature Engineering
        print("\n[4] Feature Engineering")

        engineer = FeatureEngineer(clean_df)

        encoding = engineer.encode_categorical()

        engineer.scale_numerical()

        feature_df = engineer.get_data()


        print("Encoding Map:")

        print(encoding)


        # Generate Report
        print("\n[5] Generating Report")


        report = ReportGenerator(
            df,
            clean_df,
            feature_df
        )


        report.save_report(
            "AutoEDA_Report.txt"
        )


        print("\n" + "=" * 60)

        print("AUTO EDA PIPELINE COMPLETED")

        print("=" * 60)


        return {
            "raw_data": df,
            "clean_data": clean_df,
            "features": feature_df
        }
