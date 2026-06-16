
class ReportGenerator:

    def __init__(self, original_df, cleaned_df, feature_df):
        self.original_df = original_df
        self.cleaned_df = cleaned_df
        self.feature_df = feature_df
        self.report = []


    def add_section(self, title, content):
        self.report.append("\n" + "=" * 60)
        self.report.append(title)
        self.report.append("=" * 60)
        self.report.append(str(content))


    def dataset_summary(self):

        summary = {
            "Original Shape": self.original_df.shape,
            "Cleaned Shape": self.cleaned_df.shape,
            "Feature Data Shape": self.feature_df.shape,
            "Total Features": self.feature_df.shape[1]
        }

        self.add_section(
            "DATASET SUMMARY",
            summary
        )


    def missing_report(self):

        missing = self.cleaned_df.isnull().sum()

        self.add_section(
            "MISSING VALUE REPORT",
            missing[missing > 0]
        )


    def statistical_summary(self):

        stats = self.cleaned_df.describe(
            include="all"
        )

        self.add_section(
            "STATISTICAL SUMMARY",
            stats
        )


    def feature_information(self):

        info = self.feature_df.dtypes

        self.add_section(
            "FEATURE DATA TYPES",
            info
        )


    def generate_report(self):

        self.dataset_summary()
        self.missing_report()
        self.statistical_summary()
        self.feature_information()

        return "\n".join(
            self.report
        )


    def save_report(self, filename):

        report = self.generate_report()

        with open(filename, "w") as file:
            file.write(report)

        return f"Report saved: {filename}"
