import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # Ensure that only numeric columns are considered
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df_numeric = df[numeric_cols]

    # 1. Descriptive Statistics
    print("### Descriptive Statistics:\n")
    desc_stats = df_numeric.describe().T
    desc_stats['mode'] = df_numeric.mode().iloc[0]
    desc_stats['variance'] = df_numeric.var()
    desc_stats['skewness'] = df_numeric.skew()
    desc_stats['kurtosis'] = df_numeric.kurtosis()
    display_cols = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'mode', 'variance', 'skewness', 'kurtosis']
    print(desc_stats[display_cols])

    # 2. Outlier Detection using Box Plots
    print("\n### Box Plots for Outlier Detection:")
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df_numeric[col])
        plt.title(f'Box Plot of {col}')
        plt.xlabel(col)
        plt.show()

    # 3. Correlation Analysis
    print("\n### Correlation Matrix:")
    corr_matrix = df_numeric.corr()
    print(corr_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()

    # 4. Explanation of Findings
    print("\n### Explanation of Findings:")

    # Descriptive Statistics Findings
    print("\n#### Descriptive Statistics Findings:")
    for col in numeric_cols:
        mean = desc_stats.loc[col, 'mean']
        median = desc_stats.loc[col, '50%']
        mode = desc_stats.loc[col, 'mode']
        std_dev = desc_stats.loc[col, 'std']
        skewness = desc_stats.loc[col, 'skewness']

        print(f"\n**Column '{col}':**")
        print(f"- Mean: {mean:.2f}")
        print(f"- Median: {median:.2f}")
        print(f"- Mode: {mode:.2f}")
        print(f"- Standard Deviation: {std_dev:.2f}")
        print(f"- Skewness: {skewness:.2f}")
        if skewness > 0.5:
            print("  - The distribution is positively skewed.")
        elif skewness < -0.5:
            print("  - The distribution is negatively skewed.")
        else:
            print("  - The distribution is approximately symmetric.")

    # Outlier Detection Findings
    print("\n#### Outlier Detection Findings:")
    for col in numeric_cols:
        Q1 = df_numeric[col].quantile(0.25)
        Q3 = df_numeric[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df_numeric[(df_numeric[col] < lower_bound) | (df_numeric[col] > upper_bound)][col]
        print(f"\n**Column '{col}':**")
        print(f"- Number of outliers: {outliers.count()}")
        if outliers.count() > 0:
            print(f"- Outlier values:\n{outliers.values}")
        else:
            print("- No significant outliers detected.")

    # Correlation Analysis Findings
    print("\n#### Correlation Analysis Findings:")
    high_corr = corr_matrix.abs().unstack().sort_values(ascending=False)
    high_corr = high_corr[high_corr < 1]  # Exclude self-correlation
    high_corr = high_corr.drop_duplicates()
    threshold = 0.7
    high_corr_pairs = high_corr[high_corr > threshold]
    if not high_corr_pairs.empty:
        print(f"\nPairs of variables with correlation coefficient higher than {threshold}:")
        for idx, value in high_corr_pairs.iteritems():
            print(f"- {idx[0]} and {idx[1]}: {value:.2f}")
    else:
        print("- No pairs with high correlation found.")


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
