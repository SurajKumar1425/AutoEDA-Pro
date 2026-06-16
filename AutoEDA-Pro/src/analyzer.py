
import pandas as pd


class EDAAnalyzer:

    def __init__(self, df):
        self.df = df


    def summary_statistics(self):
        return self.df.describe(include="all").T


    def numerical_analysis(self):

        numeric = self.df.select_dtypes(include="number")

        report = pd.DataFrame({
            "Mean": numeric.mean(),
            "Median": numeric.median(),
            "Std Dev": numeric.std(),
            "Min": numeric.min(),
            "Max": numeric.max(),
            "Skewness": numeric.skew(),
            "Kurtosis": numeric.kurtosis()
        })

        return report


    def correlation_analysis(self):
        return self.df.corr(numeric_only=True)


    def categorical_analysis(self):

        result = {}

        categories = self.df.select_dtypes(
            include="object"
        ).columns


        for col in categories:

            result[col] = (
                self.df[col]
                .value_counts()
                .to_dict()
            )

        return result


    def generate_insights(self):

        insights = []

        numeric = self.df.select_dtypes(
            include="number"
        )


        for col in numeric.columns:

            skew = numeric[col].skew()


            if skew > 1:

                insights.append(
                    f"{col} is highly positively skewed"
                )


            elif skew < -1:

                insights.append(
                    f"{col} is highly negatively skewed"
                )


            else:

                insights.append(
                    f"{col} has approximately normal distribution"
                )


        return insights
