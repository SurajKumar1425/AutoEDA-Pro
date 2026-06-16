
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


class Visualizer:

    def __init__(self, df):
        self.df = df


    def plot_histograms(self):

        numeric_cols = self.df.select_dtypes(
            include="number"
        ).columns

        self.df[numeric_cols].hist(
            figsize=(12, 6),
            bins=20
        )

        plt.suptitle(
            "Numerical Feature Distributions"
        )

        plt.show()


    def plot_boxplots(self):

        numeric_cols = self.df.select_dtypes(
            include="number"
        ).columns


        for col in numeric_cols:

            plt.figure(figsize=(6, 4))

            sns.boxplot(
                x=self.df[col]
            )

            plt.title(
                f"Boxplot of {col}"
            )

            plt.show()


    def correlation_heatmap(self):

        corr = self.df.corr(
            numeric_only=True
        )

        plt.figure(figsize=(8, 5))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm"
        )

        plt.title(
            "Correlation Matrix"
        )

        plt.show()


    def categorical_plots(self):

        cat_cols = self.df.select_dtypes(
            include="object"
        ).columns


        for col in cat_cols:

            plt.figure(figsize=(6, 4))

            sns.countplot(
                x=self.df[col]
            )

            plt.title(
                f"Count Plot of {col}"
            )

            plt.xticks(rotation=45)

            plt.show()


    def scatter_plots(self):

        numeric_cols = list(
            self.df.select_dtypes(
                include="number"
            ).columns
        )


        for i in range(len(numeric_cols)):

            for j in range(
                i + 1,
                len(numeric_cols)
            ):

                plt.figure(figsize=(6, 4))

                sns.scatterplot(
                    x=self.df[numeric_cols[i]],
                    y=self.df[numeric_cols[j]]
                )

                plt.xlabel(
                    numeric_cols[i]
                )

                plt.ylabel(
                    numeric_cols[j]
                )

                plt.title(
                    f"{numeric_cols[i]} vs {numeric_cols[j]}"
                )

                plt.show()


    def interactive_scatter(
        self,
        x,
        y
    ):

        fig = px.scatter(
            self.df,
            x=x,
            y=y,
            title=f"{x} vs {y}"
        )

        fig.show()
